import mysql.connector
import hashlib

# ✅ Hàm kiểm tra PIN
def verify_pin(card_no, pin):
    conn = mysql.connector.connect(
        user="root",
        password="123456",
        database="atm_demo"
    )
    cur = conn.cursor()
    cur.execute("SELECT pin_hash FROM cards WHERE card_no=%s", (card_no,))
    row = cur.fetchone()
    conn.close()
    if not row:
        print("❌ Card not found.")
        return False
    return row[0] == hashlib.sha256(pin.encode()).hexdigest()


# ✅ Hàm rút tiền
def withdraw(card_no, amount):
    conn = mysql.connector.connect(
        user="root",
        password="123456",
        database="atm_demo"
    )
    cur = conn.cursor()
    try:
        conn.start_transaction()

        # Lấy thông tin tài khoản
        cur.execute("""
            SELECT a.account_id, a.balance
            FROM accounts a
            JOIN cards c ON a.account_id = c.account_id
            WHERE c.card_no=%s FOR UPDATE
        """, (card_no,))
        result = cur.fetchone()

        if not result:
            raise Exception("Card not found")

        account_id, balance = result
        print(f"💰 Current balance: {balance}")

        # Kiểm tra số dư
        if balance < amount:
            raise Exception("Insufficient funds")

        # Trừ tiền và ghi giao dịch
        new_balance = balance - amount
        cur.execute("UPDATE accounts SET balance=%s WHERE account_id=%s", (new_balance, account_id))
        cur.execute("""
            INSERT INTO transactions(account_id, card_no, atm_id, tx_type, amount, balance_after)
            VALUES(%s, %s, 1, 'WITHDRAW', %s, %s)
        """, (account_id, card_no, amount, new_balance))

        conn.commit()
        print(f"✅ Withdraw success! You withdrew {amount}.")
        print(f"🔹 New balance: {new_balance}")

    except Exception as e:
        conn.rollback()
        print("❌ Error:", e)
    finally:
        conn.close()
