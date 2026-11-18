# this is the simple program to maake a game using python 
import random

items=["rock","paper","scissors"]
move=random.choice(items)
#print(move)


player=input("Enter Your choice:").lower()

if player==move:
    print("Tied!!")

elif (player=="rock" and move=="scissors") or (player=="paper" and move=="rock"):
    print("You Won!!")
    
    
elif player=="scissors" and move=="paper":

    print("You Won!!")

elif (player=="paper" and move=="scissors") or (player=="scissors" and move=="rock"):
    print("You Lost!!") 

elif player=="rock" and move=="paper":
    print("You Lost!!") 

else:
    print("invalid Choice!!")        
