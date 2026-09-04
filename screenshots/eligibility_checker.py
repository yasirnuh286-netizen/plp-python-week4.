age = int(input("Enter your age: "))

# Condition 1: Must be at least 13 to join
# Condition 2: Ages 18+ do not need consent; ages 13-17 require consent
if age >= 18:
    print("Welcome to the club!")
elif age >= 13:
    consent = input("Do you have parental consent? (yes/no): ").strip().lower()
    
    # Using 'and' to verify age threshold along with 'or' to check valid consent inputs
    if (consent == "yes" or consent == "y") and not (age < 13):
        print("Welcome to the club!")
    else:
        print("Sorry, you are not eligible yet.")
else:
    # Under 13 are ineligible regardless of consent
    print("Sorry, you are not eligible yet.")
