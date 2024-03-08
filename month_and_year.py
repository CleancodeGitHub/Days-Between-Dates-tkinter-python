from tkinter import *
from tkinter import ttk

# Create the root window
root = Tk()
root.title("Days Between Dates")
root.eval("tk::PlaceWindow . center")
root.geometry("1000x600")
root.maxsize(1100, 700)
root.configure(bg='#e6ffe6')  # Light green background color

# Create a ttk style object
style = ttk.Style()
style.theme_use('clam')

# Global variables for the Entry widgets
entry1 = Entry(root, bd=5, width=10, font=("Arial", 24, "bold"), justify='center', relief="sunken")
entry2 = Entry(root, bd=5, width=10, font=("Arial", 24, "bold"), justify='center', relief="sunken")
entry3 = Entry(root, bd=5, width=10, font=("Arial", 24, "bold"), justify='center', relief="sunken")
entry4 = Entry(root, bd=5, width=10, font=("Arial", 24, "bold"), justify='center', relief="sunken")
entry5 = Entry(root, bd=5, width=10, font=("Arial", 24, "bold"), justify='center', relief="sunken")
entry6 = Entry(root, bd=5, width=10, font=("Arial", 24, "bold"), justify='center', relief="sunken")

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

# Create the "Calculate" button
button = Button(
    root, text="Calculate",
    width=25,
    height=3,
    bg="blue",
    fg="yellow",
    activebackground="red",
    activeforeground="blue",
    command=calculate
)
button.grid(row=3, column=1, columnspan=3, padx=10, pady=10)

# Create label for result
label4 = Label(
    root,
    text="Days",
    font=("Verdana", 26, "normal"),
    fg="white",
    bg="red",
    relief="flat",
    width=9  # Set width to make it wider
)
label4.grid(row=3, column=0, padx=10, pady=10)

# Run the application
root.mainloop()
