# Simple ATM assignment while using Functions 28-Mar-2019

balance = 50000

def deposit(balance):    #fn for deposit
    d_amount = float(input("Enter Deposit Amount: "))
    # balance = balance + d_amount
    balance += d_amount
    print("Txn Successful, Your updated balance is: " + str(balance))
def withDrawal(balance):   #fn for withdrawal
    w_amount = float(input("Enter Withdrawal Amount: "))
    if w_amount < balance:
        # balance = balance - float(w_amount)
        balance -= w_amount
        print("Txn Successful, Your updated balance is: " + str(balance))
    else:
        print("Sorry you have insufficient balance in your account, txn can't be processed!!")

ans = input("Deposit/ Withdrawal? [d/w]")
if (ans == 'd' or ans == 'D'):
    deposit(balance)
elif (ans == 'w' or ans == 'W'):
    withDrawal(balance)
else:
    print("Invalid option selected...")
