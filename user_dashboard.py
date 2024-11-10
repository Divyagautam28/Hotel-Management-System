import tkinter as tk
from tkinter import messagebox, simpledialog
from db import get_available_rooms, book_room, check_out_room

class UserDashboard:
    def __init__(self, user_id):
        self.user_id = user_id
        self.window = tk.Tk()
        self.window.title("User Dashboard")
        self.window.geometry("400x500")
        
        tk.Button(self.window, text="View Available Rooms", command=self.view_rooms).pack(pady=10)
        tk.Button(self.window, text="Book Room", command=self.book_room).pack(pady=10)
        tk.Button(self.window, text="Check-Out", command=self.check_out).pack(pady=10)
        tk.Button(self.window, text="Logout", command=self.logout).pack(pady=10)

    def view_rooms(self):
        rooms = get_available_rooms()
        room_info = "\n".join([f"Room {r[1]} - {r[2]} (Amenities: {r[3]}, Price: {r[4]})" for r in rooms])
        messagebox.showinfo("Available Rooms", room_info if room_info else "No rooms available.")
        
    def book_room(self):
        room_id = simpledialog.askinteger("Book Room", "Enter Room ID to book:")
        check_in = simpledialog.askstring("Book Room", "Enter Check-in Date (YYYY-MM-DD):")
        check_out = simpledialog.askstring("Book Room", "Enter Check-out Date (YYYY-MM-DD):")
        
        if room_id and check_in and check_out:
            book_room(self.user_id, room_id, check_in, check_out)
            messagebox.showinfo("Success", "Room booked successfully.")
        else:
            messagebox.showerror("Error", "All fields are required.")
    
    def check_out(self):
        booking_id = simpledialog.askinteger("Check-Out", "Enter Booking ID to check out:")
        
        if booking_id:
            check_out_room(booking_id)
            messagebox.showinfo("Success", f"Checked out booking ID {booking_id}.")
        else:
            messagebox.showerror("Error", "Booking ID required.")

    def logout(self):
        self.window.destroy()
    
    def run(self):
        self.window.mainloop()
