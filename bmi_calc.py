import datetime
from tkinter import *

# Calculate BMI function
def calculate_bmi():
    name = name_entry.get()
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    body_mass_index = round(weight / height ** 2, 2)

    if body_mass_index < 18.5:
        final_output.set("Hi {}, your BMI is {:.2f}. You are underweight.".format(name, body_mass_index))
    elif body_mass_index < 24.9:
        final_output.set("Hi {}, your BMI is {:.2f}. You are in the healthy weight range.".format(name, body_mass_index))
    elif body_mass_index < 29.9:
        final_output.set("Hi {}, your BMI is {:.2f}. You are overweight.".format(name, body_mass_index))
    else:
        final_output.set("Hi {}, your BMI is {:.2f}. You are clinically obese.".format(name, body_mass_index))

# Create GUI window
window = Tk()
#window.geometry("400x300")
# window.geometry("1920x1080")  # 4k resolution
window.geometry("1080x720")  # 1080 resolution
window.title("BMI Calculator")

# Labels and Entry widgets for input
name_label = Label(window, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = Entry(window)
name_entry.grid(row=0, column=1, padx=10, pady=5)

height_label = Label(window, text="Height (m):")
height_label.grid(row=1, column=0, padx=10, pady=5)
height_entry = Entry(window)
height_entry.grid(row=1, column=1, padx=10, pady=5)

weight_label = Label(window, text="Weight (kg):")
weight_label.grid(row=2, column=0, padx=10, pady=5)
weight_entry = Entry(window)
weight_entry.grid(row=2, column=1, padx=10, pady=5)

# Button to calculate BMI
calculate_button = Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Label to display output
final_output = StringVar()
output_label = Label(window, textvariable=final_output, font=("Arial", 12))
output_label.grid(row=4, column=0, columnspan=2, pady=5)

# Exit button
exit_button = Button(window, text="Exit", command=window.destroy)
exit_button.grid(row=5, column=0, columnspan=2, pady=10)

window.mainloop()
