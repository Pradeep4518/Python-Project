import random

# Create empty board
def create_board():
    return [[0 for _ in range(9)] for _ in range(9)]

# Print board
def print_board(board):
    print()
    for i in range(9):
        for j in range(9):
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
            if (j+1) % 3 == 0 and j != 8:
                print("|", end=" ")
        print()
        if (i+1) % 3 == 0 and i != 8:
            print("-"*21)
    print()

# Check valid move
def is_valid(board, row, col, num):
    if num in board[row]:
        return False

    for i in range(9):
        if board[i][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[start_row+i][start_col+j] == num:
                return False

    return True

# Fill board using backtracking
def fill_board(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                nums = list(range(1, 10))
                random.shuffle(nums)

                for num in nums:
                    if is_valid(board, row, col, num):
                        board[row][col] = num

                        if fill_board(board):
                            return True

                        board[row][col] = 0
                return False
    return True

# Remove numbers to make puzzle
def remove_numbers(board, attempts=40):
    while attempts > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)

        if board[row][col] != 0:
            board[row][col] = 0
            attempts -= 1

# Game logic
def play():
    full_board = create_board()
    fill_board(full_board)

    puzzle = [row[:] for row in full_board]
    remove_numbers(puzzle)

    while True:
        print_board(puzzle)

        if all(0 not in row for row in puzzle):
            print("🎉 You solved the Sudoku!")
            break

        try:
            row = int(input("Row (1-9): ")) - 1
            col = int(input("Col (1-9): ")) - 1
            num = int(input("Number (1-9): "))

            if puzzle[row][col] != 0:
                print("Cell already filled!\n")
            elif is_valid(puzzle, row, col, num):
                puzzle[row][col] = num
            else:
                print("Invalid move!\n")

        except:
            print("Invalid input!\n")

# Run multiple times
while True:
    play()
    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye!")
        break
