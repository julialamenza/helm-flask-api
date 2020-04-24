from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/will')
def hello():
    return jsonify(message='Hello World')


@app.route('/ready')
def ready():
    return jsonify(message='It Works!!')


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port="8075")
