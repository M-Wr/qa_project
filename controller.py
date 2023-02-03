#-	SQL Table within your database that contains order_id, customer_name, drink, size, extras, price,
extras = []
class controller:

    def cmrNameInput():
        name = input("Hello, what is your name?: ")
        return name

    def drinkInput():
        order = input("What drink would you like?: ")
        return order

    def sizeInput():
        size = input("What size drink would you like?(sml/med/lrg): ")
        size = size.lower()
        return size

    def extrasInput():
        yes = input("would you like any extras?: ")
        yes = yes.lower()
        while yes == "yes":
            yes = input("would you like any extras?: ")
            extra = input("What extra would you like?: ")
            extras.append(extra)
        return extras
        
    def calcPrice(drinkCost, extras):
        price = 0
        price += drinkCost
        price += (len(extras) * 0.5)
