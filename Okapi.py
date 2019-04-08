def okapi():
    Die1= int(raw_input("Enter die roll 1: "))
    Die2= int(raw_input("Enter die roll 2: "))
    Die3= int(raw_input("Enter die roll 3: "))
    
    if Die1 == Die2 and Die2 == Die3:
        print("The payout is $", Die1 + Die2 + Die3,".")
    elif Die1 == Die2:
        print("The payout is $", Die1 + Die2,".")
    elif Die2 == Die3:
        print("The payout is $", Die2 + Die3,".")
    elif Die1 == Die3:
        print("The payout is $", Die1 + Die3,".")
    else:
        print("The payout is $0.")