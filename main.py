user = {"Name": "Disha","PIN": 54321,"Balance": 5000}

def deposit():
    amount=int(input("Enter amount to deposit:"))
    if amount > 0:
        user["Balance"]=amount+user["Balance"]
        print("Deposit successful")
        print("The amount deposited is",amount)

def withdraw():
    amount = int(input("Enter amount to withdraw:"))
    if amount > user["Balance"]:
        print("Insufficient balance")
    elif amount > 0:
        user["Balance"]=user["Balance"]-amount
        print("The amount witdrawn is",amount)

def check_balance():
    print("Balance:",user["Balance"])

PIN=int(input("Enter PIN: "))
if PIN!=user["PIN"]:
    print("Invalid PIN")
else:
    while True:
        print("\n1.Check Balance\t2.Deposit\t3.Withdraw\t4.Exit\n")
        choice=int(input("Choose: "))

        if choice==1:
            check_balance()
        elif choice==2:
            deposit()
        elif choice==3:
            withdraw()
        elif choice==4:
            break
        else:
            print("Invalid choice")
