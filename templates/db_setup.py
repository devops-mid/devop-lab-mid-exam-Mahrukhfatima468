import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Add phone column (if not exists)
cursor.execute("ALTER TABLE users ADD COLUMN phone TEXT")

conn.commit()
conn.close()
print("Database updated successfully!")
