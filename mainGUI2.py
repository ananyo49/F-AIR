import tkinter as tk
from tkinter import ttk
from scrape import *
import pandas as pd
# Function to navigate to the second page
def show_results_page(fromL, toL, d1, d2, hFrame, cFrame):
    # Remove the content of the first page
    hFrame.destroy()
    cFrame.destroy()
    # Create the main tkinter window
    root = tk.Tk()
    root.title("Flight Price Finder")


    # Create the header for the second page
    header_frame_results = tk.Frame(root, pady=10, bg="blue")
    header_frame_results.pack(fill="both")

    # Logo and Project Name (same as the first page)
    logo_label = tk.Label(header_frame_results, bg="blue")
    logo_label.grid(row=0, column=0, padx=10)

    project_name_label = tk.Label(header_frame_results, text="Flight Price Finder", font=("Helvetica", 16), bg="blue", fg="white")
    project_name_label.grid(row=0, column=1, padx=10)

    about_link = tk.Label(header_frame_results, text="About", cursor="hand2", bg="blue", fg="white")
    about_link.grid(row=0, column=2, padx=10)
    # You can add a function to handle the 'About' link click event here

    # Main Content Frame for the results
    content_frame_results = tk.Frame(root, padx=20, pady=20)
    content_frame_results.pack(fill="both")

    # Heading for the list
    heading_label = tk.Label(content_frame_results, text="CHEAPEST FARES FOR YOUR ROUTE:", font=("Helvetica", 14))
    heading_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

    # Create a list (for demonstration, you can replace this with actual data from your backend)


    # Add subheadings for "Name" and "Price"
    name_label = tk.Label(content_frame_results, text="Name", font=("Helvetica", 12, "bold"))
    name_label.grid(row=1, column=0, padx=10, sticky="w")

    price_label = tk.Label(content_frame_results, text="Price", font=("Helvetica", 12, "bold"))
    price_label.grid(row=1, column=1, padx=10, sticky="w")
    result = Scrape(fromL, toL, d1)
    ScrapeObjects(result)
    x = result.data["Airline(s)"]
    y = result.data["Price ($)"]
    # Display the fare data in a list format
    
    for i in range(10):
        name_label = tk.Label(content_frame_results, text=x[i])
        name_label.grid(row=i + 2, column=0, padx=10, sticky="w")

        price_label = tk.Label(content_frame_results, text=y[i])
        price_label.grid(row=i + 2, column=1, padx=10, sticky="w")
    
    # Run the tkinter main loop
    root.mainloop()

