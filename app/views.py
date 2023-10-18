from flask import Blueprint, render_template, request, flash

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template("index.html")

@views.route('/students', methods=['GET', 'POST'])
def student():
    if request.method == 'POST':
        data = request.form
        print(data)
    return render_template("student.html")

@views.route('/course', methods=['GET', 'POST'])
def course():
    if request.method == 'POST':
        data2 = request.form
        print(data2)
    return render_template("course.html")

@views.route('/college', methods=['GET', 'POST'])
def college():
    if request.method == 'POST':
        data3 = request.form
        print(data3)
    return render_template("college.html")


@views.route('/editing')
def edit():
    return render_template("edit_student.html")
