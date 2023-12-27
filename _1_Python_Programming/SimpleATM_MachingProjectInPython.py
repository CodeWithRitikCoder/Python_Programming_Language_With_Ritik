# Simple ATM Project using match case in python.
balance = int(input("Enter your balance here : "))
lastWithdrawAmount = 0
while 1:
    print("\n")
    print("1-> for Balance Enquiry.")
    print("2-> for Withdraw Amount.")
    print("3-> for Deposit.")
    print("4-> for Mini statement.")
    print("5-> for Exit.")

    option = int(input("Enter your choice here : "))

    match option:
        case 1:
            print("Balance is : ", balance)

        case 2:
            withdrawAmount = int(input("Enter withdraw amount : "))
            if withdrawAmount >= 10000:
                print("Please enter amount lesser then 10000.")
            else:
                if withdrawAmount < balance:
                    print("%d is withdraw successfully." % withdrawAmount)
                    balance -= withdrawAmount
                    lastWithdrawAmount = withdrawAmount
                else:
                    print("Your account balance is low.")
                    print("Current balance is : ", balance)

        case 3:
            depositAmount = int(input("Enter your deposit amount : "))
            balance += depositAmount
            print("%d Amount is deposited successfully. in your account" % depositAmount)

        case 4:
            if lastWithdrawAmount == 0:
                print("There is no last transaction in your account.")
            else:
                print("last withdraw amount is : ", lastWithdrawAmount)

        case 5:
            exit()

        case _:
            print("You have entered invalid option. so please try again.")