balance = 1000

while True:
    print("Choose a transaction:")
    print("1. Balance Money")
    print("2. Withdraw Money")
    print("3. Deposit Balance")
    print("4. Exit")
    
    option = int(input("Enter The Task Transaction (1/2/3/4): "))

    if(option == 1):
        print("Your balance is ", balance)

    elif(option==2):
        withdraw = float(input("Enter amount to withdraw "))
        if(balance > withdraw):
            total = balance - withdraw
            print("success")
            print("your new balance is :",total)
        else:
            print("insufficient Balance")
    
    elif(option==3):
        deposit = float(input("Enter amount to deposit "))
        totalbalance = balance + deposit
        print("success")
        print("total balnace now is: ", totalbalance)
    
    elif(option==4):
        print("thanks for choosing us!")
        break
    
    else:
        print("no selected transaction")