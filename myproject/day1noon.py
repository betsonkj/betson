from flask import*

app=Flask(__name__)

@app.route('/a')
def admin():
    return'ADMIN'

@app.route('/t')
def teacher():
    return'TEACHER'

@app.route('/s')
def student():
    return'STUDENT'

# ------------------------------------------------------


@app.route('/user/<name>')
def user(name):
    if name=="ad":
        return redirect(url_for('admin'))
    
    if name=="tea":
        return redirect(url_for('teacher'))
    
    if name=="stu":
        return redirect(url_for('student'))

# ------------------------------------------------------
    


@app.route('/page/<uname>')

def mypage(uname):
    return render_template('day1.html',name=uname)

# ---------------------------------------

@app.route('/t/<int:num>')
def mytable(num):
    return render_template('day1.html',n=num,name='mul tbl of')

if __name__=="__main__":
    app.run(debug=True)


