balance = 1000
CORRECT_PIN = "1234"

user_pin = input("Enter your 4-digit PIN: ")

if user_pin == CORRECT_PIN:
    withdraw_amount = float(input("Enter amount to withdraw: "))
    
    if withdraw_amount <= balance:
        balance -= withdraw_amount
        print(f"Withdrawal successful. Your new balance is: ${balance:.2f}")
    else:
        print("Insufficient funds")
else:
    print("Incorrect PIN")
