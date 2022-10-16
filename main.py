import sqlite3
def add_user_id(user_id):
    db=sqlite3.connect("datas.db")
    cursor=db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER
    )""")
    db.commit()
    cursor.execute(f"SELECT user_id FROM users WHERE user_id={user_id}")
    data=cursor.fetchone()
    if data is None:
        cursor.execute(f"INSERT INTO users VALUES ({user_id})")
        db.commit()
    db.close()


def del_user_id(user_id):
    db = sqlite3.connect("datas.db")
    cursor = db.cursor()
    try:
        cursor.execute(f"DELETE FROM users WHERE user_id={user_id}")
        db.commit()
    except Exception as x:
        print(x)
def get_users_list():
    db = sqlite3.connect("datas.db")
    cursor = db.cursor()
    try:
        users=cursor.execute("SELECT user_id FROM users").fetchall()
        users_list=[]
        for user in users:
            users_list.append(user[0])
        return users_list
    except Exception as x:
        users_list=[]
        return users_list
        print(x)
    db.close()
def add_channel_id(channel_id):
    db = sqlite3.connect("datas.db")
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS channel (
        channel_id INTEGER
        )""")
    db.commit()
    cursor.execute(f"SELECT channel_id FROM channel WHERE channel_id={channel_id}")
    data = cursor.fetchone()
    users = cursor.execute("SELECT channel_id FROM channel ").fetchall()
    users_list = []
    for user in users:
        users_list.append(user[0])
    if data is None and len(users_list)==0:
        cursor.execute(f"INSERT INTO channel VALUES ({channel_id})")
        db.commit()
        return "Kanal qo'shildi"
    else:
        return users_list
    db.close()

def del_channel_id(channel_id):
    db = sqlite3.connect("datas.db")
    cursor = db.cursor()
    try:
        cursor.execute(f"DELETE FROM channel WHERE channel_id={channel_id}")
        db.commit()
        return "Kanal o'chirildi"
    except Exception as x:
        return "Xatolik yuz berdi"

def get_channel_id():
    db = sqlite3.connect("datas.db")
    cursor = db.cursor()
    try:
        channels = cursor.execute("SELECT channel_id FROM channel").fetchall()
        channels_list = []
        for channel in channels:
            channels_list.append(channel[0])
        return channels_list[0]
    except Exception as x:
        channels_list = []
        return channels_list
        print(x)
    db.close()
print(del_channel_id(5566))