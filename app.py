from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///job_board.db'
db = SQLAlchemy()
db.init_app(app)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    hourly_wage = db.Column(db.Float, nullable=False)
    contact_email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<Job {self.title}>'

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/index')
def job_board():
    jobs = Job.query.all()
    return render_template('index.html', jobs=jobs)

@app.route('/add_job', methods=['POST'])
def add_job():
    title = request.form['title']
    description = request.form['description']
    hourly_wage = request.form['hourly_wage']
    contact_email = request.form['contact_email']

    job = Job(title=title, description=description, hourly_wage=hourly_wage, contact_email=contact_email)
    db.session.add(job)
    db.session.commit()

    return redirect('/index')

@app.route('/jobs')
def jobs():
    jobs = Job.query.all()
    return render_template('jobs.html', jobs=jobs)

@app.route('/job/<int:job_id>')
def job(job_id):
    job = Job.query.get(job_id)
    return render_template('job.html', job=job)

@app.route('/delete_job/<int:job_id>', methods=['POST'])
def delete_job(job_id):
    job = Job.query.get(job_id)
    db.session.delete(job)
    db.session.commit()
    return redirect('/index')

@app.route('/post_job')
def post_job():
    return render_template('post_job.html')





if __name__ == '__main__':
    app.run(debug=True)