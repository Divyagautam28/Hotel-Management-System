import tkinter as tk
from tkinter import messagebox
from admin_dashboard import AdminDashboard
from user_dashboard import UserDashboard
from db import create_db, check_user_credentials, register_user

create_db()

def register():
    username = entry_username.get()
    password = entry_password.get()
    contact = entry_contact.get()
    
    if username and password and contact:
        try:
            register_user(username, password, contact)
            messagebox.showinfo("Registration Successful", "You can now log in.")
        except Exception as e:
            messagebox.showerror("Error", f"Registration failed: {e}")
    else:
        messagebox.showerror("Error", "Username, password, and contact are required.")

def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if username == "admin" and password == "admin":
        login_window.destroy()
        AdminDashboard().run()
    else:
        user = check_user_credentials(username, password)
        if user:
            login_window.destroy()
            UserDashboard(user[0]).run()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

login_window = tk.Tk()
login_window.title("Hotel Management System - Login")
login_window.geometry("300x300")

tk.Label(login_window, text="Username").pack(pady=5)
entry_username = tk.Entry(login_window)
entry_username.pack(pady=5)

tk.Label(login_window, text="Password").pack(pady=5)
entry_password = tk.Entry(login_window, show="*")
entry_password.pack(pady=5)

tk.Label(login_window, text="Contact (for new users)").pack(pady=5)
entry_contact = tk.Entry(login_window)
entry_contact.pack(pady=5)

tk.Button(login_window, text="Register", command=register).pack(pady=5)
tk.Button(login_window, text="Login", command=login).pack(pady=20)

login_window.mainloop()
