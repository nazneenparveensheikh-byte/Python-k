print("Program 4")
age = int(input("Enter age: "))
if age < 0 or age > 120:
    print("Age is not valid")
elif age >= 18:
    print("Age is valid. Eligible for voting")
else:
    print("Age is valid. Not eligible for voting")
