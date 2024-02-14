from flask import *
app=Flask(__name__)  

app.secret_key="aaaaa"


@app.route('/')
def emp_reg():
    return render_template('day2red.html')


@app.route('/su',methods=['GET','POST'])
def emp_details():
    if request.method=="POST":
        res=request.form
        return render_template('my_details.html',data=res)

@app.route('/cs')
def cook_set():
    res=make_response("<h1>cookie set </h1>")
    res.set_cookie('place','ekm')
    return res


@app.route('/cg')
def cook_get():
    res=request.cookies.get('place')
    return res


@app.route('/ss')
def sess_set():
    res=make_response("<h1>session is set <a href='/sg'>view details</a></h1>")
    session['phone']=8714311513
    return res


@app.route('/sg')
def sess_get():
    if'phone' in session:
        c=session['phone']
        return'my session value is %d <a href="/sd">LOGOUT</a>'%c
    else:
        return'no session value found'
    

@app.route('/sd')
def sess_del():
    if 'phone' in session:
        session.pop('phone',None)
        return'logouted'
    else:
        return'no session value found'

@app.route('/upld')
def emp_upload():
    return render_template('myimage.html')

@app.route('/upldsave',methods=['POST'])
def emp_upld_save():
    if request.method=="POST":
        f=request.files['img']
        f.save(f.filename)
        return 'success'








if __name__=="__main__":
    app.run(debug=True)       
