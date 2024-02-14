from flask import *
from  flask_mail import*
app=Flask(__name__)







app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='annmaryrose152@gmail.com'
app.config['MAIL_PASSWORD']='qlre taip itfh sndf'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True


mail=Mail(app)

@app.route('/')
def send_mymail():
    msg=Message('subject',sender='annmaryrose152@gmail.com',recipients=['annmaryrose53@gmail.com'])
    msg.body="my flask msg"
    mail.send(msg)
    return 'success'

if __name__=="__main__":
    app.run(debug=True)       



