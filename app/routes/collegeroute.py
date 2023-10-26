from flask import Blueprint, render_template, request, jsonify
from app.models.collegemodels import collegemodel

collegeroute = Blueprint('collegeroute', __name__)

@collegeroute.route('/college', methods=['GET', 'POST'])
def college():
    if request.method == "POST":
        code = request.form.get("inputCOLLEGE_CD")
        name = request.form.get("inputCOLLEGE_NM")
        collegemodel.create_college(name, code)

    colleges = collegemodel.get_colleges()
    return render_template("college.html", colleges=colleges)

@collegeroute.route("/college/edit/<string:college_code>", methods=["POST"])
def edit_college(college_code):
    new_name = request.form.get("collegeName")
    result = collegemodel.update_college(college_code, new_name)
    return jsonify({'success': result == 'College updated successfully'})

@collegeroute.route('/college/search', methods=['POST'])
def search_college():
    query = request.form.get('query')

    colleges = collegemodel.search_college(query)

    return jsonify(colleges)

@collegeroute.route("/college/delete/<string:college_code>", methods=["POST"])
def delete_college(college_code):
    result = collegemodel.delete_college(college_code)

    return jsonify({'success': result == 'College deleted successfully'})