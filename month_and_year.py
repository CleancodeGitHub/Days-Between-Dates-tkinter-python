
# #It appears that the ttkbootstrap module is being used to define the style for this project. This module provides additional styling options for tkinter
applications, allowing for a more customized appearance and user experience. It is common to import the Style class from ttkbootstrap in order to apply the desired 
styling to GUI elements in the project.
# 

#==================================
import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

# Create the root window
root = tk.Tk()
root.title("Days Between Dates")
root.eval("tk::PlaceWindow . center")
root.geometry("1000x600")
root.maxsize(1100, 700)
root.configure(bg='#e6ffe6')  # Light green background color

# Create a ttkbootstrap style object
style = Style(theme='minty')

# Global variables for the Entry widgets
entry1 = ttk.Entry(root, style='success.TEntry', font=("Arial", 24, "bold"), justify='center')
entry2 = ttk.Entry(root, style='success.TEntry', font=("Arial", 24, "bold"), justify='center')
entry3 = ttk.Entry(root, style='success.TEntry', font=("Arial", 24, "bold"), justify='center')
entry4 = ttk.Entry(root, style='success.TEntry', font=("Arial", 24, "bold"), justify='center')
entry5 = ttk.Entry(root, style='success.TEntry', font=("Arial", 24, "bold"), justify='center')
entry6 = ttk.Entry(root, style='success.TEntry', font=("Arial", 24, "bold"), justify='center')

# Function to calculate the number of days between two dates
def calculate():
    # Get the input from the entries
    day1, month1, year1 = int(entry1.get()), int(entry2.get()), int(entry3.get())
    day2, month2, year2 = int(entry4.get()), int(entry5.get()), int(entry6.get())

    # Adjusting the counting of months and years
    m1, m2 = (month1 + 9) % 12, (month2 + 9) % 12
    g1, g2 = year1 - m1 // 10, year2 - m2 // 10

    # Calculation of ordinal numbers of days
    n1 = 365 * g1 + g1 // 4 - g1//100 + g1 // 400 + (m1 * 306 + 5) // 10 + day1 - 1
    n2 = 365 * g2 + g2 // 4 - g2//100 + g2 // 400 + (m2 * 306 + 5) // 10 + day2 - 1

    # Calculation of the number of days between two dates
    n = n2 - n1

    # Display the result
    label4.config(text=str(n))

# Create labels for input fields
input_labels = [
    " Day", " Month", " Year",
    " Day", " Month", " Year"
]

# Create input fields and labels
entries = [entry1, entry2, entry3, entry4, entry5, entry6]
for i, (label_text, entry) in enumerate(zip(input_labels, entries)):
    label = ttk.Label(root, text=label_text, font=("Verdana", 26, "normal"))
    label.grid(row=i % 3, column=3*(i // 3), padx=10, pady=10)
    entry.grid(row=i % 3, column=3*(i // 3) + 1, padx=10, pady=10)

# Configure the style for the 'primary.TButton'
style = ttk.Style()
style.configure('primary.TButton', font=('Helvetica', 22, 'bold'), foreground='white', background='blue')

# Create the "Calculate" button with improved style
button = ttk.Button(
    root, text="Calculate",
    command=calculate,
    width=15,
    style='primary.TButton'
)
button.grid(row=3, column=1, columnspan=3, padx=10, pady=10)

# Create label for result
label4 = ttk.Label(
    root,
    text="Days",
    font=("Verdana", 26, "normal"),
    style='success.TLabel'
)
label4.grid(row=3, column=0, padx=10, pady=10)

# Run the application
root.mainloop()
