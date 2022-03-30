from flask import Flask, render_template

app = Flask(__name__)


@app.route('/distribution')
def disrtibution():
    return render_template('accommodation.html', title='Размещение')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')