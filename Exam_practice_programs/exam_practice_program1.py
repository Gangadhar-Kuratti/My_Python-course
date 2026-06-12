# Program for ATM Withdrawal Operation Using Exception Handling.

try :
    balance=10000
    
    withdrawal_amount=int(input("Enter amount: "))
    
    if withdrawal_amount>balance:
        raise Exception("Insufficient balance")
    balance = balance - withdrawal_amount
    
    print("Withdrawan successfully")
    print("Remaining Balance is: ",balance)
    
except ValueError:
    print("Enter numbers only")
    
except Exception as e:
    print(e)
