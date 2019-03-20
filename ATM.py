# Simple ATM assignment wihtout using loop - 19Mar2019

balance = 50000

ans = input("Deposit/ Withdrawal? [d/w]")
if (ans == 'd' or ans == 'D'):
    d_amount = float(input("Enter Deposit Amount: "))
    balance = balance + d_amount
    print("Txn Successful, Your updated balance is: " + str(balance))
elif (ans == 'w' or ans == 'W'):
    w_amount = float(input("Enter Withdrawal Amount: "))
    if w_amount < balance:
        balance = balance - float(w_amount)
        print("Txn Successful, Your updated balance is: " + str(balance))
    else:
        print("Sorry you have insufficient balance in your account, txn can't be processed!!")
else:
    print("Invalid option selected...")
