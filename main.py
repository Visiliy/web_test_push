from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return '''<h1>Hello, world</h>
              <a href="/index">index</a>'''


@app.route('/index')
def href():
    return '''<h1>Hello</h1>
    <a href="/">index</a>'''


if __name__ == '__main__':
    app.run(debug=True, port=7000)