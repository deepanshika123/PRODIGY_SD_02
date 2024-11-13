import tkinter as tk
from random import randint

n=randint(1,100)
guesses=1

def GuessCheck():
    global guesses
    try:
     guess=int(entry.get())
     if guess<1 or guess>100:
        result.config(text="Please enter a number between 1 and 100" , fg="red")
     elif guess>n:
        result.config(text="Lower number please" , fg="blue")
        guesses+=1
     elif guess<n:
        result.config(text="Higher number please" , fg="blue")
        guesses+=1
     else:
        result.config(text=f"Correct Answer! The number was {n}. You Guessed it in {guesses} attempted." , fg="black")
        GuessButton.config(state="disabled")
    except ValueError:
      result.config(text=f"Please enter a valid number" , fg="red")


def ReStart():
   global n , guesses
   n=randint(1,100)
   guesses=1
   result.config(test="Guess a number between 1 to 100" , fg="gray")
   entry.delete(0,tk.END)
   GuessButton.config(state="normal")



window=tk.Tk()
window.title("Number Guessing Game")
window.geometry("400x200")
window.config(bg="#f0f0f5")

instruction=tk.Label(window, text="Guess a number between 1 and 100" , font=("Georgia",15) , bg="#f0f0f5" , fg="#333333")
instruction.pack(pady=5)

entry=tk.Entry(window , font=("Georgia" , 12) , width=10 , bg="#e6e6ff" , fg="#333333")
entry.pack(pady=7)

GuessButton=tk.Button(window,text="Submit Guess" , command=GuessCheck, font=("Arial", 10), bg="#4CAF50", fg="white", activebackground="#45a049")
GuessButton.pack(pady=7)

result=tk.Label(window, text="" ,font=("Arial", 12), bg="#f0f0f5")
result.pack(pady=5)

ReStartButtom=tk.Button(window, text="Restart" , command=ReStart , font=("Arial", 10), bg="#FF5722", fg="white", activebackground="#e64a19")
ReStartButtom.pack(pady=5)

window.mainloop()
