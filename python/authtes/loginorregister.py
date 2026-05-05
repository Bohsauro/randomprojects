import tkinter as tk
import sqlite3
from argon2 import PasswordHasher
import time


connection = sqlite3.connect('users.db')

cursor = connection.cursor()

ph = PasswordHasher()

def controlla_esistenza(username):
    cursor.execute('SELECT 1 FROM user WHERE Username = ?', (username,))
    return cursor.fetchone() is not None

def login():
    print("login")
    username = username_input.get()
    password = password_input.get()

    if username != "" and controlla_esistenza(username):
        user = (username, password)
        
        cursor.execute("SELECT password FROM user WHERE username = ?", (username,))
        riga = cursor.fetchone()
        hash = riga[0]
        if ph.verify(hash, password):
            print("login effettuato")
        else:
            print("password errata")
        
    else:
        print("account non esiste")
    


def register():
    print("register")
    username = username_input.get()
    password = password_input.get()

    

    if username != "" and not controlla_esistenza(username):
        new_user = (username, ph.hash(password))
        cursor.execute('INSERT INTO user (Username, Password) VALUES (?, ?)', new_user)
        connection.commit()
        print("creato")
    else:
        print("username già usato")



window = tk.Tk()

window.geometry("600x600")
window.title("accesso")
window.resizable(False, False)

login_button = tk.Button(text="Login", command=login)
login_button.grid(row=4, column=1)
register_button = tk.Button(text="Register", command=register)
register_button.grid(row=4, column=0, pady=20)

username_input = tk.Entry()
username_input.grid(row=1, column=0, sticky="WE", padx=10)
password_input = tk.Entry()
password_input.grid(row=3, column=0, sticky="WE", padx=10)

username_label = tk.Label(window,
                         text="USERNAME:",
                         font=("Helvetica", 15))
username_label.grid(row=0, column=0, sticky="N", padx=20, pady=10)

password_label = tk.Label(window,
                         text="PASSWORD:",
                         font=("Helvetica", 15))
password_label.grid(row=2, column=0, sticky="N", padx=20, pady=10)

close_button = tk.Button(text="close", command=connection.close)

if __name__ == "__main__":
    window.mainloop()
