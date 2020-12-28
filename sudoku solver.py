COLUMN_LENGTH = ROW_LENGTH = BOARD_LENGTH = 9

board = [[7,8,0,4,0,0,1,2,0],
         [6,0,0,0,7,5,0,0,9],
         [0,0,0,6,0,1,0,7,8],
         [0,0,7,0,4,0,2,6,0],
         [0,0,1,0,5,0,9,3,0],
         [9,0,4,0,6,0,0,0,5],
         [0,7,0,3,0,0,0,1,2],
         [1,2,0,0,0,7,4,0,0],
         [0,4,9,2,0,6,0,0,7]]

def print_board(board):
    for idx in range(BOARD_LENGTH):
        if not idx % 3 and idx !=0:
            print("- - - - - - - - - - -")
        for i, e in enumerate(board[idx]):
            if not i % 3 and i != 0:
                print("| ", end ="")
            if i == 8:
                print(e)
            else:
                print(str(e) + " ", end="")

def get_empty_slot(board):
    for row in range(ROW_LENGTH):
        for col in range(COLUMN_LENGTH):
            if board[row][col] == 0:
                return (row, col)
    return None

def is_valid(board, val, pos):
    row_idx, col_idx = pos[0], pos[1]
    
    for col in range(COLUMN_LENGTH):
        if val == board[row_idx][col] and col != col_idx:
            return False

    for row in range(ROW_LENGTH):
        if val == board[row][col_idx] and row != row_idx:
            return False

    for box_row in range((row_idx // 3) * 3, (row_idx // 3) * 3 + 3):
        for box_col in range((col_idx // 3) * 3, (col_idx // 3) * 3+ 3):
            if val == board[box_row][box_col] and (box_row, box_col) != pos:
                return False
    
    return True

def solve(board):
    ran_slot = get_empty_slot(board)
    if not ran_slot:
        return True
    else:
        row, col = ran_slot
    
    for val in range(1, 10):
        if is_valid(board, val, (row, col)):
            board[row][col] = val
            
            if solve(board):
                return True
            
            board[row][col] = 0
    
    return False
            
    
print_board(board)
solve(board)
print("\n\n")
print_board(board)