import random

print("Welcome to the Game!!!")

number=random.randint(1,100)
print(number)
guess=int(input("Enter any number: "))

if guess==number:
    print("Congrats, You made it right")


else:
    print("Wrong guess!!")   
    print(f"the correct number was:{number}") 