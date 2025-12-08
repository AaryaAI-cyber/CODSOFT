import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("CodSoft Task 4 - Rock Paper Scissors by Aarya")
root.geometry("400x300")
root.configure(bg="#1e272e")
root.resizable(False, False)

user_score = 0
comp_score = 0

user_score_var = tk.StringVar(value=f"User: {user_score}")
comp_score_var = tk.StringVar(value=f"Computer: {comp_score}")
result_var = tk.StringVar(value="Choose your move!")

tk.Label(root, textvariable=user_score_var, font=("Arial", 14), bg="#1e272e", fg="#27ae60").pack(pady=10)
tk.Label(root, textvariable=comp_score_var, font=("Arial", 14), bg="#1e272e", fg="#e74c3c").pack()
tk.Label(root, textvariable=result_var, font=("Arial", 16), bg="#1e272e", fg="#dcdde1").pack(pady=20)

def play(user_choice):
    global user_score, comp_score
    choices = ["Rock 🪨", "Paper 📄", "Scissors ✂️"]
    comp_choice = random.choice(choices)
    
    if user_choice == comp_choice:
        result = "Tie! Both chose " + user_choice
    elif (user_choice == "Rock 🪨" and comp_choice == "Scissors ✂️") or \
         (user_choice == "Paper 📄" and comp_choice == "Rock 🪨") or \
         (user_choice == "Scissors ✂️" and comp_choice == "Paper 📄"):
        result = "You Win! " + user_choice + " beats " + comp_choice
        user_score += 1
    else:
        result = "You Lose! " + comp_choice + " beats " + user_choice
        comp_score += 1
    
    result_var.set(result)
    user_score_var.set(f"User: {user_score}")
    comp_score_var.set(f"Computer: {comp_score}")

def reset():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    user_score_var.set(f"User: {user_score}")
    comp_score_var.set(f"Computer: {comp_score}")
    result_var.set("Choose your move!")

frame = tk.Frame(root, bg="#1e272e")
frame.pack(pady=10)

tk.Button(frame, text="Rock 🪨", font=("Arial", 14), bg="#353b48", fg="#dcdde1", command=lambda: play("Rock 🪨")).pack(side="left", padx=10)
tk.Button(frame, text="Paper 📄", font=("Arial", 14), bg="#353b48", fg="#dcdde1", command=lambda: play("Paper 📄")).pack(side="left", padx=10)
tk.Button(frame, text="Scissors ✂️", font=("Arial", 14), bg="#353b48", fg="#dcdde1", command=lambda: play("Scissors ✂️")).pack(side="left", padx=10)

tk.Button(root, text="Reset Scores", font=("Arial", 14), bg="#eb4d4b", fg="white", command=reset).pack(pady=10)

root.mainloop()
