from flask import Blueprint, render_template, request, jsonify, flash
from app.models.coursemodels import coursemodel
from app.models.collegemodels import collegemodel

courseroute = Blueprint('courseroute', __name__)

@courseroute.route('/course', methods=['GET', 'POST'])
def course():
    if request.method == "POST":
        code = request.form.get("inputCOURSE_CD")
        name = request.form.get("inputCOURSE_NM")
        collegecode = request.form.get("inputCOURSE_CLG")
        result = coursemodel.create_course(name, code, collegecode)
        flash(result)

    colleges = collegemodel.get_colleges()
    courses = coursemodel.get_courses()
    return render_template("course.html", courses=courses, colleges=colleges)

@courseroute.route("/course/edit/<string:course_code>", methods=["POST"])
def edit_course(course_code):
    new_name = request.form.get("courseName")
    college_code = request.form.get("collegeCode")
    result = coursemodel.update_course(course_code, new_name, college_code)
    return jsonify({'success': result == 'Course updated successfully'})

@courseroute.route('/course/search', methods=['POST'])
def search_course():
    query = request.form.get('query')

    courses = coursemodel.search_course(query)

    return jsonify(courses)

@courseroute.route("/course/delete/<string:course_code>", methods=["POST"])
def delete_course(course_code):
    result = coursemodel.delete_course(course_code)

    return jsonify({'success': result == 'Course deleted successfully'})