age = input("How old are you: ")

if age.isdigit():
    age = int(age)
    if age >= 21:
        print("You can enter and drink")
    elif age >= 18:
        print("You can enter but need a wristband")
    else:
        print("You are too young")
else:
    print("Please enter an age!")
