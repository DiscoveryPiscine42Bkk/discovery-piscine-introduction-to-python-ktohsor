import sys
from checkmate import is_king_in_check  # เรียกใช้ฟังก์ชันจากไฟล์ checkmate.py

if __name__ == "__main__":
    # รับกระดานหมากรุกจาก argument ที่พิมพ์ตอนรันโปรแกรม
    board = [line.strip() for line in sys.argv[1:]]

    # ถ้าไม่ได้ส่งกระดานมาเลย ก็ไม่ต้องทำอะไร
    if not board:
        exit()

    try:
        # เรียกฟังก์ชันเช็ก และแสดงผล
        result = is_king_in_check(board)
        print("Success" if result else "Fail")
    except:
        pass 
    