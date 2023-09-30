# Submitted by Ruchita Mahajan (Batch 12)
#TASK -ATM Simulator

import os

def transaction(balance):
    print("\nEnter any option to be served!\n")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Balance\n")
    choice = int(input())

    if (choice == 1):
        print("Please enter amount to withdraw: ")
        amountToWithDraw = int(input())

        if (amountToWithDraw > balance):
            print("There is no insufficient funds in your account")
            print("Do you want another transaction?\nPress 1 to proceed and 2 to exit")
            anotherTransaction = int(input())

            if (anotherTransaction == 1):
                t = os.system("clear")
                transaction(balance)
        else:
            balance -= amountToWithDraw
            print("You have withdrawn ${}.00 and your balance is ${}.00".format(amountToWithDraw, balance))
            print("Do you want another transaction?\nPress 1 to proceed and 2 to exit")
            anotherTransaction = int(input())

            if (anotherTransaction == 1):
                t = os.system("clear")
                transaction(balance)
    
    elif (choice == 2):
        print("Please enter amount to deposit: ")
        amountToDeposit = int(input())

        balance += amountToDeposit

        print("Thank you for depositing, new balance is ${}".format(balance))
        print("Do you want another transaction?\nPress 1 to proceed and 2 to exit")
        anotherTransaction = int(input())

        if (anotherTransaction == 1):
            t = os.system("clear")
            transaction(balance)

    elif(choice == 3):
        print("Your bank account balance is: ${}.00".format(balance))
        print("Do you want another transaction?\nPress 1 to proceed and 2 to exit")
        anotherTransaction = int(input())

        if (anotherTransaction == 1):
            t = os.system("clear")
            transaction(balance)
    
    else:
        t = os.system("clear")
        transaction(balance)


balance = 0
transaction(balance)