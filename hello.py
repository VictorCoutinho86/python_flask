from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello/<user>')
def hello_name(user):
    return render_template('hello.html', name=user)


@app.route('/score/<int:score>')
def hello_score(score):
    return render_template('score.html', marks=score)


if __name__ == '__main__':
    app.run(debug=True)
