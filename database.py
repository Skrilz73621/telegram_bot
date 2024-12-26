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
                    extra_comments TEXT,
                    date DATE
                )
            ''')
            conn.execute('''
                CREATE TABLE IF NOT EXISTS dish (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    price FlOAT,
                    description TEXT,
                    picture TEXT,
                    category TEXT
                )
            ''')            
            conn.commit()


    def save_poll(self, data:dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
                    INSERT INTO poll (name, phone_number, food_rating, cleanliness_rating, extra_comments, date)
                    VALUES(?, ?, ?, ?, ?, ?)
                """,
                (data['name'], data['phone_number'], data['food_rating'], data['cleanliness_rating'], data['extra_comments'], data['date'])
            )
        
    def save_dish(self, data:dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
                    INSERT INTO dish (name, price, description, picture, category)
                    VALUES(?, ?, ?, ?, ?)
                """,
                (data['name'], data['price'], data['description'],data['picture'], data['category'])
            )
            
    def show_all_dishes(self):
        with sqlite3.connect(self.path) as conn:
            result = conn.execute(
                """
                    SELECT * FROM dish 
                    ORDER BY price ASC
                """
            )
            
            result.row_factory = sqlite3.Row
            data = result.fetchall()
            return [dict(row) for row in data]
            