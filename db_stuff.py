import _sqlite3 as sql
conn = sql.connect("coffee_shop.db")
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()

class repo_db:

    def CreatingTable(self):
        sql_file = open("coffee_shop.sql")
        sql_string = sql_file.read()
        cursor.executescript(sql_string)

    def selectQuery(query):
        return cursor.execute(query).fetchall()

    def dataQuery(query):
        cursor.execute(query)
        return True

    def addDrink(self, val1, val2):
        query = f"INSERT INTO prices(drink, price) VALUES ('{val1}','{val2}')"
        conn.commit()
        return repo_db.dataQuery(query)

    def updateDrinkName(self, name, drinkId):
        query = f"UPDATE movies SET drink = '{name}' WHERE drink_id = '{drinkId}';"
        return repo_db.dataQuery(query)

    def updateDrinkPrice(self, price, drinkId):
        query = f"UPDATE movies SET price = '{price}' WHERE drink_id = '{drinkId}';"
        return repo_db.dataQuery(query)

    def readAllDrinks():
        query = "SELECT * FROM prices"
        return repo_db.selectQuery(query)

    def getPrice(self, drinkId):
        query = f"SELECT price FROM prices where drink_id = '{drinkId}' "
        return repo_db.selectQuery(query)

print(repo_db.readAllDrinks())