import time
import os
from plyer import notification

import tkinter as tk
from tkinter import messagebox, simpledialog


def shutdown_time(duration, break_time):
    while duration > 0:
       print(f"Remaining time: {duration} seconds")
       time.sleep(1)
       duration -= 1

       if duration == break_time:
                 notification.notify(
                    title="You Have Not much time be Hurry",
                    message="Please Save What you have made changes",
                    timeout="10"
                )
    #Shutdown in Provided Specific time
    os.system("shutdown /s /t 1")
#providing the time when we want to shutdown the pc
exam_duration = (0.01*60)
#providiing the notification time when we want to say that they have minimum time and they should save their work
break_time = (60*0.05)
#print("Enter only in Hours\n")
#exam_duration =int(input("Enter the Hours you want to Shutdown your PC \n"))
#total_duration = (exam_duration*60*60)
#print("You have 2 Hours for Your Examination \n And All the Best for your Exam\n and don't worry we will give notification when your have 10 minutes of time ")
#print("Enter the Password \n")
#Password = input("Enter the Password\n")
#if Password == secret:
    # shutdown_time(exam_duration,break_time)
#else:
 #   print(("You have entered the Wrong one !Please Try again later\n"))
def authenticate():
    entered_password = password_entry.get()

    # Replace 'your_correct_password' with the actual correct password
    if entered_password == 'Suhas0110':
        # Code to execute when the password is correct
        print("Authentication Successful!")
        shutdown_time(exam_duration, break_time)
    else:
        # Show error message for incorrect password
        messagebox.showerror("Error", "Incorrect Password")

secret = 'Close_program'
def on_close():
    close_password = simpledialog.askstring("Password", "Enter password to close:")

    # Replace 'your_close_password' with the actual password to close the interface
    if close_password == secret:
        close_password = tk.Entry(root, show="*")
        close_password.pack(pady=10)
        root.destroy()
    else:
        messagebox.showerror("Error", "Incorrect Password")


# Creating the main window
root = tk.Tk()
root.title("Password Protected Interface")

# Adding widgets to the window
password_label = tk.Label(root, text="Enter Password:")
password_label.pack(pady=10)

password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=10)

authenticate_button = tk.Button(root, text="Authenticate", command=authenticate)
authenticate_button.pack(pady=10)

# Bind the window close event to the on_close function
root.protocol("WM_DELETE_WINDOW", on_close)

# Run the main loop
root.mainloop()
root.protocol("WM_DELETE_WINDOW", on_close)