# Simple ATM Project using match case in python.
balance = int(input("Enter your balance here: "))
mainPin = int(input("Create your account PIN: "))
lastWithdrawAmount = 0
listOfAmount = []
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
            pin = int(input("Enter your account PIN: "))
            if pin == mainPin:
                print("Balance is : ", balance)
            else:
                print("You have entered wrong password.")

        case 2:
            withdrawAmount = int(input("Enter withdraw amount : "))
            pin = int(input("Enter your account PIN: "))
            if pin == mainPin:
                if withdrawAmount > 10000:
                    print("Please enter amount lesser then 10000.")
                else:
                    if withdrawAmount < balance:
                        print("%d is withdraw successfully." % withdrawAmount)
                        balance -= withdrawAmount
                        lastWithdrawAmount = withdrawAmount
                        listOfAmount.append(withdrawAmount)

                    else:
                        print("Your account balance is low.")
                        print("Current balance is : ", balance)
            else:
                print("You have entered wrong password.")

        case 3:
            depositAmount = int(input("Enter your deposit amount : "))
            balance += depositAmount
            print("%d Amount is deposited successfully. in your account" % depositAmount)

        case 4:
            pin = int(input("Enter your account PIN: "))
            if pin == mainPin:
                if lastWithdrawAmount == 0:
                    print("There is no last transaction in your account.")
                else:
                    # print("last withdraw amount is : ", lastWithdrawAmount)
                    listOfAmount.reverse()
                    i = 1
                    for money in listOfAmount[0:5]:
                        print(i, "-> last withdraw amount is : ", money)
                        i += 1
                    listOfAmount.reverse()
            else:
                print("You have entered wrong password.")

        case 5:
            exit()

        case _:
            print("You have entered invalid option. so please try again.")