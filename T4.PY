import random

size = 5

# Create empty grid
grid = [["." for _ in range(size)] for _ in range(size)]

# Player start position
player_pos = [0, 0]

# Random treasure position
treasure = [random.randint(0, size-1), random.randint(0, size-1)]

# Random traps
traps = []
while len(traps) < 3:
    trap = [random.randint(0, size-1), random.randint(0, size-1)]
    if trap != treasure and trap != player_pos:
        traps.append(trap)

def print_grid():
    for i in range(size):
        for j in range(size):
            if [i, j] == player_pos:
                print("P", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

def move(direction):
    if direction == "up" and player_pos[0] > 0:
        player_pos[0] -= 1
    elif direction == "down" and player_pos[0] < size-1:
        player_pos[0] += 1
    elif direction == "left" and player_pos[1] > 0:
        player_pos[1] -= 1
    elif direction == "right" and player_pos[1] < size-1:
        player_pos[1] += 1
    else:
        print("Invalid move!")

def play():
    while True:
        print_grid()
        move_input = input("Move (up/down/left/right): ").lower()
        move(move_input)

        if player_pos == treasure:
            print("💰 You found the treasure! You win!")
            break

        if player_pos in traps:
            print("💣 You hit a trap! Game over!")
            break

play()
