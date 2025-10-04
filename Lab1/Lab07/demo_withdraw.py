from withdraw_module import verify_pin, withdraw

# Dữ liệu test
card_no = "1234567890"
pin = input("Enter your PIN: ")

# Kiểm tra PIN
if verify_pin(card_no, pin):
    print("✅ PIN verified.")
    amount = float(input("Enter amount to withdraw: "))
    withdraw(card_no, amount)
else:
    print("❌ Invalid PIN.")
