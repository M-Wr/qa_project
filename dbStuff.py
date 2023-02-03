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

    def addDrink(val1, val2):
        query = f"INSERT INTO prices(drink, price) VALUES ('{val1}','{val2}')"
        conn.commit()
        return repo_db.dataQuery(query)

    def updateDrinkName(name, drinkId):
        query = f"UPDATE prices SET drink = '{name}' WHERE drink_id = '{drinkId}';"
        return repo_db.dataQuery(query)

    def updateDrinkPrice(price, drinkId):
        query = f"UPDATE prices SET price = '{price}' WHERE drink_id = '{drinkId}';"
        return repo_db.dataQuery(query)

    def readAllDrinks():
        query = "SELECT * FROM prices"
        return repo_db.selectQuery(query)

    def readAllOrders():
        query = "SELECT * FROM orders"
        return repo_db.selectQuery(query)

    def getPrice(drinkId):
        query = f"SELECT price FROM prices where drink_id = '{drinkId}' "
        return repo_db.selectQuery(query)

    def addOrder(cmrName, cmrDrink, cmrSize, cmrExtras, cmrCost):
        query = f"INSERT INTO orders(customer_name, drink, size, extras, price) VALUES ('{cmrName}', '{cmrDrink}','{cmrSize}','{cmrExtras}', '{cmrCost}'')"
        return repo_db.dataQuery(query)


print(repo_db.readAllOrders())