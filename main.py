from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        job_reqs = request.form['reqs']
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