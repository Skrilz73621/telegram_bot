import sqlite3

class Database:
    def __init__(self, path:str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS poll (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    age INTEGER,
                    genre GENRE
                )
            ''')
            conn.commit()


    def save_poll(self, data:dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
                    INSERT INTO poll (name, age, genre)
                    VALUES(?, ?, ?)
                """,
                (data['name'], data['age'], data['genre'])
            )
        
        