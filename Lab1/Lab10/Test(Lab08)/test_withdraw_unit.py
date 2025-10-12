import pytest
from withdraw import verify_pin, withdraw
import mysql.connector
from decimal import Decimal

DB_CONFIG = {
    "user": "atm_user",
    "password": "123456",
    "host": "127.0.0.1",
    "database": "atm_demo"
}

def get_balance(card_no):
    conn = mysql.connector.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("""
        SELECT balance FROM accounts a 
        JOIN cards c ON a.account_id = c.account_id
        WHERE c.card_no=%s
    """, (card_no,))
    bal = cur.fetchone()[0]
    conn.close()
    return Decimal(bal)

# --- verify_pin ---
def test_verify_pin_correct():
    assert verify_pin("1111222233334444", "1234") == True

def test_verify_pin_wrong():
    assert verify_pin("1111222233334444", "0000") == False

# --- withdraw ---
def test_withdraw_success():
    card = "1111222233334444"
    old_balance = get_balance(card)
    withdraw(card, 100000)
    new_balance = get_balance(card)
    assert new_balance == old_balance - Decimal(100000)

def test_withdraw_insufficient():
    card = "1111222233334444"
    old_balance = get_balance(card)
    withdraw(card, 999999999)
    new_balance = get_balance(card)
    assert new_balance == old_balance
