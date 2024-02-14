from flask import Flask

app=Flask(__name__)  #creating a flask object obj


@app.route('/bb')    #url mapping associatec with func  / syntax/ app.route(rule,options)
def home():
    return "<h1>welcome to flask</h1>"




@app.route('/hai/<myname>')
def details(myname):
    return 'hai my name is'+myname

@app.route('/hai/<int:num>')
def mynum (num):
    return 'my num is %d' %num



def myhome():
    return'my home page'

app.add_url_rule('/myhome','myhome',myhome)




if __name__=="__main__":
    app.run(debug=True)   #syntax/app.run(host,port,debug,options)
