from tkinter import *
from PIL import Image
import tkinter.font as font
from tkinter import messagebox

#----------------------------------Main window set up---------------------------------------------------------------------------------------------------------------------------
Main = Tk()
Main.title("GUI Pizza Ordering Page")
Main.iconbitmap(r'pizza.ico')
Main.geometry("434x400")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------Main Window Headers--------------------------------------------------------------------------------------------------------------------------
LgSz = font.Font(size=30, weight='bold')
MedSz = font.Font(size=15)
SmSz = font.Font(size=10)
MainTitle = Label(Main, text="Welcome to GUI Pizza!", font= LgSz).grid(row=0, column=0, columnspan=3)
orderText = Label(Main, text="Enter Your Order Below", font=MedSz).grid(row=1, column=0, columnspan=3)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------Main Window Functions------------------------------------------------------------------------------------------------------------------------
def exitMain():
    Main.destroy()

def appendList():
    return
"""
    selectedToppings = []
    toppingList = [pizzaPep, pizzaSg, pizzaSsg, pizzaBf, pizzaCkn, pizzaOni, pizzaGp, pizzaBo, pizzaGo, pizzaProv, pizzaChz, pizzaHam, pizzaBac, pizzaSpin, pizzaTom, pizzaGbC]
    x = 0
    while x <= len(toppingList):
        topSelector = toppingList[x]
        if topSelector.get() == 1:
            selectedToppings.append(topSelector)
        x += 1
"""

def proceedChkout():
    if sizeOption.get() == "":
        messagebox.showerror("Error", "Incorrect Size Chosen")
    if sauceOption.get() == "":
        messagebox.showerror("Error", "Incorrect Sauce Chosen")
    if sizeOption.get() != "" and sauceOption.get() != "":
        Chkout = Toplevel(Main)
        Chkout.title("GUI Pizza Checkout Page")
        Chkout.iconbitmap(r'pizza.ico')
        Chkout.geometry("450x350")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------Main Window Elements-------------------------------------------------------------------------------------------------------------------------
sizeText = Label(Main, text="Choose the size of your pizza:", font= SmSz).grid(row=2, column=0)
sauceText = Label(Main, text="Choose your Sauce:", font= SmSz).grid(row=2, column=2, sticky=W)
toppingText= Label(Main, text="Choose your toppings:", font= SmSz).grid(row=4, column=0, sticky=W)
#Pizza Size List:
pizzaSizes = ["Large", "Medium", "Small"]
sizeOption = StringVar()
sizeMenu = OptionMenu(Main, sizeOption, *pizzaSizes).grid(row=3, column=0)
#Pizza Sauce List:
sauceOption = StringVar()
pizzaSauces = ["Pizza Sauce", "Barbecue", "Ranch", "Garlic Butter"]
pizzaSauce = OptionMenu(Main, sauceOption, *pizzaSauces).grid(row=3, column=2, sticky=W)

#Toppings Check List:
pizzaPep = Checkbutton(Main, text="Pepperoni", onvalue= 1, offvalue= 0).grid(row=5, column=0, sticky=W)
pizzaSg = Checkbutton(Main, text="Sausage", onvalue= 1, offvalue= 0).grid(row=6, column=0, sticky=W)
pizzaSsg = Checkbutton(Main, text="Spicy Sausage", onvalue= 1, offvalue= 0).grid(row=7, column=0, sticky=W)
pizzaBf = Checkbutton(Main, text="Beef", onvalue= 1, offvalue= 0).grid(row=8, column=0, sticky=W)
pizzaCkn = Checkbutton(Main, text="Chicken", onvalue= 1, offvalue= 0).grid(row=9, column=0, sticky=W)                                                                   
pizzaOni = Checkbutton(Main, text="Onion", onvalue= 1, offvalue= 0).grid(row=10, column=0, sticky=W)
pizzaGp = Checkbutton(Main, text="Green Pepper", onvalue= 1, offvalue= 0).grid(row=11, column=0, sticky=W)
pizzaBo = Checkbutton(Main, text="Black Olive", onvalue= 1, offvalue= 0).grid(row=12, column=0, sticky=W)
pizzaGo = Checkbutton(Main, text="Green Olive", onvalue= 1, offvalue= 0).grid(row=5, column=2, sticky=W)
pizzaProv = Checkbutton(Main, text="Provolone Cheese", onvalue= 1, offvalue= 0).grid(row=6, column=2, sticky=W)
pizzaChz = Checkbutton(Main, text="Four Cheese", onvalue= 1, offvalue= 0).grid(row=7, column=2, sticky=W)
pizzaHam = Checkbutton(Main, text="Ham", onvalue= 1, offvalue= 0).grid(row=8, column=2, sticky=W)
pizzaBac = Checkbutton(Main, text="Bacon", onvalue= 1, offvalue= 0).grid(row=9, column=2, sticky=W)
pizzaSpin = Checkbutton(Main, text="Spinach", onvalue= 1, offvalue= 0).grid(row=10, column=2, sticky=W)
pizzaTom = Checkbutton(Main, text="Tomato", onvalue= 1, offvalue= 0).grid(row=11, column=2, sticky=W)
pizzaGbC = Checkbutton(Main, text="Garlic Butter on Crust", onvalue= 1, offvalue= 0).grid(row=12, column=2, sticky=W)
#Exit Button:
exitButSpace = Label(Main, text="").grid(row=13, column=0)
exitBut = Button(Main, text="Exit Menu", command=exitMain).grid(row=14, column=0, sticky=SW)
#Proceed to Checkout Button:
chkoutButSpace = Label(Main, text="").grid(row=13, column=2)
chkoutBut = Button(Main, text="Proceed to Checkout", command=proceedChkout).grid(row=14, column=2, sticky=E)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Main.mainloop()
