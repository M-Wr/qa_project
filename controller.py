#-	SQL Table within your database that contains order_id, customer_name, drink, size, extras, price,

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
#first y/n for extras
    def extrasInputYoN():
        yes = input("would you like any extras?(y/n): ")
        yes = yes.lower()
        return yes
#asking if any more extras are needed
    def extraAnother():
        YoN = ["y","n"]
        cmrExtrasYoN = input("Would you like another extra?(y/n): ")
        cmrExtrasYoN = cmrExtrasYoN.lower()
        while cmrExtrasYoN not in YoN:
            cmrExtrasYoN = input("Please try again (y/n): ")
        return cmrExtrasYoN
#adding extra to extras list
    def extrasInput(cmrExtras):
        # extras = []
        extra = input("What extra would you like?: ")
        cmrExtras.append(extra)
        return cmrExtras
#looping through 
    # def extraLoop():
    #     while yes == "y":
    #         cmrExtras = controller.extrasInput(extras)
    #         # extras = []
    #         yes = controller.extraAnother()
        
    def calcPrice(drinkCost, cmrExtras):
        price = 0
        price += drinkCost
        price += (len(cmrExtras) * 0.5)
        return price
