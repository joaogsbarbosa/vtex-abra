from flask import Flask, render_template, request, session, Response

import abrapi

app = Flask(__name__)

app.secret_key = b"1\xfe&\xbdI\nAA\x8c\xdd'M\xfe\xb8r\x10"

abrapi.rodar()

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
