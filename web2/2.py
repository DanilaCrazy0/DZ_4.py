from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/table/<string:sex>/<int:number>')
def table(sex, number):
    if sex == 'male' and number >= 25:
        return render_template("table.html", color='blue', image=url_for('static', filename='img/bigg.jpg'), title='table')
    if sex == 'male' and number < 25:
        return render_template("table.html", color='#00b3ff', image=url_for('static', filename='img/little.jpg'), title='table')
    if sex == 'female' and number >= 25:
        return render_template("table.html", color='red', image=url_for('static', filename='img/big.jpg'), title='table')
    if sex == 'female' and number < 25:
        return render_template("table.html", color='pink', image=url_for('static', filename='img/little.jpg'), title='table')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')