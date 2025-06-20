import sys
from checkmate import is_king_in_check  

if __name__ == "__main__":
    
    board = [line.strip() for line in sys.argv[1:]]

    
    if not board:
        exit()

    try:
        
        result = is_king_in_check(board)
        print("Success" if result else "Fail")
    except:
        pass   