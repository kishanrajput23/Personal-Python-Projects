balance = 1000
print("""
Welcome to ATM Machine

Choose Transaction

1)BALANCE
2)WITHDRAW
3)DEPOSIT
4)EXIT

""")
option = int(input("Enter Transaction "))

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
    exit()
else:
    print("no selected transaction")
