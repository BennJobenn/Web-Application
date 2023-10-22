$(document).ready(function() {

    

    // Listen for the "Edit" button click for colleges
    const editButtonsCollege = document.querySelectorAll('.edit-college');
    editButtonsCollege.forEach(button => {
        button.addEventListener('click', () => {
            const collegeCode = button.getAttribute('data-college-code');
            const collegeName = button.getAttribute('data-college-name');

            // Populate the edit form fields
            const editCollegeCodeField = document.getElementById('editCollegeCode');
            const editCollegeNameField = document.getElementById('editCollegeName');
            editCollegeCodeField.value = collegeCode;
            editCollegeNameField.value = collegeName;
        });
    });

    const editButtonsCourse = document.querySelectorAll('.edit-course');
    editButtonsCourse.forEach(button => {
        button.addEventListener('click', () => {
            const courseCode = button.getAttribute('data-course-code');
            const courseName = button.getAttribute('data-course-name');
            const collegeCode = button.getAttribute('data-college-code');

            // Populate the edit form fields
            const editCourseCodeField = document.getElementById('editCourseCode');
            const editCourseNameField = document.getElementById('editCourseName');
            const editCollegeCodeField = document.getElementById('editCollegeCode');
            editCourseCodeField.value = courseCode;
            editCourseNameField.value = courseName;
            editCollegeCodeField.value = collegeCode;
        });
    });

    const editButtonsStudent = document.querySelectorAll('.edit-student');
    editButtonsStudent.forEach(button => {
        button.addEventListener('click', () => {
            const studentID = button.getAttribute('data-student-id');
            const firstName = button.getAttribute('data-first-name');
            const lastName = button.getAttribute('data-last-name');
            const courseCode = button.getAttribute('data-course-code');
            const year = button.getAttribute('data-year');
            const gender = button.getAttribute('data-gender');

            // Populate the edit form fields
            const editStudentIDField = document.getElementById('editStudentID');
            const editFirstNameField = document.getElementById('editFirstName');
            const editLastNameField = document.getElementById('editLastName');
            const editCourseField = document.getElementById('editCourse');
            const editYearField = document.getElementById('editYear');
            const editGenderField = document.getElementById('editGender');

            editStudentIDField.value = studentID;
            editFirstNameField.value = firstName;
            editLastNameField.value = lastName;
            editCourseField.value = courseCode;
            editYearField.value = year;
            editGenderField.value = gender;
        });
    });



    ////// EDIT //////

    $(".edit-college").click(function () {
        var collegeCode = $(this).data("college-code");
        var collegeName = $(this).data("college-name");

        $("#editCollegeCode").val(collegeCode);
        $("#editCollegeName").val(collegeName);
    });

    $("#editCollegeForm").submit(function (e) {
        e.preventDefault();
        var collegeCode = $("#editCollegeCode").val();
        var newCollegeName = $("#editCollegeName").val();

        $.ajax({
            type: "POST",
            url: `/college/edit/${collegeCode}`,
            data: {
                collegeName: newCollegeName,
            },
            success: function (response) {
                if (response.success) {
                    alert("College updated successfully");
                    window.location.reload();
                } else {
                    alert("Failed to update college");
                }
            },
        });
    });
    
  });

  $(".edit-course").click(function () {
    var courseCode = $(this).data("course-code");
    var courseName = $(this).data("course-name");
    var collegeCode = $(this).data("college-code");

    $("#editCourseCode").val(courseCode);
    $("#editCourseName").val(courseName);
    $("#editCollegeCode").val(collegeCode);
});

$("#editCourseForm").submit(function (e) {
    e.preventDefault();
    var courseCode = $("#editCourseCode").val();
    var newCourseName = $("#editCourseName").val();
    var collegeCode = $("#editCollegeCode").val(); 

    $.ajax({
        type: "POST",
        url: `/course/edit/${courseCode}`,
        data: {
            courseName: newCourseName,
            collegeCode: collegeCode, 
        },
        success: function (response) {
            if (response.success) {
                alert("Course updated successfully");
                window.location.reload();
            } else {
                alert("Failed to update course");
            }
        },
    });
});

$(".edit-student").click(function () {
    var studentId = $(this).data("student-id");
    var firstName = $(this).data("first-name");
    var lastName = $(this).data("last-name");
    var courseCode = $(this).data("course-code");
    var gender = $(this).data("gender");
    var year = $(this).data("year");

    $("#editStudentID").val(studentId);
    $("#editFirstName").val(firstName);
    $("#editLastName").val(lastName);
    $("#editCourseCode").val(courseCode);
    $("#editYear").val(year);
    $("#editGender").val(gender);
});

$("#editStudentForm").submit(function (e) {
    e.preventDefault();
    var studentId = $("#editStudentID").val();
    var newFirstName = $("#editFirstName").val();
    var newLastName = $("#editLastName").val();
    var newCourseCode = $("#editCourseCode").val();
    var newYear = $("#editYear").val();
    var newGender = $("#editGender").val();

    $.ajax({
        type: "POST",
        url: `/students/edit/${studentId}`,
        data: {
            firstName: newFirstName,
            lastName: newLastName,
            courseCode: newCourseCode,
            gender: newGender,
            year: newYear
        },
        success: function (response) {
            if (response.success) {
                alert("Student updated successfully");
                window.location.reload();
            } else {
                alert("Failed to update student");
            }
        },
    });
});