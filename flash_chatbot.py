from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Configure MySQL connection
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "chatbot_db"
}

# Function to establish database connection
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Function to query MySQL
def get_response_from_db(user_question):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    # Query to match the question
    query = "SELECT answer FROM faq WHERE question LIKE %s"
    cursor.execute(query, (user_question,))
    result = cursor.fetchone()
    
    cursor.close()
    connection.close()
    
    # Return the answer if found, else a default response
    return result['answer'] if result else "Sorry, I don't understand that question."

# Define chatbot endpoint
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_question = data.get('question')
    
    if not user_question:
        return jsonify({"error": "Question is required"}), 400
    
    # Get the response from the database
    response = get_response_from_db(user_question)
    return jsonify({"answer": response})

# Endpoint to get all FAQs
@app.route('/faqs', methods=['GET'])
def get_faqs():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM faq")
    faqs = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    return jsonify(faqs)

# Endpoint to add a new FAQ
@app.route('/add_faq', methods=['POST'])
def add_faq():
    data = request.json
    question = data.get('question')
    answer = data.get('answer')
    
    if not question or not answer:
        return jsonify({"error": "Both question and answer are required"}), 400
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("INSERT INTO faq (question, answer) VALUES (%s, %s)", (question, answer))
    connection.commit()
    
    cursor.close()
    connection.close()
    
    return jsonify({"message": "FAQ added successfully"}), 201

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
