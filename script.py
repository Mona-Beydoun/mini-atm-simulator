print("'''''''''''''''''''''''")
print("Welcome to the ATM")
print("1.Check Balance")
print("2.Deposit Money")
print("3.Withdraw Money")
print("4.Exit")
while True:
    balance=1000
    option =int(input("Choose an option: "))
    if option==1:
        print("Your balance is: " , balance)
    elif option==2:
        op2=int(input("Enter amount to deposit: "))
        print("Deposit successful. New balance = ", balance+op2)
    elif option==3:
        op3=int(input("Enter amount to withdraw: "))
        if op3<balance:
           print("Withdrawal successful. New balance= ",balance-op3)
        elif op3>=balance :
           print("Insufficient funds!")
    
    else:
        print("GoodBye!")
        print("'''''''''''''''''''''''")
        
        break
        
    

