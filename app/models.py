from app import mysql

class studentmodel:
    @classmethod
    def create_student(cls, id, firstname, lastname, course_code, year, gender):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("INSERT INTO student (id, firstname, lastname, course_code, year, gender) VALUES (%s, %s, %s, %s, %s, %s)",
                        (id, firstname, lastname, course_code, year, gender))
            mysql.connection.commit()
            return "Student data added!"
        except Exception as e:
            return f"Adding student failed: {str(e)}"

    @classmethod
    def get_students(cls):
        cur = mysql.new_cursor(dictionary=True)
        cur.execute("SELECT id, firstname, lastname, course_code, year, gender FROM student")
        students = cur.fetchall()
        return students
    
    @classmethod
    def update_student(cls, id, firstname, lastname, course_code, year, gender):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("UPDATE student SET firstname = %s, lastname = %s, course_code = %s, year = %s, gender = %s WHERE id = %s", 
                        (firstname, lastname, course_code, year, gender, id))
            mysql.connection.commit()
            return "Student updated successfully"
        except Exception as e:
            return f"Failed to update student: {str(e)}"
        
    @classmethod
    def search_student(cls, query):
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("""
                SELECT id, firstname, lastname, course_code, gender, year
                FROM student
                WHERE
                    id LIKE %s OR
                    firstname LIKE %s OR
                    lastname LIKE %s OR
                    course_code LIKE %s OR
                    year LIKE %s OR
                    gender LIKE %s;
            """, (f'%{query}%', f'%{query}%', f'%{query}%', f'%{query}%', f'%{query}%', f'%{query}%'))
            students = cur.fetchall()
            return students
    
    @classmethod
    def delete_student(cls, student_id):
        try:
            cur = mysql.new_cursor()
            cur.execute("DELETE FROM student WHERE id = %s", (student_id,))
            mysql.connection.commit()
            if cur.rowcount == 0:
                return "No student with the provided ID found"
            return "Student deleted successfully"
        except Exception as e:
            return f"Failed to delete student: {str(e)}"



        
class collegemodel:
    @classmethod
    def create_college(cls, name, code):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("INSERT INTO college (code, name) VALUES (%s, %s)", (code, name))
            mysql.connection.commit()
            return "College added to data"
        except Exception as e:
            return f"Failed to add college: {str(e)}"

    @classmethod
    def get_colleges(cls):
        cur = mysql.new_cursor(dictionary=True)
        cur.execute("SELECT code, name FROM college")
        colleges = cur.fetchall()
        return colleges
        
    @classmethod
    def update_college(cls, code, new_name):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("UPDATE college SET name = %s WHERE code = %s", (new_name, code))
            mysql.connection.commit()
            return "College updated successfully"
        except Exception as e:
            return f"Failed to update college: {str(e)}"
        
    @classmethod
    def search_college(cls, query):
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("""
                SELECT code, name
                FROM college
                WHERE
                    code LIKE %s OR
                    name LIKE %s;
            """, (f'%{query}%', f'%{query}%'))
            colleges = cur.fetchall()
            return colleges
    
    @classmethod
    def delete_college(cls, college_code):
        try:
            cur = mysql.new_cursor()
            cur.execute("DELETE FROM college WHERE code = %s", (college_code,))
            mysql.connection.commit()
            if cur.rowcount == 0:
                return "No College with the provided Code found"
            return "College deleted successfully"
        except Exception as e:
            return f"Failed to delete college: {str(e)}"

class coursemodel:
    @classmethod
    def create_course(cls, name, code, college_code):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("INSERT INTO course (code, name, college_code) VALUES (%s, %s, %s)", (code, name, college_code))
            mysql.connection.commit()
            return "Course added to data"
        except Exception as e:
            return f"Failed to add course: {str(e)}"
    @classmethod
    def get_courses(cls):
        cur = mysql.new_cursor(dictionary=True)
        cur.execute("SELECT code, name, college_code FROM course")#course.code AS course_code, course.name AS course_name, college.code AS college_code, college.name AS college_name FROM course INNER JOIN college ON course.college_code = college.code")
        courses = cur.fetchall()
        return courses
    
    @classmethod
    def update_course(cls, code, new_name, college_code):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("UPDATE course SET name = %s, college_code = %s WHERE code = %s", (new_name, college_code, code))
            mysql.connection.commit()
            return "Course updated successfully"
        except Exception as e:
            return f"Failed to update course: {str(e)}"
    @classmethod
    def search_course(cls, query):
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("""
                SELECT code, name, college_code
                FROM course
                WHERE
                    code LIKE %s OR
                    name LIKE %s OR
                    college_code LIKE %s;
            """, (f'%{query}%', f'%{query}%', f'%{query}%'))
            courses = cur.fetchall()
            return courses
    
    @classmethod
    def delete_course(cls, course_code):
        try:
            cur = mysql.new_cursor()
            cur.execute("DELETE FROM course WHERE code = %s", (course_code,))
            mysql.connection.commit()
            
            if cur.rowcount > 0:
                return "Course deleted successfully"
            else:
                return "No Course with the provided Code found"
        
        except Exception as e:
            return f"Failed to delete course: {str(e)}"
