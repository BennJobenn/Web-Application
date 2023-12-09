from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from app.models.studentmodels import studentmodel
from app.models.coursemodels import coursemodel
import cloudinary.uploader

studentroute = Blueprint('studentroute', __name__)

@studentroute.route('/')
def index():
    return render_template("index.html")

@studentroute.route('/students', methods=['GET', 'POST'])
def student():
    if request.method == "POST":
        id = request.form.get("inputID")
        fname = request.form.get("inputFirstName")
        lname = request.form.get("inputLastName")
        course = request.form.get("inputCourse")
        year = request.form.get("inputYear")
        gender = request.form.get("inputGender")
        result = studentmodel.create_student(id, fname, lname, course, year, gender)
        flash(result)

    students = studentmodel.get_students()
    courses = coursemodel.get_courses()
    return render_template("student.html", students=students, courses=courses)



@studentroute.route("/students/edit/<string:student_id>", methods=["POST"])
def edit_student(student_id):
    new_first_name = request.form.get("firstName")
    new_last_name = request.form.get("lastName")
    new_course_code = request.form.get("courseCode")
    new_year = request.form.get("year")
    new_gender = request.form.get("gender")

    result = studentmodel.update_student(student_id, new_first_name, new_last_name, new_course_code, new_year, new_gender)

    return jsonify({'success': result == 'Student updated successfully'})

@studentroute.route('/students/search', methods=['POST'])
def search_students():
    query = request.form.get('query')

    students = studentmodel.search_student(query)

    return jsonify(students)

@studentroute.route("/students/delete/<string:student_id>", methods=["POST"])
def delete_student(student_id):
    result = studentmodel.delete_student(student_id)

    return jsonify({'success': result == 'Student deleted successfully'})



@studentroute.route("/profile/<string:student_id>")
def view_profile(student_id):

    student_profile = studentmodel.get_student_info(student_id)

    student_image_url = studentmodel.get_image_url(student_id)

    return render_template("profile.html", student_profile=student_profile, student_image_url=student_image_url)

@studentroute.route('/upload_image/<string:student_id>', methods=['POST'])
def upload_image(student_id):
    if request.method == 'POST':
        file = request.files['file']

        # Upload the file to Cloudinary
        result = cloudinary.uploader.upload(file)

        # Access the uploaded image URL
        image_url = result['secure_url']

        # Update the student's image URL in the database
        studentmodel.update_image_url(student_id, image_url)

    return redirect(url_for('studentroute.view_profile', student_id=student_id))
