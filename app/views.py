from flask import Blueprint, render_template, request, redirect, jsonify
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



@views.route("/college/edit/<string:college_code>", methods=["POST"])
def edit_college(college_code):
    new_name = request.form.get("collegeName")
    result = collegemodel.update_college(college_code, new_name)
    return jsonify({'success': result == 'College updated successfully'})

@views.route("/course/edit/<string:course_code>", methods=["POST"])
def edit_course(course_code):
    new_name = request.form.get("courseName")
    college_code = request.form.get("collegeCode")
    result = coursemodel.update_course(course_code, new_name, college_code)
    return jsonify({'success': result == 'Course updated successfully'})

@views.route("/students/edit/<string:student_id>", methods=["POST"])
def edit_student(student_id):
    new_first_name = request.form.get("firstName")
    new_last_name = request.form.get("lastName")
    new_course_code = request.form.get("courseCode")
    new_year = request.form.get("year")
    new_gender = request.form.get("gender")

    result = studentmodel.update_student(student_id, new_first_name, new_last_name, new_course_code, new_year, new_gender)

    return jsonify({'success': result == 'Student updated successfully'})

@views.route('/students/search', methods=['POST'])
def search_students():
    query = request.form.get('query')

    students = studentmodel.search_student(query)

    return jsonify(students)

@views.route('/course/search', methods=['POST'])
def search_course():
    query = request.form.get('query')

    courses = coursemodel.search_course(query)

    return jsonify(courses)