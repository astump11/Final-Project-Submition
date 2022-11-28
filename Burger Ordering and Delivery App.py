"""The main purpose of this program is to make it easy for a user to order a burger and have it delivered to them"""
from breezypythongui import EasyFrame
class BODA(EasyFrame):
        def __init__(self):
            EasyFrame.__init__(self, title = "Burger Ordering and Delivery App")
            self.Buns = 0 #set to 0 for defualt
            self.Burger = 0 #will have actuall pricing for Build your own and menu items
            self.Lettuce = 0 
            self.Cheese = 0
            self.Onion = 0 
            self.Pickle = 0
            self.Totmato = 0
            self.Bacon = 0
            self.Dicedonion = 0
            self.Mayo = 0
            self.Mustard = 0
            self.Ketchup = 0
            self.Relish = 0
            self.myLabel = self.addLabel(text = "Hello Valued Customer, this app will let you order a burger and have it delivered to you",
                                       row = 0, column = 0,
                                       sticky = "NSEW",
                                       columnspan = 1)
            self.Menu = self.addButton(text = "Menu", row = 1,
                                    column = 1, command = self.Menuoptions)

def Menuoptions(self): #current pricing is a place holder for now until futher devoloped 
    self.messageBox(title = "Menu",message = "Option 1, double decker double pounder - 12.50$, Option 2, Cheesemegedon - 15.99$, Option 3, Bacons revege - 25.99, Option 4, build your own price varyies on creation ")

def main(): #actually runs the GUI
    BODA().mainloop()
if __name__ == "__main__":
    while True:
        main()

        