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



/////////SEARCHING INSIDE STUDENT TABLE/////////
var $searchInput = $('#student_search');
  var $tableBody = $('#student_table');

  // Listen for keyup event in the search input
  $searchInput.on('keyup', function() {
    var query = $searchInput.val();
    performSearch(query);
  });

  // Initial load to display all students
  performSearch('');

  // Function to perform the search and update the table
  function performSearch(query) {
    $.ajax({
      type: 'POST',
      url: '/students/search',
      data: { query: query },
      dataType: 'json',
      success: function(data) {
        // Clear the table
        $tableBody.empty();

        if (data.length > 0) {
          // Populate the table with search results
          data.forEach(function(student) {
            var row = '<tr>';
            row += '<td>' + student.id + '</td>';
            row += '<td>' + student.firstname + '</td>';
            row += '<td>' + student.lastname + '</td>';
            row += '<td>' + student.course_code + '</td>';
            row += '<td>' + student.gender + '</td>';
            row += '<td>' + student.year + '</td>';
            
            row += '<td>';
            row += '<button id="edit_button" name="edit_button" type="button" data-student-id="' + student.id + '"';
            row += ' data-first-name="' + student.firstname + '"';
            row += ' data-last-name="' + student.lastname + '"';
            row += ' data-course-code="' + student.course_code + '"';
            row += ' data-gender="' + student.gender + '"';
            row += ' data-year="' + student.year + '"';
            row += ' data-bs-toggle="modal" data-bs-target="#editStudentModal"';
            row += ' style="margin-right: 20px;" class="btn btn-warning edit-student">Edit</button>';
            row += '<button type="button" class="btn btn-danger" ';
            row += 'onclick="return confirm(\'Delete student data?\')">Delete</button>';
            row += '</td>';

            
            row += '</tr>';
            $tableBody.append(row);
          });
        } else {
          // Display a message when no results are found
          $tableBody.html('<tr><td colspan="6">No results found</td></tr>');
        }
      },
      error: function() {
        console.error('An error occurred during the search.');
      }
    });
  }

  $tableBody.on('click', '.edit-student', function() {
    var studentId = $(this).data('student-id');
    var firstName = $(this).data('first-name');
    var lastName = $(this).data('last-name');
    var courseCode = $(this).data('course-code');
    var gender = $(this).data('gender');
    var year = $(this).data('year');
    
    $("#editStudentID").val(studentId);
    $("#editFirstName").val(firstName);
    $("#editLastName").val(lastName);
    $("#editCourseCode").val(courseCode);
    $("#editYear").val(year);
    $("#editGender").val(gender);
    // Now you can use these variables to populate the edit modal or perform other actions.
  });


  ////COURSE SEARCH TABLE/////
var $courseInput = $('#course_search');
  var $tablecourse = $('#course_table');

  // Listen for keyup event in the search input
  $courseInput.on('keyup', function() {
    var query = $courseInput.val();
    performSearch_course(query);
  });

  // Initial load to display all students
  performSearch_course('');

  // Function to perform the search and update the table
  function performSearch_course(query) {
    $.ajax({
      type: 'POST',
      url: '/course/search',
      data: { query: query },
      dataType: 'json',
      success: function(data) {
        // Clear the table
        $tablecourse.empty();

        if (data.length > 0) {
          // Populate the table with search results
          data.forEach(function(course) {
            var row = '<tr>';
            row += '<td>' + course.code + '</td>';
            row += '<td>' + course.name + '</td>';
            row += '<td>' + course.college_code + '</td>';
            row += '<td>';
            row += '<button id="edit_course" name="edit_course" type="button" style="margin-right: 20px;" class="btn btn-warning edit-course" data-course-code="' + course.code + '"';
            row += 'data-course-name="' + course.name + '"';
            row += 'data-college-code="' + course.college_code + '"';
            row += 'data-bs-toggle="modal" data-bs-target="#editCourseModal" >Edit</button>';
            row += '<button type="button" class="btn btn-danger" ';
            row += 'onclick="return confirm(\'Delete student data?\')">Delete</button>';
            row += '</td>';
            row += '</tr>';
            $tablecourse.append(row);
          });
        } else {
          // Display a message when no results are found
          $tablecourse.html('<tr><td colspan="6">No results found</td></tr>');
        }
      },
      error: function() {
        console.error('An error occurred during the search.');
      }
    });
}
    $tablecourse.on('click', '.edit-student', function() {
        var courseCode = $(this).data("course-code");
        var courseName = $(this).data("course-name");
        var collegeCode = $(this).data("college-code");

        $("#editCourseCode").val(courseCode);
        $("#editCourseName").val(courseName);
        $("#editCollegeCode").val(collegeCode);
        // Now you can use these variables to populate the edit modal or perform other actions.
      });
  
