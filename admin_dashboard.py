import tkinter as tk
from tkinter import messagebox, simpledialog
from db import add_room, get_booking_details, check_out_room, update_room_price

class AdminDashboard:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Admin Dashboard")
        self.window.geometry("400x500")
        
        tk.Button(self.window, text="Add Room", command=self.add_room).pack(pady=10)
        tk.Button(self.window, text="View All Bookings", command=self.view_bookings).pack(pady=10)
        tk.Button(self.window, text="Check-Out Guest", command=self.check_out).pack(pady=10)
        tk.Button(self.window, text="Update Room Price", command=self.update_price).pack(pady=10)
        tk.Button(self.window, text="Logout", command=self.logout).pack(pady=10)

    def add_room(self):
        room_number = simpledialog.askstring("Add Room", "Enter Room Number:")
        room_type = simpledialog.askstring("Add Room", "Enter Room Type (e.g., Single, Double):")
        amenities = simpledialog.askstring("Add Room", "Enter Amenities (e.g., TV, WiFi):")
        price = simpledialog.askfloat("Add Room", "Enter Room Price:")
        
        if room_number and room_type and price is not None:
            add_room(room_number, room_type, amenities, price)
            messagebox.showinfo("Success", f"Room {room_number} added successfully.")
        else:
            messagebox.showerror("Error", "All fields are required.")
    
    def view_bookings(self):
        bookings = get_booking_details()
        booking_info = "\n".join([f"Booking ID {b[0]} - Room {b[2]} - User: {b[1]} (Check-in: {b[3]}, Check-out: {b[4]})" for b in bookings])
        messagebox.showinfo("All Bookings", booking_info if booking_info else "No bookings available.")
        
    def check_out(self):
        booking_id = simpledialog.askinteger("Check-Out", "Enter Booking ID to check out:")
        
        if booking_id:
            check_out_room(booking_id)
            messagebox.showinfo("Success", f"Checked out booking ID {booking_id}.")
        else:
            messagebox.showerror("Error", "Booking ID required.")

    def update_price(self):
        room_number = simpledialog.askstring("Update Room Price", "Enter Room Number to update:")
        new_price = simpledialog.askfloat("Update Room Price", "Enter new room price:")
        
        if room_number and new_price:
            update_room_price(room_number, new_price)
            messagebox.showinfo("Success", f"Room {room_number} price updated to {new_price}.")
        else:
            messagebox.showerror("Error", "Room number and new price are required.")

    def logout(self):
        self.window.destroy()
    
    def run(self):
        self.window.mainloop()
