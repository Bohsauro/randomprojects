import tkinter as tk
import sqlite3
from argon2 import PasswordHasher


connection = sqlite3.connect('users.db')

cursor = connection.cursor()

cursor.execute('SELECT * FROM user')
tutti_gli_utenti = cursor.fetchall()

for utente in tutti_gli_utenti:
    print(f"Username: {utente[1]}, Password: {utente[2]}")