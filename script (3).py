import random

# Define constants for the players
HUMAN = 'X'
AI = 'O'

# Create the game board
def create_board():
    return [' ' for _ in range(9)]

# Display the game board
def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}\n---------")
    print(f"{board[3]} | {board[4]} | {board[5]}\n---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Check if a player has won
def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Check if the board is full
def is_board_full(board):
    return ' ' not in board

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, maximizing_player):
    if check_winner(board, AI):
        return 1
    if check_winner(board, HUMAN):
        return -1
    if is_board_full(board):
        return 0
    
    if maximizing_player:
        max_eval = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = AI
                eval = minimax(board, depth + 1, False)
                board[i] = ' '
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = HUMAN
                eval = minimax(board, depth + 1, True)
                board[i] = ' '
                min_eval = min(min_eval, eval)
        return min_eval

# Find the best move using minimax and alpha-beta pruning
def find_best_move(board):
    best_move = -1
    best_eval = -float('inf')
    for i in range(9):
        if board[i] == ' ':
            board[i] = AI
            eval = minimax(board, 0, False)
            board[i] = ' '
            if eval > best_eval:
                best_eval = eval
                best_move = i
    return best_move

# Main game loop
def main():
    board = create_board()
    display_board(board)
    while True:
        move = int(input("Enter your move (0-8): "))
        if board[move] != ' ':
            print("Invalid move! Cell is already occupied.")
            continue
        board[move] = HUMAN
        display_board(board)
        
        if check_winner(board, HUMAN):
            print("You win!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break
        
        ai_move = find_best_move(board)
        board[ai_move] = AI
        print(f"AI's move: {ai_move}")
        display_board(board)
        
        if check_winner(board, AI):
            print("AI wins!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
