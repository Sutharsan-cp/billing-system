import tkinter as tk
from tkinter import messagebox
import subprocess

    
class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        self.root.configure(bg="#f0f0f0")
        self.employee_records = {"Meena": "0606", "sutharsan": "7373","barath":"2005"}  # Sample employee records
        
        self.login_frame = tk.Frame(self.root, bg="#f0f0f0", bd=5)
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        title_label = tk.Label(self.login_frame, text="Login", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#3b9fe2")
        title_label.grid(row=0, columnspan=2, padx=20, pady=(20, 0))
        
        line_label = tk.Label(self.login_frame, text="===============================", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#3b9fe2")
        line_label.grid(row=1, columnspan=2, padx=20, pady=(0, 20))
        
        self.username_label = tk.Label(self.login_frame, text="Username:", font=("Arial", 14), bg="#f0f0f0", fg="#3b9fe2")
        self.username_label.grid(row=2, column=0, padx=20, pady=10, sticky="e")
        self.username_entry = tk.Entry(self.login_frame, font=("Arial", 14))
        self.username_entry.grid(row=2, column=1, padx=20, pady=10)
        
        self.password_label = tk.Label(self.login_frame, text="Password:", font=("Arial", 14), bg="#f0f0f0", fg="#3b9fe2")
        self.password_label.grid(row=3, column=0, padx=20, pady=10, sticky="e")
        self.password_entry = tk.Entry(self.login_frame, font=("Arial", 14), show="*")
        self.password_entry.grid(row=3, column=1, padx=20, pady=10)
        
        self.login_button = tk.Button(self.login_frame, text="Login", font=("Arial", 14), bg="#3b9fe2", fg="white", command=self.login)
        self.login_button.grid(row=4, columnspan=2, pady=20)
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username in self.employee_records and self.employee_records[username] == password:
            messagebox.showinfo("Success", f"Welcome, {username}!")
            self.launch_billingSystem()
            
        else:
            messagebox.showerror("Error", "Invalid username or password")
    def launch_billingSystem(self):
        command=['Python','billing_system.py']
        subprocess.run(command,check=True,stderr=subprocess.PIPE)
  
root = tk.Tk()
app = LoginSystem(root)
root.mainloop()
