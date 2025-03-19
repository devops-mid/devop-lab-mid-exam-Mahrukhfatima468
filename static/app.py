import re

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    
    email_regex = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
    if not re.match(email_regex, email):
        return jsonify({"error": "Invalid email format!"}), 400

    if not phone.isdigit() or len(phone) != 10:
        return jsonify({"error": "Phone number must be 10 digits."}), 400

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
    conn.commit()
    conn.close()

    return jsonify({"message": "Data saved successfully!"})
