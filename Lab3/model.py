from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/MyBD'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.app_context().push()
db = SQLAlchemy(app)

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    tname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)

    task = db.relationship('Task', backref=db.backref('teachers', lazy=True))

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255))
    code = db.Column(db.String())
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))
    teacher = db.relationship('Teacher', backref=db.backref('tasks', lazy=True))

db.create_all()