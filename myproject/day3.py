from flask import*
import sqlite3
app=Flask(__name__)


@app.route('/')
def index():
    return render_template('emp_reg.html')


@app.route('/save',methods=['POST'])
def emp_save():
    if request.method=="POST":
        name=request.form['fname']
        email=request.form['email']
        ph=request.form['Phone']

        with sqlite3.connect("emp.db") as con:
            mycursor=con.cursor()
            mycursor.execute(''' 
            insert into Employee (name,email,phone) values (?,?,?)''',
            (name,email,ph))
            con.commit()

    return 'success'



@app.route('/List')
def emp_list():
    con=sqlite3.connect('emp.db')
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("select * from Employee")
    rows=cur.fetchall()
    return render_template('emplist.html',data=rows)


@app.route('/empdel/<int:id>')
def emp_del(id):
    print(id)
    con=sqlite3.connect('emp.db')
    cur=con.cursor()
    cur.execute('delete from Employee where id=?',(id,))
    con.commit()
    return 'successfully deleted'


@app.route('/empedit/<int:id>')
def emp_edit(id):
    print(id)
    con=sqlite3.connect('emp.db')
    cur=con.cursor()
    cur.execute(" select * from Employee where id=?",(id,))
    em=cur.fetchone()
    print(em)
    return render_template('emp_edit.html',data=em)


@app.route('/empupdate/<int:id>',methods=['POST'])
def emp_update(id):
      if request.method=="POST":
        name=request.form['fname']
        email=request.form['email']
        ph=request.form['Phone']

        with sqlite3.connect("emp.db") as con:
            mycursor=con.cursor()
            mycursor.execute('update Employee set name=?,email=?,phone=? where id=?',(name,email,ph,id))
            con.commit()
            return 'successfully update'













if __name__=="__main__":
    app.run(debug=True)       
