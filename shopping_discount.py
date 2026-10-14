amount = float(input("Enter order amount (₹): "))
membership = input("Are you a member? (yes/no): ").strip().lower()

if amount < 0 or amount > 100000:
    print("Invalid order amount!")
elif membership not in ("yes", "no"):
    print("Invalid membership status! Enter yes or no.")
else:
    if amount >= 5000:
        discount_percent = 15
    elif amount >= 2000 and membership == "yes":
        discount_percent = 10
    else:
        discount_percent = 0

    discount = amount * discount_percent / 100
    payable = amount - discount

    print("\n--- Order Summary ---")
    print(f"Original amount: ₹{amount:.2f}")
    print(f"Discount percentage: {discount_percent}%")
    print(f"Discount amount: ₹{discount:.2f}")
    print(f"Final payable amount: ₹{payable:.2f}")

    if discount_percent > 0:
        print("Eligibility status: Discount eligible")
    else:
        print("Eligibility status: No discount")
