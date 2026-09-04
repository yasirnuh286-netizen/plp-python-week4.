# Initial balance and PIN setup
balance = 1000
CORRECT_PIN = "1234"

# Outer decision: Prompt and verify PIN
user_pin = input("Enter your 4-digit PIN: ")

if user_pin == CORRECT_PIN:
    # Inner decision: Prompt for withdrawal amount with input validation
    try:
        withdraw_amount = float(input("Enter amount to withdraw: "))
        
        if withdraw_amount <= 0:
            print("Invalid amount. Withdrawal must be greater than zero.")
        elif withdraw_amount <= balance:
            balance -= withdraw_amount
            print(f"Withdrawal successful. Your new balance is: ${balance:.2f}")
        else:
            print("Insufficient funds")
            
    except ValueError:
        print("Error: Please enter a valid numeric amount.")
else:
    print("Incorrect PIN")
