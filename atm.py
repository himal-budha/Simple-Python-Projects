# Simple program in python that shows the normal workflow of ATM System
print("Welcome to the ATM System!!!!")
pin="12345"
balance=40000

pin1=input("Enter the Pin ")

if pin1==pin:

    
 print("Press 1 to show Balance Information")
 print("press 2 to Deposit the amount ")
 print("press 3 to Withdraw amount ")
 print("press 4 to Exit")

 choice=int(input("Enter Your choice:"))

 if choice==1:
    print(f"Your current balance is {balance}")


 elif choice==2:
    print("Welcome Customer")
    amount=int(input("Enter the amount:")) 
    balance+=amount
    print(balance) 

 elif choice==3:
    print('welcome Customer!!') 
    amount1=int(input("Enter the amount:"))

    if amount1<=balance:
        balance-=amount1
        print(f"{balance}")  
    else:
        print("You Entered exceeds amount!!!")  

 else:
   print('Thank You,Visit Again!!!!') 
else:
   print("Wrong Pin!")            


        

