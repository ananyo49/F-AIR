import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
from tkinter.font import Font
from PIL import ImageTk,Image
from tkinter import PhotoImage
import mainGUI2 as mg2
import os
import webbrowser
# Function to handle button click
def search_flights():
    from_location = from_var.get()
    to_location = to_var.get()
    date1 = date1_cal.get_date()
    date2 = date2_cal.get_date()
    
    mg2.show_results_page(from_location, to_location, date1, date2, header_frame, content_frame)
    # You can add your code to fetch flight data and display it here

# Create the main tkinter window
root = tk.Tk()
root.title("F[AIR]")


custom_font = Font(family="Avenir", size=12)
def toggle_fullscreen(event=None):
    # Check if the window is already full screen
    if root.attributes('-fullscreen'):
        root.attributes('-fullscreen', False)
    else:
        root.attributes('-fullscreen', True)

# Bind the F11 key to toggle fullscreen mode
root.bind('<F11>', toggle_fullscreen)
root.bind('<Escape>', toggle_fullscreen)  # Bind Escape key to exit fullscreen
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))


# Header Frame
header_frame = tk.Frame(root, pady=10)
header_frame.pack(fill="both")

#Logo (You can replace 'logo.png' with your actual logo file)
#logo = tk.PhotoImage(file='logo.png')
#logo_label = tk.Label(header_frame, image=logo)
#logo_label.grid(row=0, column=0, padx=10)

# Project Name
logo = ImageTk.PhotoImage(Image.open("logo.png").resize((100, 100), Image.Resampling.LANCZOS))
project_name_label = tk.Label(header_frame, image=logo, height=100, width=100)
project_name_label.grid(row=0, column=1, padx=(root.winfo_screenwidth()/2-100, 10))

# Main Content Frame
content_frame = tk.Frame(root, padx=20, pady=20)
content_frame.pack(fill="both")

# Dropdown for 'From' location
from_var = tk.StringVar()
from_label = tk.Label(content_frame, text="From:", font=custom_font)
from_label.grid(row=0, column=0,  padx=(root.winfo_screenwidth()/2-150, 10), pady = (root.winfo_screenheight()/2-200, 10), sticky="w")
from_dropdown = ttk.Combobox(content_frame, textvariable=from_var, foreground="gray")
from_dropdown['values'] = ("ABQ",
"ANC",
"ATL",
"AUS",
"BDL",
"BHM",
"BNA",
"BOS",
"BUF",
"BUR",
"BWI",
"CHS",
"CLE",
"CLT",
"CMH",
"CVG",
"DAL",
"DCA",
"DEN")
from_dropdown.grid(row=0, column=1, padx= 10, pady = (root.winfo_screenheight()/2-200, 10))
# Populate 'From' dropdown with airport data

# Dropdown for 'To' location
to_var = tk.StringVar()
to_label = tk.Label(content_frame, text="To:", font = custom_font)
to_label.grid(row=1, column=0,  padx=(root.winfo_screenwidth()/2-150, 10), sticky="w")
to_dropdown = ttk.Combobox(content_frame, textvariable=to_var, foreground="gray")
to_dropdown['values'] = ("ABQ",
"ANC",
"ATL",
"AUS",
"BDL",
"BHM",
"BNA",
"BOS",
"BUF",
"BUR",
"BWI",
"CHS",
"CLE",
"CLT",
"CMH",
"CVG",
"DAL",
"DCA",
"DEN")
to_dropdown.grid(row=1, column=1,  padx= 10)
# Populate 'To' dropdown with airport data

import datetime
# Function to open calendar for Date 1
def open_calendar_date1():
    date1_cal_popup = tk.Toplevel(root)
    date1_cal_popup.title("Select Date 2")
    date1_cal_popup.geometry("300x250")
    global date1_cal
    date1_cal = Calendar(date1_cal_popup, selectmode="day", year=datetime.date.today().year, month=datetime.date.today().month, day=datetime.date.today().day, date_pattern = "yyyy-mm-dd")
    date1_cal.pack(padx=20, pady=20)
    date1_cal_button = tk.Button(date1_cal_popup, text="OK", command=lambda: update_date1(date1_cal))
    date1_cal_button.pack()

# Function to update Date 1 input field
def update_date1(calendar):
    selected_date = calendar.get_date()
    date1_var.set(selected_date)
    calendar.master.destroy()

# Function to open calendar for Date 2
def open_calendar_date2():
    date2_cal_popup = tk.Toplevel(root)
    date2_cal_popup.title("Select Date 2")
    date2_cal_popup.geometry("300x250")
    global date2_cal
    date2_cal = Calendar(date2_cal_popup, selectmode="day", year=datetime.date.today().year, month=datetime.date.today().month, day=datetime.date.today().day, date_pattern = "yyyy-mm-dd")
    date2_cal.pack(padx=20, pady=20)
    date2_cal_button = tk.Button(date2_cal_popup, text="OK", command=lambda: update_date2(date2_cal))
    date2_cal_button.pack()

# Function to update Date 2 input field
def update_date2(calendar):
    selected_date2 = calendar.get_date()
    date2_var.set(selected_date2)
    calendar.master.destroy()


# Date 1
date1_var = tk.StringVar()
date1_label = tk.Label(content_frame, text="Date 1:", font=custom_font)
date1_label.grid(row=2, column=0,  padx=(root.winfo_screenwidth()/2-150, 10), sticky="w")
date1_entry = tk.Entry(content_frame, textvariable=date1_var)
date1_entry.grid(row=2, column=1, padx=10)

# Calendar button for Date 1
date1_calendar_button = tk.Button(content_frame, text="Calendar", command=open_calendar_date1, font=custom_font)
date1_calendar_button.grid(row=2, column=2, padx=10)

# Date 2
date2_var = tk.StringVar()
date2_label = tk.Label(content_frame, text="Date 2:", font=custom_font)
date2_label.grid(row=3, column=0,  padx=(root.winfo_screenwidth()/2-150, 10), sticky="w")
date2_entry = tk.Entry(content_frame, textvariable=date2_var)
date2_entry.grid(row=3, column=1, padx=10)

# Calendar button for Date 2
date2_calendar_button = tk.Button(content_frame, text="Calendar", command=open_calendar_date2, font=custom_font)
date2_calendar_button.grid(row=3, column=2, padx=10)


# Search Button
search_button = tk.Button(content_frame, text="Search", command=search_flights, font=custom_font)
search_button.grid(row=4, column=0, columnspan=2,  padx=(root.winfo_screenwidth()/2-150, 8))

# Set background color for the main window
root.configure(bg="#eef2f8")

# Set background color for the header frame
header_frame.configure(bg="#3b77dc")

# Set background color for the content frame
content_frame.configure(bg="#eef2f8")

# Set background color for specific widgets
from_label.configure(bg="darkgoldenrod1", fg="black")  # Change text and background color
to_label.configure(bg="darkgoldenrod1", fg="black")
date1_label.configure(bg="darkgoldenrod1", fg="black")
date2_label.configure(bg="darkgoldenrod1", fg="black")

# Set background color for buttons
search_button.configure(bg="green", fg="white")

# You can also set background colors for other widgets as needed

# Run the tkinter main loop
root.mainloop()


