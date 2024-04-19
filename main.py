from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index')
def href():
    return render_template('fh.html')


if __name__ == '__main__':
    app.run(debug=True, port=7000)