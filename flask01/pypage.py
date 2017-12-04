#!/usr/local/bin/python3
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world$$'

@app.route('/test/<int:testid>')
def test(testid):
    return 'haha %s' % testid

@app.route('/test2')
def test2():
    return 'test2'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')