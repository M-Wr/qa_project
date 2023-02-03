from db_stuff import *
from controller import *


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


print("""
========================================

Welcome to MaxBucks

""")

a = controller.cmrNameInput()
controller.drinkInput()
controller.sizeInput()
controller.extrasInput()

print(a)







print("========================================")