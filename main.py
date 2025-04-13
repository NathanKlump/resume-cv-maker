from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv

import os

app = Flask(__name__)

def send_message(job_reqs):
    url = "https://open-ai21.p.rapidapi.com/conversationllama"
    headers = {
        'Content-Type': 'application/json',
        'x-rapidapi-host': os.getenv('x-rapidapi-host'),
        'x-rapidapi-key': os.getenv('x-rapidapi-key'),
    }
    data = {
        "messages": [{"role": "user", "content": job_reqs}],
        "web_access": False
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        job_reqs = request.form['reqs']
        resp = send_message(job_reqs)
        print(resp)
        return f"Job requirements received: {job_reqs}"
    return '''
        <form method="post">
            <label for="requirements">Enter Job Requirements:</label><br>
            <textarea id="requirements" name="reqs" rows="4" cols="50"></textarea><br>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)