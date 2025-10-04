balance=1000

print("'''''''''''''''''''''''Welcome to the ATM")
print("Your balance is:" , balance , "$")
print("")
print("1.Check Balance")
print("2.Deposit Money")
print("3.Withdraw Money")
print("4.Exit")

while True:
    userInput = input("Choose an option: ")

    if userInput.isdigit():
        option = int(userInput)
        if option == 1:
            print("Your balance is: " , balance, "$")
        elif option == 2:
            op2 = int(input("Enter amount to deposit: "))
            balance += op2
            print("Deposit successful. New balance = ", balance, "$")
        elif option == 3:
            op3 = int(input("Enter amount to withdraw: "))
            if op3 < balance:
                balance -= op3
                print("Withdrawal successful. New balance= ",balance, "$")
            elif op3 >= balance :
                print("Insufficient funds!")
        else:
            print("Goodbye!")
            print("'''''''''''''''''''''''")
            break           
    else:
        print("Insert a digit!")

    

