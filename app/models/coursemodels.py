from app import mysql

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
