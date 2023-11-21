from flask import Flask, request, redirect, url_for, render_template, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'daydayday'

# Replace the below URI with your actual database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1071@localhost/Pg2Py'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def repr(self):
        return '<User %r>' % self.username

class Grades(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(80), nullable=False)
    assignment = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(200))
    due_date = db.Column(db.Date, nullable=False)
    grade = db.Column(db.String(10), nullable=False)

# Function to create database tables, only needs to be run once
with app.app_context():
    db.create_all()

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get data from form
        username = request.form.get('user')
        email = request.form.get('email')
        password = request.form.get('password')  # In production, ensure this password is hashed

        # Create new User object
        new_user = User(username=username, email=email, password=password)

        # Add to the session and commit to the database
        db.session.add(new_user)
        db.session.commit()

        # Redirect to the login page
        return redirect(url_for('login'))
    return render_template('auth/reg.html')  # Assuming you have a register.html template

# Login route (placeholder)
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        print("gay")

        if user and (user.password == password):
            # Login success
            # Here you can set up the user session
            return redirect(url_for('index'))  # Redirect to main page or dashboard
        else:
            # Login failed
            flash('Invalid email or password')
    return render_template('auth/login.html')

# Main index route
@app.route('/main')
def index():
    return render_template('main/index.html')

@app.route('/courses')
def courses():
    return render_template('main/courses.html')

@app.route('/oq')
def oq():
    return render_template('main/oq.html')

@app.route('/dashboard')
def dashboard():
    return render_template('main/dashboard.html')

@app.route('/grades')
def grades():
    grades_data = Grades.query.all()
    return render_template('main/grades.html', grades=grades_data)

@app.route('/add_grade', methods=['POST'])
def add_grade():
    courses = request.form.getlist('course[]')
    assignments = request.form.getlist('assignment[]')
    descriptions = request.form.getlist('description[]')
    due_dates = request.form.getlist('due_date[]')
    grades = request.form.getlist('grade[]')

    for course, assignment, description, due_date, grade in zip(courses, assignments, descriptions, due_dates, grades):
        new_grade = Grades(course=course, assignment=assignment, description=description, due_date=due_date, grade=grade)
        db.session.add(new_grade)

    db.session.commit()
    return redirect(url_for('grades'))

@app.route('/delete_grade/<int:grade_id>', methods=['POST'])
def delete_grade(grade_id):
    grade_to_delete = Grades.query.get(grade_id)
    if grade_to_delete:
        db.session.delete(grade_to_delete)
        db.session.commit()
    return redirect(url_for('grades'))


if __name__ == '__main__':
    app.run(debug=True)