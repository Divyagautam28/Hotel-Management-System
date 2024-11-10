import sqlite3

def create_db():
    conn = sqlite3.connect('hotel_management.db')
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL,
                        contact TEXT
                     )''')

  
    cursor.execute('''CREATE TABLE IF NOT EXISTS rooms (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        room_number TEXT UNIQUE NOT NULL,
                        room_type TEXT NOT NULL,
                        amenities TEXT,
                        price REAL NOT NULL,
                        available INTEGER DEFAULT 1
                     )''')

    
    cursor.execute('''CREATE TABLE IF NOT EXISTS bookings (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        room_id INTEGER,
                        check_in TEXT,
                        check_out TEXT,
                        FOREIGN KEY(user_id) REFERENCES users(id),
                        FOREIGN KEY(room_id) REFERENCES rooms(id)
                     )''')
    conn.commit()
    conn.close()

def register_user(username, password, contact):
    conn = sqlite3.connect('hotel_management.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password, contact) VALUES (?, ?, ?)", (username, password, contact))
    conn.commit()
    conn.close()

def check_user_credentials(username, password):
    conn = sqlite3.connect('hotel_management.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

def add_room(room_number, room_type, amenities, price):
    conn = sqlite3.connect('hotel_management.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO rooms (room_number, room_type, amenities, price) VALUES (?, ?, ?, ?)", 
                   (room_number, room_type, amenities, price))
    conn.commit()
    conn.close()

def update_room_price(room_number, new_price):
    conn = sqlite3.connect('hotel_management.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE rooms SET price = ? WHERE room_number = ?", (new_price, room_number))
    conn.commit()
    conn.close()

def get_available_rooms():
    conn = sqlite3.connect('hotel_management.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, room_number, room_type, amenities, price FROM rooms WHERE available = 1")
    rooms = cursor.fetchall()
    conn.close()
    return rooms

def book_room(user_id, room_id, check_in, check_out):
    conn = sqlite3.connect('hotel_management.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bookings (user_id, room_id, check_in, check_out) VALUES (?, ?, ?, ?)", 
                   (user_id, room_id, check_in, check_out))
    cursor.execute("UPDATE rooms SET available = 0 WHERE id = ?", (room_id,))
    conn.commit()
    conn.close()

def get_booking_details():
    conn = sqlite3.connect('hotel_management.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT b.id, u.username, r.room_number, b.check_in, b.check_out
                      FROM bookings b
                      JOIN users u ON b.user_id = u.id
                      JOIN rooms r ON b.room_id = r.id''')
    bookings = cursor.fetchall()
    conn.close()
    return bookings

def check_out_room(booking_id):
    conn = sqlite3.connect('hotel_management.db')
    cursor = conn.cursor()
    cursor.execute("SELECT room_id FROM bookings WHERE id = ?", (booking_id,))
    room_id = cursor.fetchone()
    if room_id:
        cursor.execute("UPDATE rooms SET available = 1 WHERE id = ?", (room_id[0],))
        cursor.execute("DELETE FROM bookings WHERE id = ?", (booking_id,))
        conn.commit()
    conn.close()
