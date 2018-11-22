import sys, json
from flask import Flask, request, abort

app = Flask(__name__)


@app.route('/', methods=['POST'])

def webhook():
    print("webhook"); sys.stdout.flush()
    if request.method == 'POST' and request.headers['content-type'] == 'application/x-www-form-urlencoded':
        data = json.loads(request.form['payload'])
        print(data)
        return '', 200
    elif request.method == 'POST' and request.headers['content-type'] == 'application/json':
        data = json.loads(request.data)
        print(request.json)
        return '', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run()