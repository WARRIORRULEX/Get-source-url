from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        try:
            response = requests.get(url)
            source_code = response.text
            return f"""
                <h1>Source Code:</h1>
                <form method="post">
                    <label for="url">URL:</label>
                    <input type="text" id="url" name="url" placeholder="URL डालें" required>
                    <button type="submit">Get Source Code</button>
                </form>
                <h2>Source Code:</h2>
                <pre>{source_code}</pre>
            """
        except requests.exceptions.RequestException as e:
            return f"""
                <h1>Source Code:</h1>
                <form method="post">
                    <label for="url">URL:</label>
                    <input type="text" id="url" name="url" placeholder="URL डालें" required>
                    <button type="submit">Get Source Code</button>
                </form>
                <p style="color: red;">Error: {e}</p>
            """
    return """
        <h1>Source Code:</h1>
        <form method="post">
            <label for="url">URL:</label>
            <input type="text" id="url" name="url" placeholder="URL डालें" required>
            <button type="submit">Get Source Code</button>
        </form>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
