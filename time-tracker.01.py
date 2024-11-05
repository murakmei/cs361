#This system is used when a user want to track people's check in and out information for the person's name and time
from tkinter import *
from tkinter.ttk import *
from time import strftime

# Creating tkinter window
root = Tk()
root.title('Clock')

# display the current time
def time():
    current_time = strftime('%H:%M %p')
    lbl.config(text=current_time)
    lbl.after(1000, time)

# check in function
def check_in():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    check_in_time = strftime('%H:%M %p')
    check_in_label.config(text=f"{first_name} {last_name} - Check in: {check_in_time}")
    # Clear the label after 3 seconds
    root.after(3000, lambda: check_in_label.config(text=''))
    # Clear the entry fields
    first_name_entry.delete(0, END)
    last_name_entry.delete(0, END)

# check out function
def check_out():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    check_out_time = strftime('%H:%M %p')
    check_out_label.config(text=f"{first_name} {last_name} - Check out: {check_out_time}")
    # clear the label after 3 seconds
    root.after(3000, lambda: check_out_label.config(text=''))
    # clear the entry fields
    first_name_entry.delete(0, END)
    last_name_entry.delete(0, END)

# styling the clock
lbl = Label(root, font=('calibri', 40, 'bold'),
            background='gray', foreground='white')
lbl.pack(anchor='center')

# labels for first name and last name text boxes
Label(root, text="First Name:", font=('calibri', 14)).pack(pady=5)
first_name_entry = Entry(root, font=('calibri', 14))
first_name_entry.pack(pady=5)

Label(root, text="Last Name:", font=('calibri', 14)).pack(pady=5)
last_name_entry = Entry(root, font=('calibri', 14))
last_name_entry.pack(pady=5)

# label to display check-in and check-out times
check_in_label = Label(root, font=('calibri', 16), foreground='white')
check_in_label.pack(anchor='center', pady=10)
check_out_label = Label(root, font=('calibri', 16), foreground='white')
check_out_label.pack(anchor='center', pady=10)

# check-in and check-out buttons
check_in_button = Button(root, text="Check In", command=check_in)
check_in_button.pack(side=LEFT, padx=20, pady=20)

check_out_button = Button(root, text="Check Out", command=check_out)
check_out_button.pack(side=RIGHT, padx=20, pady=20)

# Start the clock
time()

# Run the Tkinter main loop
mainloop()
