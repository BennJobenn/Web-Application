from app import mysql

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