from dbStuff import *
from controller import *



extras = []
def cost():
    getPrice = controller.getPrice()
    thePrice = getPrice(2)
    for w in thePrice:
        w = str(w)[1:5]
        w = float(w)
    return w 

def drinkSml(w):
    w = w * 0.9
    w = round(w, 2)
    return w

def drinkLrg(w):
    w = w * 2
    w = round(w, 2)
    return w

def printPrice(w):
    return f"The price is {w}"

def extrasLoop(cmrExtras):
    cmrExtras = controller.extrasInput(cmrExtras)



print("""
========================================

Welcome to MaxBucks

1. Espresso
2. Flat White
3. Americano
4. Cortado
5. Latte
6. Tea

""")

cmrName = controller.cmrNameInput()
cmrDrink = controller.drinkInput()
menu = ["1","2","3","4","5","6","7"]
while cmrDrink not in menu:
    print("Invalid input, try again")
    cmrDrink = controller.drinkInput()

cmrDrink = int(cmrDrink)
while not 1 <= cmrDrink <= 7:
    print("Invalid input, try again: ")
    cmrDrink = controller.drinkInput()
    cmrDrink = int(cmrDrink)

cmrSize = controller.sizeInput()
cmrSize = cmrSize.lower()
while cmrSize not in ["sml","med","lrg"]:
    cmrSize = input("Invalid input, try again: ")


YoN = ["y","n"]
#asking about another extra
yes = controller.extrasInputYoN()
while yes not in YoN:
    yes = input("Please try again (y/n):")
cmrExtras = []

# controller.extraLoop(extras)
while yes == "y":
    cmrExtras = controller.extrasInput(cmrExtras)
    # extras = []
    yes = controller.extraAnother()

if cmrSize == "sml":
    sizeMulti = 0.9
elif cmrSize == "lrg":
    sizeMulti = 1.25
else:
    sizeMulti = 1
cmrCost =(repo_db.getPrice(cmrDrink))
# cmrCost = int(cmrCost)


repo_db.addOrder(cmrName, cmrDrink, cmrSize, cmrExtras, cmrCost)
conn.commit()
print("Order added")
print("Thank you")
print(repo_db.readAllOrders())


#[(1, 'Cappucino', 3.0), (2, 'Espresso', 1.75), (3, 'Flat White', 2.25), (4, 'Americano', 2.0), (5, 'Cortado', 2.1), (6, 'Cappucino', 3.0), (7, 'Latte', 2.75), (8, 'tea', 1.75)]

print("========================================")