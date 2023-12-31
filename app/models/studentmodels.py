from app import mysql

class studentmodel:
    @classmethod
    def create_student(cls, id, firstname, lastname, course_code, year, gender, image_url):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("INSERT INTO student (id, firstname, lastname, course_code, year, gender, image_url) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (id, firstname, lastname, course_code, year, gender, image_url))
            mysql.connection.commit()
            return "Student data added!"
        except Exception as e:
            return f"Adding student failed: {str(e)}"

    @classmethod
    def get_students(cls):
        cur = mysql.new_cursor(dictionary=True)
        cur.execute("""
            SELECT student.id, student.image_url, student.firstname, student.lastname, student.course_code, CONCAT(college.name,'(',college.code, ')') AS collegename, student.year, student.gender
            FROM student
            JOIN course ON student.course_code = course.code
            JOIN college ON course.college_code = college.code
        """)
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
                SELECT student.id, student.image_url, student.firstname, student.lastname, student.course_code, CONCAT(college.name,'(',college.code, ')') AS collegename, student.gender, student.year
                FROM student
                JOIN course ON student.course_code = course.code
                JOIN college ON course.college_code = college.code
                WHERE
                    id LIKE %s OR
                    firstname LIKE %s OR
                    lastname LIKE %s OR
                    course_code LIKE %s OR
                    CONCAT(college.name,'(',college.code, ')') LIKE %s OR
                    year LIKE %s OR
                    gender LIKE %s;
            """, (f'%{query}%',f'%{query}%', f'%{query}%', f'%{query}%', f'%{query}%', f'%{query}%', f'%{query}%'))
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
        

    @classmethod
    def get_student_info(cls, student_id):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("SELECT * FROM student WHERE id = %s", (student_id,))
            student = cur.fetchone()

            if student:
                # Process or return the student information
                return student
            else:
                return f"No student found with ID: {student_id}"

        except Exception as e:
            return f"Failed to find student: {str(e)}"
        
    @classmethod
    def get_image_url(cls, student_id):
        cur = mysql.new_cursor(dictionary=True)
        cur.execute("SELECT image_url FROM student WHERE id = %s", (student_id,))
        result = cur.fetchone()
        return result['image_url'] if result else '/static/css/profile.png'
    
    @classmethod
    def update_image_url(cls, student_id, image_url):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("UPDATE student SET image_url = %s WHERE id = %s", (image_url, student_id))
            mysql.connection.commit()
            return "Image URL updated"
        except Exception as e:
            return f"Image URL update failed: {str(e)}"
