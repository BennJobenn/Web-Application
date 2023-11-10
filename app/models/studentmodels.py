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
        cur.execute("""
            SELECT student.id, student.firstname, student.lastname, student.course_code, CONCAT(college.name,'(',college.code, ')') AS collegename, student.year, student.gender
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
                SELECT student.id, student.firstname, student.lastname, student.course_code, CONCAT(college.name,'(',college.code, ')') AS collegename, student.gender, student.year
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
