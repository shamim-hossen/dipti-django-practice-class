# Bkash app
call = int(input("Call 247 for bKash USSD MENU: "))
if call == 247:
    print('''
    bKash
    1.Send Money
    2.Send Money to Non-Bkash User
    3.Mobile Recharge
    4.Payment
    5.Cash Out
    6.Pay Bill
    7.Microfinance
    8.Download Bkash App 
    9.My Bkash
    10.Reset PIN
    ''')

    value = int(input("Choose Any One Option: "))
    #OPTION:1 SEND MONEY
    if value == 1:
        personal_bkash = int(input("Enter Personal Bkash Number: "))
        if personal_bkash:
            amount = int(input("Enter Amount: "))
            if amount:
                pin = int(input("Enter Your Bkash PIN: "))
                if pin:
                    print("Congratulations! Your send money was successfully send to ",str(personal_bkash).zfill(11))
    

    #OPTION:2 SEND MONEY TO NON-BKASH USER
    elif value == 2:
        non_bkash = int(input("Enter Reciver Number: "))
        if non_bkash:
            amount = int(input("Enter Your Amount: "))
            if amount:
                pin = int(input("Enter Your PIN: "))
                if pin:
                    print("Congratulations! You send with prepaid to non-bkash user ",str(non_bkash).zfill(11))
                else:
                    print("YOUR ARE WRONG! PLEASE, TYPE THE CORRECT PASSWORD!")

    #OPTION:3 MOBILE RECHARGE
    elif value == 3:
        print('''
            Choose Your Operator-
            1.Grameenphone
            2.Robi
            3.Banglalink
            4.Airtel
            5.Teletalk 
        ''')
        choose_operators = int(input("Enter Your Operator: "))
        if choose_operators == 1:
            number = int(input("Enter Your Grameenphone Number: "))
            if number:
                amount = int(input("Enter Mobile Recharge Amount: "))
                if amount:
                    pin = int(input("Enter Your Password: "))
                    if pin:
                        print("Successfull Grameenphone Mobile Recharge, Amount is",amount,"Send to",str(number).zfill(11),"Number")

        elif choose_operators == 2:
            number = int(input("Enter Your Robi Number: "))
            if number:
                amount = int(input("Enter Mobile Recharge Amount: "))
                if amount:
                    pin = int(input("Enter Your Password: "))
                    if pin:
                        print("Successfull Robi Mobile Recharge, Amount is",amount,"Send to",str(number).zfill(11),"Number")

        elif choose_operators == 3:
            number = int(input("Enter Your Banglalink Number: "))
            if number:
                amount = int(input("Enter Mobile Recharge Amount: "))
                if amount:
                    pin = int(input("Enter Your Password: "))
                    if pin:
                        print("Successfull Banglalink Mobile Recharge, Amount is",amount,"Send to",str(number).zfill(11),"Number")

        elif choose_operators == 4:
            number = int(input("Enter Your Airtel Number: "))
            if number:
                amount = int(input("Enter Mobile Recharge Amount: "))
                if amount:
                    pin = int(input("Enter Your Password: "))
                    if pin:
                        print("Successfull Airtel Mobile Recharge, Amount is",amount,"Send to",str(number).zfill(11),"Number")

        elif choose_operators == 5:
            number = int(input("Enter Your Teletalk Number: "))
            if number:
                amount = int(input("Enter Mobile Recharge Amount: "))
                if amount:
                    pin = int(input("Enter Your Password: "))
                    if pin:
                        print("Successfull Teletalk Mobile Recharge, Amount is",amount,"Send to",str(number).zfill(11),"Number")
        else:
            print("YOUR ARE WRONG! PLEASE, CHOOSE THE RIGHT OPTION!")

    #OPTION:4 PAYMENT
    elif value == 4:
        merchant_number = int(input("Enter the Merchant bKash Account Number: "))
        if merchant_number:
            amount = int(input("Enter The Amount: "))
            if amount:
                reference = str(input("Enter A Reference: "))
                if reference:
                    counter_number = int(input("Enter The Counter Number: "))
                    if counter_number:
                        pin = int(input("Enter Your bKash PIN: "))
                        if pin:
                            print("Done! You will receive a confirmation message from bKash.")

    #OPTION:5 CASH OUT
    elif value == 5:
        print('''
            1.Cash Out From Agent
            2.Cash Out From ATM
        ''')
        choose = int(input("Choose Your Method: "))
        if choose == 1:
            agent = int(input("Enter Agent bKash Account Number: "))
            if agent:
                amount = int(input("Enter the amount: "))
                if amount:
                    pin = int(input("Enter your bKash Mobile Menu PIN: "))
                    if pin:
                        print("Done! You and the Agent will both receive a confirmation message.")

        elif choose == 2:
            number = int(input("Enter Your Number: "))
            if number:
                pin = int(input("Enter your bKash PIN Number: "))
                if pin:
                    otp = int(input("A security Code (OTP) will be sent to the mobile number. Please enter your OTP with five(5) values: "))
                    if otp:
                        print("Successfully Cash Out From Agent's!")
        else:
            print("YOUR ARE WRONG! PLEASE, CHOOSE THE RIGHT METHOD!")

    #OPTION:6 PAY BILL
    elif value == 6:
        print('''
            1.Electricity Bill
            2.Gas Bill
            3.Telephone Bill
            4.Land Fee
            5.Water Bill
            6.Cable TV Bill
        ''')

        bill = int(input("Choose Your Bill Option: "))
        if bill == 1:
            info = int(input("Enter Account number & necessary information: "))
            if info:
                amount = int(input("Enter Your Electricity Bill: "))
                if amount:
                    pin = int(input("Enter Your Bkash PIN: "))
                    if pin:
                        print("Successfully, Your Electricity Bill was done.")

        elif bill == 2:
            info = int(input("Enter Account number & necessary information: "))
            if info:
                amount = int(input("Enter Your Gas Bill: "))
                if amount:
                    pin = int(input("Enter Your Bkash PIN: "))
                    if pin:
                        print("Successfully, Your Gas Bill was done.")

        elif bill == 3:
            info = int(input("Enter Account number & necessary information: "))
            if info:
                amount = int(input("Enter Your Telephone Bill: "))
                if amount:
                    pin = int(input("Enter Your Bkash PIN: "))
                    if pin:
                        print("Successfully, Your Telephone Bill was done.")

        elif bill == 4:
            info = int(input("Enter Account number & necessary information: "))
            if info:
                amount = int(input("Enter Your Land Fee: "))
                if amount:
                    pin = int(input("Enter Your Bkash PIN: "))
                    if pin:
                        print("Successfully, Your Land Fee was done.")

        elif bill == 5:
            info = int(input("Enter Account number & necessary information: "))
            if info:
                amount = int(input("Enter Your Water Bill: "))
                if amount:
                    pin = int(input("Enter Your Bkash PIN: "))
                    if pin:
                        print("Successfully, Your Water Bill was done.")

        elif bill == 6:
            info = int(input("Enter Account number & necessary information: "))
            if info:
                amount = int(input("Enter Your Cable TV Bill: "))
                if amount:
                    pin = int(input("Enter Your Bkash PIN: "))
                    if pin:
                        print("Successfully, Your Cable TV Bill was done.")

        else:
            print("YOUR ARE WRONG! PLEASE, CHOOSE THE RIGHT METHOD!")


    #OPTION:7 MICROFINANCE
    elif value == 7:
        type = str(input("Enter Your Microfinance Type: "))
        if type:
            amount = int(input("Enter Your Pay Loan Amount: "))
            if amount:
                number = int(input("Enter Your ID or Number: "))
                if number:
                    pin = int(input("Enter Your PIN: "))
                    if pin:
                        print("Successfully, Done Your Microfinance Loan!")

    #OPTION:8 DOWNLOAD BKASH APP
    elif value == 8:
        download = int(input("Download Now to type 1: "))
        if download:
            print("Your download bkash app was downloaded. Have a Good Day!")

    #OPTION:9 MY BKASH
    elif value == 9:
        print('''
            1.Check Balance
            2.Request Statement
            3.Change PIN
            4.Priyo Numbers
            5.History
        ''')

        select = int(input("Choose Your Option: "))
        if select == 1:
            pin = int(input("Enter Your PIN: "))
            if pin:
                print("Your bkash balance was 1000K TK. Now, you can enjoyed with your money.")

        elif select == 2:
            request = int(input("Press 1: "))
            if request:
                print("Successfully send your requeste...")

        elif select == 3:
            present_pin = int(input("Enter Your Current PIN: "))
            if present_pin:
                new_pin = int(input("Enter Your New PIN: "))
                if new_pin:
                    confirm_pin = int(input("Enter Confirm PIN: "))
                    if confirm_pin:
                        print("Your PIN was successfully changed...")

        elif select == 4:
            print('''
                1.01629480966
                2.01806580303
                3.01518912910
                4.01929862944
                5.01727865423
            ''')
            add_number = int(input("You can add priyo number. Type Here: "))
            if add_number:
                print("Successfully add your priyo number!")

        elif select == 5:
            print('''
                This is your Bkash history-

                Bikash is the leading mobile money transfer (MFS) service provider in Bangladesh. It is the largest financial institution in Bangladesh. Bikash was launched to provide financial services to the unbanked.[2][3] Customers dial *247# and use the Bikash app to deposit cash, withdraw cash, send money, add money, remittance, mobile recharge. , payment and billing services etc. [4] To open a Bikash account a customer has to fill the prescribed customer registration form (KYC) with complete details.
            ''')

        else:
            print("YOUR ARE WRONG! PLEASE, CHOOSE THE RIGHT METHOD!")

    #OPTION:9 RESET PIN
    elif value == 10:
        reset_pin = str(input("Do you reset your PIN? Type 'RESET': "))
        if reset_pin == 'RESET':
            print("Successfully reset your PIN... Thank You!")

    else:
        print("YOUR ARE WRONG! PLEASE, CHOOSE THE RIGHT METHOD!")

else:
    print("Error! Please Enter The Right Option...")