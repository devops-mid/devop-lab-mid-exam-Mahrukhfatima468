from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect("database.db")

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    
    # Save to database
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
    conn.commit()
    conn.close()

    return jsonify({"message": "Data saved successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
