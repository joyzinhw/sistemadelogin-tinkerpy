import sqlite3

#criar banco 
conn = sqlite3.connect("User.db")


cursor = conn.cursor()

#criar tabelas
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    User TEXT NOT NULL,
    Password TEXT NOT NULL
);
""")

print("conectado ao login")
