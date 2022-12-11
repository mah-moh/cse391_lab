from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
db = SQLAlchemy(app)

class Lab(db.Model):
    __tablename__ = 'lab'
    id = db.Column(db.Integer, primary_key=True)
    slots = db.Column(db.String(80), nullable=False)

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True , unique=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    lab_slot = db.Column(db.Integer, db.ForeignKey('lab.id'), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        lab = Lab.query.all()
        return render_template('index.html', lab=lab)

    if request.method == 'POST':
        name = request.form['name']
        id = request.form['sid']
        email = request.form['email']
        lab_slot = request.form['lab']
        student = Student(id=id, name=name, email=email, lab_slot=lab_slot)
        db.session.add(student)
        db.session.commit()
    return render_template('index.html')


@app.route('/seat', methods=['GET', 'POST'])
def seat():
    if request.method == 'GET':
        lab = Lab.query.all()
        return render_template('seat_status.html', lab=lab)

    if request.method == 'POST':
        lab_slot = request.form['lab']
        students = Student.query.filter_by(lab_slot=lab_slot).all()
        for student in students:
            print(student.id)
    return render_template('seat_status.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)