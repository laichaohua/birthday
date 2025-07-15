from flask import Flask,render_template
from flask_mail import Mail, Message

app =Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = '	laizhaohua88@gmail.com'

app.config['MAIL_PASSWORD'] = 'omfedoaxbzdpzdfy'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
    msg = Message('Happy Birthday', sender = 'laizhaohua88@gmail.com', recipients = ['diligent2718@gmail.com'])

    msg.body = "Hello Flask message sent from Flask-Mail"
    msg.html="<p>點我打開驚喜<a href='/birthday'>生日快樂</a></p>"
    mail.send(msg)
    return "Sent"

@app.route("/birthday")
def birthday():
    return render_template("birthday.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=10000)