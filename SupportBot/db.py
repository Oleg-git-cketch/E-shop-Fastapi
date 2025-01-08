import sqlite3


connection = sqlite3.connect('support.db', check_same_thread=False)
sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS users (tg_id INTEGER, name TEXT, number TEXT);')

def register(tg_id, name, number):
    sql.execute('INSERT INTO users VALUES (?, ?, ?);', (tg_id, name, number))
    connection.commit()

def check_user(tg_id):
    if sql.execute('SELECT * FROM users WHERE tg_id=?;', (tg_id,)).fetchone():
        return True
    else:
        return False
