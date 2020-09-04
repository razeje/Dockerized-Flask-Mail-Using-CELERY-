from flask import Flask
from flask_mail import Mail, Message
from flask_restful import Resource, Api
from tasks import make_celery
import config

app = Flask(__name__)
api = Api(app)
celery = make_celery(app)
#c = Celery('flasksmtp', backend='rpc://', broker='amqp://guest:@localhost:5672//')


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = config.EMAIL_ADDRESS
app.config['MAIL_PASSWORD'] = config.PASSWORD
mail = Mail(app)


class Mail(Resource):
    def get(self):
        mailkar.delay()
        return "task assigned"


@celery.task(name='Mail.mailkar')
def mailkar():
    msg = Message("DOCKERIZED CELERY AND MAIL API ", sender=config.EMAIL_ADDRESS, recipients=[config.EMAIL_ADDRESS])
    msg.body = "hello testing api"
    msg.html = "<b>hello testing celery mail</b>"
    mail.send(msg)
    return "message sent"


api.add_resource(Mail,'/mail')
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug = True )



