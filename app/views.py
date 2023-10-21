from flask import Blueprint, render_template, request, redirect
from app.models import studentmodel, coursemodel, collegemodel


views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template("index.html")

@views.route('/students', methods=['GET', 'POST'])
def student():
    if request.method == "POST":
        id = request.form.get("inputID")
        fname = request.form.get("inputFirstName")
        lname = request.form.get("inputLastName")
        course = request.form.get("inputCourse")
        year = request.form.get("inputYear")
        gender = request.form.get("inputGender")
        studentmodel.create_student(id, fname, lname, course, year, gender)


    students = studentmodel.get_students()
    courses = coursemodel.get_courses()
    return render_template("student.html", students= students, courses=courses)

@views.route('/course', methods=['GET', 'POST'])
def course():
    if request.method == "POST":
        code = request.form.get("inputCOURSE_CD")
        name = request.form.get("inputCOURSE_NM")
        collegecode = request.form.get("inputCOURSE_CLG")
        coursemodel.create_course(name, code, collegecode)


    colleges = collegemodel.get_colleges()
    courses = coursemodel.get_courses()
    return render_template("course.html", courses=courses, colleges=colleges)

@views.route('/college', methods=['GET', 'POST'])
def college():
    if request.method == "POST":
        code = request.form.get("inputCOLLEGE_CD")
        name = request.form.get("inputCOLLEGE_NM")
        collegemodel.create_college(name, code)

    colleges = collegemodel.get_colleges()
    return render_template("college.html", colleges=colleges)


# @views.route('/editing_stud')
# def edit_student():
#     return render_template("edit_student.html")
# @views.route('/editing_cour')
# def edit_course():
#     return render_template("edit_course.html")
# @views.route('/editing_coll')
# def edit_college():
#     return render_template("edit_college.html")


