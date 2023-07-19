# this is nested if and elif statements example code

height = float(input("Enter your height in Meter"))
weight = float(input("Enter your weight in kg"))
# body_mass_index = round((80 / 1.75 ** 2), 2)
body_mass_index = round(weight / height ** 2)
# print(type(body_mass_index))
print(f"Your Height: {height}m and Your Weight: {weight}kg")
# print(f'Your body_mass_index:{body_mass_index}')

if body_mass_index < 18.5:  # below 18.5 – you're in the underweight range
    print(f"Your body_mass_index:{body_mass_index},you are underweight.")
elif body_mass_index < 25:  # between 18.5 and 24.9 – you're in the healthy weight range
    print(f"Your body_mass_index:{body_mass_index}, you are healthy weight.")
elif body_mass_index < 30:  # between 25 and 29.9 – you're in the overweight range
    print(f"Your body_mass_index:{body_mass_index}, you are overweight.")
elif body_mass_index < 35:
    print(f"Your body_mass_index:{body_mass_index}, you are obese.")
else:  # 30 or over – you're in the obese range.
    print(f"Your body_mass_index:{body_mass_index}, you are clinically obese.")
