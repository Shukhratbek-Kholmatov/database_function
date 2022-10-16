import sqlite3
def add_user_id(user_id):
    db=sqlite3.connect("datas.db")
    cursor=db.cursor()
    cursor.execute("""CREAT TABLE IF NOT EXISTS users (
    user_id INTEGER
    )""")
    db.commit()
    cursor.execute(f"INSERT INTO users VALUES ({user_id})")
    db.commit()
    db.close()