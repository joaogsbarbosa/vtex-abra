from flask import Flask, render_template, request, session, Response

import abrapi

app = Flask(__name__)

app.secret_key = b"1\xfe&\xbdI\nAA\x8c\xdd'M\xfe\xb8r\x10"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/1', methods=["POST"])
def dbcon():
    json = request.get_json()

    session['host'] = json['host']
    session['username'] = json['username']
    session['password'] = json['password']
    session['dbname'] = json['dbname']

    try:
        conn = abrapi.models.ApiToTable(session['host'], session['dbname'], session['username'],
                                        session['password'])
    except Exception as exec:
        return Response(status=400)

    return Response(status=200)


@app.route('/api/2', methods=["POST"])
def req():
    json = request.get_json()

    url = json['url']
    headers = json['headers']
    path = json['path']
    table_name = json['table_name']

    conn = abrapi.models.ApiToTable(session['host'], session['dbname'], session['username'], session['password'])

    conn.request(url, headers, path)
    conn.table_name = table_name

    conn.execute()

    return Response(status=200)


if __name__ == "__main__":
    app.run()
