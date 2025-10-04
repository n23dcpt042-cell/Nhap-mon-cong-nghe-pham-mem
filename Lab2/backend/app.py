# backend/app.py
from flask import Flask, request, jsonify
import mysql.connector
from datetime import datetime, timedelta
import os

app = Flask(__name__)

DB_CONFIG = {
    'user': os.environ.get('DB_USER','root'),
    'password': os.environ.get('DB_PASS',''),
    'host': os.environ.get('DB_HOST','127.0.0.1'),
    'database': os.environ.get('DB_NAME','hotel_db')
}

def get_conn():
    return mysql.connector.connect(**DB_CONFIG)

@app.route('/rooms', methods=['GET'])
def search_rooms():
    checkin = request.args.get('checkin')
    checkout = request.args.get('checkout')
    capacity = int(request.args.get('capacity', 1))
    # Simple: return rooms whose RoomType.capacity >= capacity and Room.status='available'
    conn = get_conn()
    cur = conn.cursor(dictionary=True)
    q = """
    SELECT r.RoomID, r.RoomNumber, r.Status, rt.Name as TypeName, rt.Price, rt.Capacity
    FROM Room r JOIN RoomType rt ON r.TypeID = rt.TypeID
    WHERE rt.Capacity >= %s AND r.Status = 'available'
    LIMIT 50
    """
    cur.execute(q, (capacity,))
    rows = cur.fetchall()
    cur.close(); conn.close()
    return jsonify(rows)

@app.route('/reserve/hold', methods=['POST'])
def hold_room():
    data = request.json
    guest = data['guest']  # {Name, Email, Phone}
    room_id = data['room_id']
    checkin = data['checkin']
    checkout = data['checkout']
    hold_minutes = int(data.get('hold_minutes', 15))
    hold_expires = datetime.utcnow() + timedelta(minutes=hold_minutes)

    conn = get_conn()
    cur = conn.cursor()
    # create guest if not exists (simple)
    cur.execute("INSERT INTO Guest (Name, Phone, Email) VALUES (%s,%s,%s)",
                (guest.get('Name'), guest.get('Phone'), guest.get('Email')))
    guest_id = cur.lastrowid
    # create reservation with status 'pending' and holdExpiresAt
    cur.execute("""INSERT INTO Reservation
                   (GuestID, RoomID, CheckInDate, CheckOutDate, Status, HoldExpiresAt)
                   VALUES (%s,%s,%s,%s,'pending',%s)""",
                (guest_id, room_id, checkin, checkout, hold_expires))
    resv_id = cur.lastrowid
    # set room status to held
    cur.execute("UPDATE Room SET Status='held' WHERE RoomID=%s", (room_id,))
    conn.commit()
    cur.close(); conn.close()
    return jsonify({'resv_id': resv_id, 'hold_expires': hold_expires.isoformat()})

@app.route('/payment/callback', methods=['POST'])
def payment_callback():
    data = request.json
    resv_id = data['resv_id']
    status = data['status']  # 'success' or 'failed'
    txn = data.get('transaction')
    amount = data.get('amount', 0)

    conn = get_conn()
    cur = conn.cursor()
    # record payment
    cur.execute("""INSERT INTO Payment (ResvID, Amount, Method, Status, TransactionRef)
                   VALUES (%s,%s,%s,%s,%s)""",
                (resv_id, amount, data.get('method','card'), status, txn))
    if status == 'success':
        # confirm reservation and set room occupied
        cur.execute("UPDATE Reservation SET Status='confirmed' WHERE ResvID=%s", (resv_id,))
        # find room id
        cur.execute("SELECT RoomID FROM Reservation WHERE ResvID=%s", (resv_id,))
        row = cur.fetchone()
        room_id = row[0] if row else None
        if room_id:
            cur.execute("UPDATE Room SET Status='occupied' WHERE RoomID=%s", (room_id,))
    conn.commit()
    cur.close(); conn.close()
    return jsonify({'ok': True})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
