def is_king_in_check(board):
    size = len(board)

 
    for row in board:
        if len(row) != size:
            return False

     
    king_pos = None
    for i in range(size):
        for j in range(size):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        return False   

    kx, ky = king_pos  

    
    directions = {
        'R': [(-1, 0), (1, 0), (0, -1), (0, 1)],   
        'B': [(-1, -1), (-1, 1), (1, -1), (1, 1)],   
        'Q': [(-1, 0), (1, 0), (0, -1), (0, 1),
              (-1, -1), (-1, 1), (1, -1), (1, 1)],  
        'P': [(1, -1), (1, 1)],   
    }

    
    def in_bounds(x, y):
        return 0 <= x < size and 0 <= y < size

    
    for i in range(size):
        for j in range(size):
            piece = board[i][j]

            if piece == '.' or piece == 'K':
                continue

            if piece == 'P':
                for dx, dy in directions['P']:
                    x, y = i + dx, j + dy
                    if (x, y) == (kx, ky):
                        return True

            elif piece in 'RBQ':
                for dx, dy in directions[piece]:
                    x, y = i + dx, j + dy
                    while in_bounds(x, y):
                        target = board[x][y]
                        if (x, y) == (kx, ky):
                            return True
                        if target != '.':
                            break   
                        x += dx
                        y += dy

    return False 