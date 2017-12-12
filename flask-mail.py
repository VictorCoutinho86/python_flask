from flask_mail import Mail, Message
from flask import Flask

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'victormelo@id.uff.br'
app.config['MAIL_PASSWORD'] = '******'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route('/')
def index():
    msg = Message(
        'Hello',
        sender='victormelo@id.uff.br',
        recipients=['victormelo@id.uff.br', 'fonsa19@hotmail.com'])
    msg.body = "Hello From my first Flask Mail sent!"
    mail.send(msg)
    return "Sent"


if __name__ == '__main__':
    app.run(debug=True)


