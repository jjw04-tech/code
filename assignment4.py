try:
    number_input = input("Enter a number: ")
    number = int(number_input)

    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")

print("-" * 30) # Visual separator for terminal clarity

try:
    age_input = input("Enter your age: ")
    age = int(age_input)

    if age >= 18:
        print("You are 18 or older.")
    else:
        print("You are under 18.")
except ValueError:
    print("Invalid input. Please enter a valid integer for age.")

print("-" * 30)

try:
    selection_input = input("Enter a number from 1 to 3: ")
    selection = int(selection_input)

    if selection == 1:
        print("You selected option 1.")
    elif selection == 2:
        print("You selected option 2.")
    elif selection == 3:
        print("You selected option 3.")
    else:
        print("Invalid selection message.")
except ValueError:
    print("Invalid input. Please enter a number.")