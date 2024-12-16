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
                    phone_number INTEGER,
                    food_rating INTEGER,
                    cleanliness_rating INTEGER,
                    extra_comments TEXT
                )
            ''')
            conn.commit()


    def save_poll(self, data:dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
                    INSERT INTO poll (name, phone_number, food_rating, cleanliness_rating, extra_comments)
                    VALUES(?, ?, ?, ?, ?)
                """,
                (data['name'], data['phone_number'], data['food_rating'], data['cleanliness_rating'], data['extra_comments'])
            )
        
        