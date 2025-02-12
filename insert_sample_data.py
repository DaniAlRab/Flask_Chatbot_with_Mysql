import mysql.connector

def insert_sample_data():
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "",
        "database": "chatbot_db"
    }
    
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    
    # Insert sample data
    sample_data = [
        ("What is your name?", "I am ChatBot, here to help you!"),
        ("How can I reset my password?", "To reset your password, click 'Forgot Password' on the login page.")
    ]
    
    cursor.executemany("INSERT INTO faq (question, answer) VALUES (%s, %s)", sample_data)
    
    connection.commit()
    cursor.close()
    connection.close()
    print("Sample data inserted successfully!")

if __name__ == "__main__":
    insert_sample_data()
