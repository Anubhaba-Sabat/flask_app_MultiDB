from flask import Flask, render_template, url_for, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# SQLAlchemy configuration
app.config['SECRET_KEY'] = "a_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_BINDS'] = {'first_db': 'mysql://root:anubhaba@localhost/sqldatabase',
                                  'second_db': 'postgresql://root:anubhaba@localhost/postgredatabase'}


# Database Initialization
db = SQLAlchemy(app)


# MySQL Model creation
class SQLModel(db.Model):
    __bind_key__ = 'first_db'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item = db.Column(db.String(20), nullable=False)
    itemvalue = db.Column(db.Integer, nullable=False)


# PostgreSQL Model creation
class PSQLModel(db.Model):
    __bind_key__ = 'second_db'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item = db.Column(db.String(20), nullable=False)
    itemvalue = db.Column(db.Integer, nullable=False)


# db.create_all()


@app.route('/')
def home():
    return render_template('index.html', page_name='Home Page')


@app.route('/PostgreSQL')
def postgrepage():
    read_db = PSQLModel.query.all()
    results = [data for data in read_db]
    return render_template('index.html', page_name='PostgreSQL Page', results=results)


@app.route('/MySQL')
def mysqlpage():
    read_db = SQLModel.query.all()
    results = [data for data in read_db]
    return render_template('index.html', page_name='MySQL Page', results=results)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80,debug=True)
