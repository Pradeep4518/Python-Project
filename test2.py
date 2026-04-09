import tkinter as tk
from tkinter import messagebox

# Create window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Game variables
current_player = "X"
buttons = [""] * 9

# Check winner
def check_winner():
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    
    for pos in win_positions:
        if buttons[pos[0]] == buttons[pos[1]] == buttons[pos[2]] != "":
            return True
    return False

# Button click
def click(index):
    global current_player
    
    if buttons[index] == "":
        buttons[index] = current_player
        btn_list[index].config(text=current_player)

        if check_winner():
            messagebox.showinfo("Game Over", f"🎉 Player {current_player} wins!")
            reset_game()
            return

        if "" not in buttons:
            messagebox.showinfo("Game Over", "🤝 It's a draw!")
            reset_game()
            return

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Reset game
def reset_game():
    global buttons, current_player
    buttons = [""] * 9
    current_player = "X"
    for btn in btn_list:
        btn.config(text="")

# Create buttons
btn_list = []
for i in range(9):
    btn = tk.Button(root, text="", font=("Arial", 20), width=5, height=2,
                    command=lambda i=i: click(i))
    btn.grid(row=i//3, column=i%3)
    btn_list.append(btn)

# Run app
root.mainloop()
