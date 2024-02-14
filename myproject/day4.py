from flask import*
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///anu.db'
app.config['SECRET_KEY']='abc'

db=SQLAlchemy(app)

class Employee(db.Model):
    id=db.Column('employee_id',db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    address=db.Column(db.String(20))

    def __init__(self,name,address):
        self.name=name
        self.address=address


@app.route('/add',methods=['GET','POST'])
def add_emp():
    if request.method=="POST":
        em=Employee(request.form['name'],request.form['add'])
        # return'success'
        db.session.add(em)
        db.session.commit()
        return redirect(url_for('display'))
    else:
        return render_template('add.html')
    


@app.route('/')
def display():
    return render_template('listemp.html',emp=Employee.query.all())

    



if __name__=="__main__":
  with app.app_context():
      db.create_all()
      app.run(debug=True)    

      