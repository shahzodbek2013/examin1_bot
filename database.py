import sqlite3 as sql


connection = sql.Connection("Connect.database")
cursor = connection.cursor()


def create_table():    
    cursor.execute(
        '''
            CREATE TABLE IF NOT EXISTS Users(username TEXT, user_id TEXT);
        '''
    )

def inert_in(name, user_id):
    sql = f"""INSERT INTO Users(username, user_id) VALUES('{name}', '{user_id}');"""
    print(sql)
    cursor.execute(sql)

def get_all_musics():
    result = cursor.execute(
        '''
            SELECT * FROM Users
        '''
    )
    return result.fetchall()