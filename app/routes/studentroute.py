from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from app.models.studentmodels import studentmodel
from app.models.coursemodels import coursemodel
from werkzeug.utils import secure_filename
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

        image_file = request.files.get('inputImage')
        if image_file:
            # Upload the image to Cloudinary
            upload_result = cloudinary.uploader.upload(image_file)
            image_url = upload_result['secure_url']
        else:
            # If no image is provided, use a default image URL or set to None
            image_url = '/static/css/profile.png'

        result = studentmodel.create_student(id, fname, lname, course, year, gender, image_url)
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

        # Check if the file is an allowed image type
        allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
        if file.filename.split('.')[-1].lower() not in allowed_extensions:
            flash("Invalid file type. Please upload a valid image.", 'error')
            return redirect(url_for('studentroute.view_profile', student_id=student_id))

        # Check if the file size is within the limit (2 MB in this example)
        max_file_size = 2 * 1024 * 1024  # 2 MB
        if len(file.read()) > max_file_size:
            flash(f"File size exceeds the limit of {max_file_size / (1024 * 1024)} MB.", 'error')
            return redirect(url_for('studentroute.view_profile', student_id=student_id))

        # Rewind the file pointer to read it again during upload
        file.seek(0)

        # Secure filename to prevent any malicious activities
        secured_filename = secure_filename(file.filename)

        # Upload the file to Cloudinary
        result = cloudinary.uploader.upload(file, public_id=secured_filename)

        # Access the uploaded image URL
        image_url = result['secure_url']

        # Update the student's image URL in the database
        studentmodel.update_image_url(student_id, image_url)

        flash("Image uploaded successfully.", 'success')

    return redirect(url_for('studentroute.view_profile', student_id=student_id))

