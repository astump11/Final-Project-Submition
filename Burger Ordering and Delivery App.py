"""The main purpose of this program is to make it easy for a user to order a burger and have it delivered to them"""
from tkinter import messagebox
from tkinter import *
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
            self.Mayo = 0
            self.Mustard = 0
            self.Ketchup = 0
            self.Option_1_counter = 0
            self.Option_2_counter = 0
            self.Option_3_counter = 0
            self.total = 0
            def Menu(): #current pricing is a place holder for now until futher devoloped 
                messagebox.showinfo(title = "Menu",message = "Option 1, double decker double pounder - 11.39$, Option 2, Cheesemegedon - 11.76$, Option 3, Bacons revenge - 17.91$, Option 4, Build Your Own, prices may differ upon creation.")
                messagebox.showwarning(title="NOTICE",message="NOTE, cliking on ethier option will result in said option being added to your order!!!")
                self.Option_1["state"] = "normal"
                self.Option_1_display["state"] = "normal"
                self.Option_2["state"] = "normal"
                self.Option_2_display["state"] = "normal"
                self.Option_3["state"] = "normal"
                self.Option_3_display["state"] = "normal"
                self.Option_BYO["state"] = "normal"
                self.Pricebeforetax["state"] = "normal"
                self.Option_1_counter_display["state"] = "normal"
                self.Option_2_counter_display["state"] = "normal"
                self.Option_3_counter_display["state"] = "normal"
            def Menu_option_1():
                self.Buns += 1 
                self.Burger += 2
                self.Lettuce += 2
                self.Cheese += 2
                self.Onion += 2
                self.Pickle += 4
                self.Totmato += 2
                self.Bacon += 2
                self.Mayo += 1
                self.Mustard += 1
                self.Ketchup += 1
                self.Option_1_counter += 1
                self.Option_1_counter_display = self.addButton(text = "Number of time you ordered option 1:" + str(self.Option_1_counter), row = 3,
                                    column = 0)
                self.total += (self.Buns * 0.22) + (self.Burger * 4.26) + ( self.Lettuce * 0.04) + (self.Cheese * 0.29) + (self.Onion * 0.1) + (self.Pickle * 0.1) + (self.Totmato * 0.03) + (self.Bacon * 0.29) + (self.Mayo * 0.25) + (self.Mustard * 0.25) + ( self.Ketchup * 0.25)
                self.Pricebeforetax = self.addButton(text = "Current price before tax " + str(self.total), row = 2,
                                    column = 0)
                self.Buns = 0 
                self.Burger = 0 
                self.Lettuce = 0 
                self.Cheese = 0
                self.Onion = 0 
                self.Pickle = 0
                self.Totmato = 0
                self.Bacon = 0
                self.Mayo = 0
                self.Mustard = 0
                self.Ketchup = 0
            def Menu_option_2 ():
                self.Buns += 1
                self.Burger += 2 
                self.Lettuce += 0 
                self.Cheese += 6
                self.Onion += 0 
                self.Pickle += 2
                self.Totmato += 0
                self.Bacon += 2
                self.Mayo += 0
                self.Mustard += 1
                self.Ketchup += 1
                self.Option_2_counter += 1
                self.Option_2_counter_display = self.addButton(text = "Number of time you ordered option 2:" + str(self.Option_2_counter), row = 4,
                                    column = 0)
                self.total += (self.Buns * 0.22) + (self.Burger * 4.26) + ( self.Lettuce * 0.04) + (self.Cheese * 0.29) + (self.Onion * 0.1) + (self.Pickle * 0.1) + (self.Totmato * 0.03) + (self.Bacon * 0.29) + (self.Mayo * 0.25) + (self.Mustard * 0.25) + ( self.Ketchup * 0.25)
                self.Pricebeforetax = self.addButton(text = "Current price before tax " + str(self.total), row = 2,
                                    column = 0)
                self.Buns = 0 
                self.Burger = 0 
                self.Lettuce = 0 
                self.Cheese = 0
                self.Onion = 0 
                self.Pickle = 0
                self.Totmato = 0
                self.Bacon = 0
                self.Mayo = 0
                self.Mustard = 0
                self.Ketchup = 0
            def Menu_option_3 ():
                self.Buns += 1
                self.Burger += 3
                self.Lettuce += 0 
                self.Cheese += 2
                self.Onion += 1 
                self.Pickle += 0
                self.Totmato += 0
                self.Bacon += 12
                self.Mayo += 1
                self.Mustard += 1
                self.Ketchup += 1
                self.Option_3_counter += 1
                self.Option_3_counter_display = self.addButton(text = "Number of time you ordered option 3:" + str(self.Option_3_counter), row = 5,
                                    column = 0)
                self.total += (self.Buns * 0.22) + (self.Burger * 4.26) + ( self.Lettuce * 0.04) + (self.Cheese * 0.29) + (self.Onion * 0.1) + (self.Pickle * 0.1) + (self.Totmato * 0.03) + (self.Bacon * 0.29) + (self.Mayo * 0.25) + (self.Mustard * 0.25) + ( self.Ketchup * 0.25)
                self.Pricebeforetax = self.addButton(text = "Current price before tax " + str(self.total), row = 2,
                                    column = 0)
                self.Buns = 0 
                self.Burger = 0 
                self.Lettuce = 0 
                self.Cheese = 0
                self.Onion = 0 
                self.Pickle = 0
                self.Totmato = 0
                self.Bacon = 0
                self.Mayo = 0
                self.Mustard = 0
                self.Ketchup = 0
            def Menu_option_BYO ():
                self.myLabel = self.addLabel(text = "Hello Valued Customer, welcome to the build our own section of the appplease enter into the following fields for what you want for your burger",
                                       row = 5, column = 5,
                                       sticky = "NSEW",
                                       columnspan = 11)
                self.Buns = self.addFloatField(value = 0,row = 1, column = 8)
                self.Burger = self.addFloatField(value = 0,row = 2, column = 8)
                self.Lettuce = self.addFloatField(value = 0,row = 3, column = 8) 
                self.Cheese = self.addFloatField(value = 0,row = 4, column = 8)
                self.Onion = self.addFloatField(value = 0,row = 5, column = 8) 
                self.Pickle = self.addFloatField(value = 0,row = 6, column = 8)
                self.Totmato = self.addFloatField(value = 0,row = 7, column =8)
                self.Bacon = self.addFloatField(value = 0,row = 8, column = 8)
                self.Mayo = self.addFloatField(value = 0,row = 9, column = 8)
                self.Mustard = self.addFloatField(value = 0,row = 10, column = 8)
                self.Ketchup = self.addFloatField(value = 0,row = 11, column = 8)
                messagebox.showinfo(title = "!!!Note!!!",message = "The current version of this app does not keep indiviudul track of build your own burger orders, if you order more than one then some assemble will be required")
                self.total += (self.Buns * 0.22) + (self.Burger * 4.26) + ( self.Lettuce * 0.04) + (self.Cheese * 0.29) + (self.Onion * 0.1) + (self.Pickle * 0.1) + (self.Totmato * 0.03) + (self.Bacon * 0.29) + (self.Mayo * 0.25) + (self.Mustard * 0.25) + ( self.Ketchup * 0.25)
                self.Pricebeforetax = self.addButton(text = "Current price before tax " + str(self.total), row = 2,
                                    column = 0)
                self.Buns = 0 
                self.Burger = 0 
                self.Lettuce = 0 
                self.Cheese = 0
                self.Onion = 0 
                self.Pickle = 0
                self.Totmato = 0
                self.Bacon = 0
                self.Mayo = 0
                self.Mustard = 0
                self.Ketchup = 0
            self.myLabel = self.addLabel(text = "Hello Valued Customer, this app will let you order a burger and have it delivered to you",
                                       row = 0, column = 0,
                                       sticky = "NSEW",
                                       columnspan = 1)
            self.Menuoptions = self.addButton(text = "Menu", row = 1,
                                    column = 0, command = Menu)
            self.Pricebeforetax = self.addButton(text = "Current price before tax " + str(self.total), row = 2,
                                    column = 0,state= "disabled")
            self.Option_1_counter_display = self.addButton(text = "Number of time you ordered option 1:" + str(self.Option_1_counter), row = 3,
                                    column = 0,state= "disabled")
            self.Option_2_counter_display = self.addButton(text = "Number of time you ordered option 2:" + str(self.Option_2_counter), row = 4,
                                    column = 0,state= "disabled")
            self.Option_3_counter_display = self.addButton(text = "Number of time you ordered option 3:" + str(self.Option_3_counter), row = 5,
                                    column = 0,state= "disabled")                        
            self.Option_1 = self.addButton(text = "Option 1", row = 1,
                                    column = 1, command = Menu_option_1, state= "disabled")
            self.Option_1_display = self.addButton(text = "Double Decker Double Pounder 11.39$", row = 2,
                                    column = 1, command = Menu_option_1, state= "disabled")
            self.Option_2 = self.addButton(text = "Option 2", row = 1,
                                    column = 2, command = Menu_option_2, state="disabled")
            self.Option_2_display = self.addButton(text = "Cheesemegedon - 11.76$", row = 2,
                                    column = 2, command = Menu_option_2, state="disabled")                    
            self.Option_3 = self.addButton(text = "Option 3", row = 1,
                                    column = 3, command = Menu_option_3, state= "disabled")
            self.Option_3_display = self.addButton(text = "Bacons revenge - 17.91$", row = 2,
                                    column = 3, command = Menu_option_3, state= "disabled")
            self.Option_BYO = self.addButton(text = "Option Build your own", row = 1,
                                    column = 4, command = Menu_option_BYO, state= "disabled")
def main(): #actually runs the GUI
    BODA().mainloop()
if __name__ == "__main__":
    for i in range(1,2):
        main()

        