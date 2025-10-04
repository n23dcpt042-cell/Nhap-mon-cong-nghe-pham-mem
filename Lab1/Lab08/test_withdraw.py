from withdraw import verify_pin, withdraw

card_no = input("Nhập số thẻ (card_no): ").strip()
pin = input("Nhập PIN: ").strip()

if verify_pin(card_no, pin):
    amount = input("Nhập số tiền cần rút: ").strip()
    withdraw(card_no, amount)
else:
    print("❌ Sai mã PIN hoặc thẻ không tồn tại.")
