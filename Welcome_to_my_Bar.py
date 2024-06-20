print("Welcome to the bar!")
age = int(input("What is your age? "))

if age >= 21:
    print("You are allowed to enter the bar.")
    print("We serve the following drinks:")
    print("1. Whisky ($5)")
    print("2. Beer ($7)")
    print("3. Wine ($30)")

    drink_choice = int(input("What would you like to drink? Enter the number (1, 2, or 3): "))
    
    bill = 0
    if drink_choice == 1:
        bill = 5
        print("You chose Whisky. That will be $5.")
    elif drink_choice == 2:
        bill = 7
        print("You chose Beer. That will be $7.")
    elif drink_choice == 3:
        bill = 30
        print("You chose Wine. That will be $30.")
    else:
        print("Invalid choice. Please choose a valid drink next time.")

    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you must be 21 or older to enter the bar.")