board = [" "]*9
def board_display():
    print(board[0],"|",board[1],"|",board[2])
    print("--*---*--")
    print(board[3],"|",board[4],"|",board[5])
    print("--*---*--")
    print(board[6],"|",board[7],"|",board[8])
    print()
def check(player):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for combo in wins:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False
def play_game():
    player = "X"
    for turn in range(9):
        board_display()
        move = int(input(f"Player {player}, choose position(1-9): ")) - 1
        if board[move] == " ":
            board[move] = player
        else:
            print("Position already taken!")
            continue
        if check(player):
            board_display()
            print(f"Player {player} wins!")
            return
        player = "O" if player == "X" else "X"
    board_display()
    print("It is draw")
while True:
    play_game()
    again = input("Are you intersed to play again ?(yes / no): ").lower()
    if again != "yes":
        print("Exiting.....")
        break
    else:
        board  = [" "]*9
        play_game()
        
