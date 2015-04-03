""" hello.py """

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
        'hello': 'world'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0')
