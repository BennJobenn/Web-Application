from app import mysql

class studentmodel:

    @classmethod
    def get_students(cls):
        cur = mysql.new_cursor(dictionary=True)
        cur.execute("SELECT id, firstname, lastname, course_code, year, gender FROM student")
        students = cur.fetchall()
        return students
        
class collegemodel:
    @classmethod
    def create_college(cls, name, code):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("INSERT INTO college (code, name) VALUES (%s, %s)", (code, name))
            mysql.connection.commit()
            return "College created successfully"
        except Exception as e:
            return f"Failed to create college: {str(e)}"

    @classmethod
    def get_colleges(cls):
        cur = mysql.new_cursor(dictionary=True)
        cur.execute("SELECT code, name FROM college")
        colleges = cur.fetchall()
        return colleges

class coursemodel:
    @classmethod
    def create_course(cls, name, code, college_code):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("INSERT INTO course (code, name, college_code) VALUES (%s, %s, %s)", (code, name, college_code))
            mysql.connection.commit()
            return "Course created successfully"
        except Exception as e:
            return f"Failed to create course: {str(e)}"
    @classmethod
    def get_courses(cls):
        cur = mysql.new_cursor(dictionary=True)
        cur.execute("SELECT code, name, college_code FROM course")#course.code AS course_code, course.name AS course_name, college.code AS college_code, college.name AS college_name FROM course INNER JOIN college ON course.college_code = college.code")
        courses = cur.fetchall()
        return courses