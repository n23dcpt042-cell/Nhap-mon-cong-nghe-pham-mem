import mysql.connector
import hashlib
from decimal import Decimal

DB_CONFIG = {
    "user": "atm_user",
    "password": "123456",
    "host": "127.0.0.1",
    "port": 3306,
    "database": "atm_demo"
}

def verify_pin(card_no, pin):
    conn = mysql.connector.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("SELECT pin_hash FROM cards WHERE card_no=%s", (card_no,))
    row = cur.fetchone()
    conn.close()
    if not row:
        print("❌ Thẻ không tồn tại.")
        return False
    pin_hash = hashlib.sha256(pin.encode()).hexdigest()
    return row[0] == pin_hash

def withdraw(card_no, amount):
    conn = mysql.connector.connect(**DB_CONFIG)
    cur = conn.cursor()
    try:
        conn.start_transaction()
        cur.execute("""
            SELECT a.account_id, a.balance
            FROM accounts a JOIN cards c ON a.account_id = c.account_id
            WHERE c.card_no=%s FOR UPDATE
        """, (card_no,))
        result = cur.fetchone()

        if not result:
            raise Exception("Thẻ không hợp lệ.")
        
        account_id, balance = result
        balance = Decimal(balance)
        amount = Decimal(amount)

        if balance < amount:
            raise Exception("Số dư không đủ.")
        
        new_balance = balance - amount

        cur.execute("UPDATE accounts SET balance=%s WHERE account_id=%s", (new_balance, account_id))
        cur.execute("""
            INSERT INTO transactions (account_id, card_no, atm_id, tx_type, amount, balance_after)
            VALUES (%s, %s, 1, 'WITHDRAW', %s, %s)
        """, (account_id, card_no, amount, new_balance))

        conn.commit()
        print(f"✅ Rút {amount}đ thành công! Số dư còn lại: {new_balance}đ")
    except Exception as e:
        conn.rollback()
        print("❌ Lỗi:", e)
    finally:
        conn.close()
