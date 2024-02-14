from flask import*
app=Flask(__name__) 


@app.route('/login',methods=['GET'])
def reg():
    uname=request.args.get('name')
    place=request.args.get('place')
    return 'saved'+uname+place


if __name__=="__main__":
    app.run(debug=True)   

