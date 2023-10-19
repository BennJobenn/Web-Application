from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template("index.html")

@views.route('/students', methods=['GET', 'POST'])
def student():

    return render_template("student.html")

@views.route('/course', methods=['GET', 'POST'])
def course():

    return render_template("course.html")

@views.route('/college', methods=['GET', 'POST'])
def college():

    return render_template("college.html")


@views.route('/editing_stud')
def edit_student():
    return render_template("edit_student.html")
@views.route('/editing_cour')
def edit_course():
    return render_template("edit_course.html")
@views.route('/editing_coll')
def edit_college():
    return render_template("edit_college.html")
