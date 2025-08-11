import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="dev-rds-ecs.c72kki2285tf.ap-south-1.rds.amazonaws.com", # change to your host
            user="devdbuser",     # your DB username
            password="devdbpass-admin321", # your DB password
            database="crm"  # your DB name
        )
        self.cursor = self.conn.cursor(dictionary=True)
        print("Connected to DB")
    
    def get_Top_student_rank(self,section_id):
        querry = f"""SELECT s.id, s.name, COUNT(q.id) AS correct_answers
        FROM student s
        JOIN quiz_rooms_student_answer_submissions q ON s.id = q.student_id
        WHERE q.is_correct_answer = 1 AND s.section_id = {section_id}
        GROUP BY s.id, s.name
        HAVING COUNT(q.id) = (
        SELECT MAX(correct_count)
        FROM (
        SELECT COUNT(q2.id) AS correct_count
        FROM student s2
        JOIN quiz_rooms_student_answer_submissions q2 ON s2.id = q2.student_id
        WHERE q2.is_correct_answer = 1 AND s2.section_id = {section_id}
        GROUP BY s2.id
        ) AS counts
    );"""
        self.cursor.execute(querry)
        return self.cursor.fetchall()
    
    def get_freash_lead_numbers(self):
        querry = "SELECT phone FROM leads WHERE lead_stage IS NULL"
        self.cursor.execute(querry)
        result = self.cursor.fetchall()
        return result


    def close_connection(self):
        self.cursor.close()
        self.conn.close()
        print("Connection closed")