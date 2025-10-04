1. Giải thích use case cho ATM mini project
    🎭 Đối tượng tham gia 
        Cardholder: Thực hiện rút tiền ở ATM

        Bank customer (Người dùng): Thực hiện các thao tác như rút tiền, nạp tiền, nộp séc, xem số dư.

        Bank System (Hệ thống Ngân hàng): Kiểm tra số dư, xác thực thẻ/PIN, trừ tiền, cập nhật tài khoản.

        ATM (Hệ thống máy ATM): Trung gian giữa User và Bank System, quản lý phần cứng (nhả tiền, đếm tiền, quét séc).

    🔗 Luồng tương tác chi tiết 

    1) Use Case: Withdraw Money

        CardHolder → ATM: Insert Card

        ATM → CardHolder: Request PIN

        CardHolder → ATM: Enter PIN

        ATM → Bank System: Verify PIN

        Bank System → ATM: PIN Valid / Invalid

        ATM → CardHolder: Request Withdraw Amount

        CardHolder → ATM: Enter Amount

        ATM → Bank System: Check Balance & Deduct

        Bank System → ATM: Approval / Insufficient Funds

        ATM → CardHolder: Dispense Cash + Return Card

        (Include) Count Notes: ATM đếm số tiền trước khi nhả

    2) Use Case: Deposit Cash

        Bank Customer → ATM: Insert Card, Request Deposit

        ATM → Bank Customer: Ask to Insert Cash

        Bank Customer → ATM: Insert Cash

        ATM → Detect Counterfeit Notes (Extend): Kiểm tra tiền giả

        ATM → Bank System: Update Balance

        Bank System → ATM: Confirm Deposit

        ATM → Bank Customer: Show Success, Return Card

    3) Use Case: Deposit Cheques

        Bank Customer → ATM: Insert Cheque

        ATM → Scan Cheque Image (Include): Quét hình ảnh séc

        ATM → Bank System: Validate Cheque, Update Balance

        Bank System → ATM: Confirm Deposit

        ATM → Bank Customer: Success Message

    4) Use Case: Consult Balance

        Bank Customer → ATM: Request Balance Inquiry

        ATM → Bank System: Query Balance

        Bank System → ATM: Return Balance

        ATM → Bank Customer: Display Balance

    5) Use Case: Balance Reconciliation

        ATM → Refill Dispenser (Include): Yêu cầu thêm tiền mặt

        Maintenance/Bank System → ATM: Confirm Refill

        ATM → Bank System: Update Balance Reconciliation

    6) Use Case: Retrieve Cards that have been Swallowed

        Bank System / Maintenance → ATM: Request Retrieve Card

        ATM → Maintenance: Release Swallowed Card

    7) Use Case: Retrieve Cheques that have been Deposited

        Bank System / Maintenance → ATM: Request Retrieve Cheques

        ATM → Maintenance: Release Deposited Cheques

    2. Giải thích sequence diagram cho ATM mini project
    🎭 Đối tượng tham gia 

        Bank customer (Người dùng): Thực hiện các thao tác như rút tiền, nạp tiền, nộp séc, xem số dư.

        Bank System (Hệ thống Ngân hàng): Kiểm tra số dư, xác thực thẻ/PIN, trừ tiền, cập nhật tài khoản.

        ATM (Hệ thống máy ATM): Trung gian giữa User và Bank System, quản lý phần cứng (nhả tiền, đếm tiền, quét séc).

    🔗 Luồng tương tác chi tiết 
        Bank Customer → ATM: Insert Card 
        Khách hàng đưa thẻ vào máy ATM.

        ATM → Bank Customer: Request PIN
        ATM hiển thị màn hình yêu cầu nhập PIN.

        Bank Customer → ATM: Enter PIN
        Khách hàng nhập mã PIN.

        ATM → Bank System: Verify PIN
        ATM gửi yêu cầu xác thực PIN đến hệ thống ngân hàng.

        Bank System → ATM: PIN OK / Invalid

        Nếu sai → ATM báo lỗi cho khách hàng, giữ hoặc trả thẻ, kết thúc.

        Nếu đúng → tiếp tục giao dịch.

        ATM → Bank Customer: Show Menu
        ATM hiển thị menu các chức năng (Withdraw, Deposit, Consult balance...).

        Bank Customer → ATM: Choose Withdraw
        Khách hàng chọn chức năng rút tiền.

        ATM → Bank Customer: Enter Amount
        ATM yêu cầu nhập số tiền muốn rút.

        Bank Customer → ATM: Input Amount
        Khách hàng nhập số tiền cần rút.

        ATM → Bank System: Check Balance & Deduct
        ATM gửi yêu cầu kiểm tra số dư và trừ tiền.

        Bank System → ATM: Approval / Insufficient Funds

        Nếu số dư không đủ → ATM thông báo lỗi, trả lại thẻ, kết thúc.

        Nếu số dư đủ → tiếp tục xử lý.

        ATM → Bank Customer: Dispense Cash
        ATM nhả tiền mặt cho khách hàng.

        ATM → Bank Customer: Offer Receipt
        ATM hỏi khách hàng có muốn in biên lai không.

        Bank Customer → ATM: Confirm Yes/No
        Khách hàng lựa chọn có hoặc không.

        ATM → Bank Customer: Print Receipt (optional)
        Nếu chọn Yes → ATM in biên lai.
        Nếu chọn No → bỏ qua.

        ATM → Bank Customer: Return Card
        ATM trả lại thẻ cho khách hàng.


