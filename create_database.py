import mysql.connector

def setup_database():
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": ""
    }
    
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    
    # Create database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS chatbot_db")
    cursor.execute("USE chatbot_db")
    
    # Create table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS faq (
        id INT AUTO_INCREMENT PRIMARY KEY,
        question VARCHAR(255),
        answer TEXT
    )
    """)
    
    connection.commit()
    cursor.close()
    connection.close()
    print("Database and table setup completed successfully!")

if __name__ == "__main__":
    setup_database()
