from flask import Blueprint, render_template, request
from app.models import studentmodel, coursemodel, collegemodel


views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template("index.html")

@views.route('/students', methods=['GET', 'POST'])
def student():
    students = studentmodel.get_students()
    courses = coursemodel.get_courses()
    return render_template("student.html", students= students, courses=courses)

@views.route('/course', methods=['GET', 'POST'])
def course():
    courses = coursemodel.get_courses()
    return render_template("course.html", courses=courses)

@views.route('/college', methods=['GET', 'POST'])
def college():
    colleges = collegemodel.get_colleges()
    return render_template("college.html", colleges=colleges)


@views.route('/editing_stud')
def edit_student():
    return render_template("edit_student.html")
@views.route('/editing_cour')
def edit_course():
    return render_template("edit_course.html")
@views.route('/editing_coll')
def edit_college():
    return render_template("edit_college.html")
