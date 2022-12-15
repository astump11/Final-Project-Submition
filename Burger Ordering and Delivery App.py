"""The main purpose of this program is to make it easy for a user to order a burger and have it delivered to them"""
#burger ordering and delivery app version 1.0.0 author Adam Stump
from tkinter import messagebox #everything here is needed to make the program run
from tkinter import PhotoImage
from tkinter import *
from breezypythongui import EasyFrame
from breezypythongui import *
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
            self.user = None #only text based input will have the None value attached to them
            self.home = None
            self.username = None
            self.credit = 0
            self.total = 0
            self.tax = 0.07
            self.creditchecker = 0
            def Menu(): #this must be clicked on in order to access the rest of the program
                messagebox.showinfo(title = "Menu",message = "Option 1, double decker double pounder - $11.39, Option 2, Cheesemegedon - $11.76, Option 3, Bacons revenge - $17.91.")
                messagebox.showwarning(title="NOTICE",message="NOTE, clicking on either option will result in said option being added to your order!!!")
                messagebox.showinfo(title = "Canceling/removing items",message ="If you simply click on the 'number of times you order x' then it will simply reset itself back to 0")
                self.Option_1["state"] = "normal"
                self.Option_1_display["state"] = "normal"
                self.Option_2["state"] = "normal"
                self.Option_2_display["state"] = "normal"
                self.Option_3["state"] = "normal"
                self.Option_3_display["state"] = "normal"
                self.Pricebeforetax["state"] = "normal"
                self.Option_1_counter_display["state"] = "normal"
                self.Option_2_counter_display["state"] = "normal"
                self.Option_3_counter_display["state"] = "normal"
                self.Taxwithoutprice["state"] = "normal"
                self.Orderingbutton["state"] = "normal"
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
                self.Option_1_counter_display = self.addButton(text = "Number of time you ordered option 1:" + str(self.Option_1_counter), row = 6,
                                    column = 0, command=reset1)
                self.total += (self.Buns * 0.22) + (self.Burger * 4.26) + ( self.Lettuce * 0.04) + (self.Cheese * 0.29) + (self.Onion * 0.1) + (self.Pickle * 0.1) + (self.Totmato * 0.03) + (self.Bacon * 0.29) + (self.Mayo * 0.25) + (self.Mustard * 0.25) + ( self.Ketchup * 0.25)
                self.Pricebeforetax = self.addButton(text = "Current price before tax %.2f" % self.total, row = 2,
                                    column = 0)
                self.Taxwithoutprice = self.addButton(text = "Current Tax %.2f" %(self.total * self.tax), row = 3, column = 0)
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
                self.Option_2_counter_display = self.addButton(text = "Number of time you ordered option 2:" + str(self.Option_2_counter), row = 7,
                                    column = 0, command=reset2)
                self.total += (self.Buns * 0.22) + (self.Burger * 4.26) + ( self.Lettuce * 0.04) + (self.Cheese * 0.29) + (self.Onion * 0.1) + (self.Pickle * 0.1) + (self.Totmato * 0.03) + (self.Bacon * 0.29) + (self.Mayo * 0.25) + (self.Mustard * 0.25) + ( self.Ketchup * 0.25)
                self.Pricebeforetax = self.addButton(text = "Current price before tax %.2f" % self.total, row = 2,
                                    column = 0)
                self.Taxwithoutprice = self.addButton(text = "Current Tax %.2f" %(self.total * self.tax), row = 3, column = 0)
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
                self.Option_3_counter_display = self.addButton(text = "Number of time you ordered option 3:" + str(self.Option_3_counter), row = 8,
                                    column = 0, command=reset3)
                self.total += (self.Buns * 0.22) + (self.Burger * 4.26) + ( self.Lettuce * 0.04) + (self.Cheese * 0.29) + (self.Onion * 0.1) + (self.Pickle * 0.1) + (self.Totmato * 0.03) + (self.Bacon * 0.29) + (self.Mayo * 0.25) + (self.Mustard * 0.25) + ( self.Ketchup * 0.25)
                self.Pricebeforetax = self.addButton(text = "Current price before tax %.2f" % self.total, row = 2,
                                    column = 0)
                self.Taxwithoutprice = self.addButton(text = "Current Tax %.2f" %(self.total * self.tax), row = 3, column = 0)
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
            def reset1(): #sets for each reset will as the name suggests reset the values in the program
                self.total -= (self.Option_1_counter * 11.39)
                self.Option_1_counter = 0
                self.Option_1_counter_display = self.addButton(text = "Number of time you ordered option 1:" + str(self.Option_1_counter), row = 6,
                                    column = 0)
                self.Pricebeforetax = self.addButton(text = "Current price before tax %.2f" % self.total, row = 2,
                                    column = 0)
                self.Taxwithoutprice = self.addButton(text = "Current Tax %.2f" %(self.total * self.tax), row = 3, column = 0)
            def reset2():
                self.total -= (self.Option_2_counter * 11.76)
                self.Option_2_counter = 0
                self.Option_2_counter_display = self.addButton(text = "Number of time you ordered option 2:" + str(self.Option_2_counter), row = 7,
                                    column = 0)
                self.Pricebeforetax = self.addButton(text = "Current price before tax %.2f" % self.total, row = 2,
                                    column = 0)
                self.Taxwithoutprice = self.addButton(text = "Current Tax %.2f" %(self.total * self.tax), row = 3, column = 0)
            def reset3():
                self.total -= (self.Option_3_counter * 11.39)
                self.Option_3_counter = 0
                self.Option_3_counter_display = self.addButton(text = "Number of time you ordered option 3:" + str(self.Option_1_counter), row = 8,
                                    column = 0)
                self.Pricebeforetax = self.addButton(text = "Current price before tax %.2f" % self.total, row = 2,
                                    column = 0)
                self.Taxwithoutprice = self.addButton(text = "Current Tax %.2f" %(self.total * self.tax), row = 3, column = 0)
            def Order(): #this is to get info from the user in order to complete the order
                self.userlabel = self.addLabel(text="enter your username here:",row=9,column=0)
                self.user = self.addTextField(text="username here: ", row=10, column=0)
                self.username = self.user.getText()
                self.homelabel = self.addLabel(text="enter your home address here:",row=11,column=0)
                self.home = self.addTextField(text="home address here: ",row=12,column=0)
                self.creditlabel = self.addLabel(text="enter your credit card here",row=13,column=0)
                self.credit= self.addIntegerField(value=0,row=14,column=0, width=10)
                self.Orderingbuttonfinal["state"] = "normal"  
            def orderplaced():   
                try: #this is to make sure that a vaild credit card number was inputed, it does not check to see if it is an actuall number
                    self.creditchecker = (self.credit.getNumber() * 1)
                except:
                    messagebox.showerror(title="Credit error",message="if you are seeing this then you may have inputed a letter instead of a number.")
                    self.Orderingbuttonfinal["state"] = "disabled"
                    while self.creditchecker != (self.credit.getNumber() * 1) :
                        break
                messagebox.showinfo(title="Order placed!",message="Your order has been placed!, And it will be delivered soon!")
                messagebox.showinfo(title="Thank you for ordering",message="Thank for ordering " + self.username)
                messagebox.showinfo(title="Final price",message="Your final total for the order is $%.2f" %(self.total + (self.total * self.tax)))
                self.Option_1["state"] = "disabled" #big ol reset of the program
                self.Option_1_display["state"] = "disabled"
                self.Option_2["state"] = "disabled"
                self.Option_2_display["state"] = "disabled"
                self.Option_3["state"] = "disabled"
                self.Option_3_display["state"] = "disabled"
                self.Pricebeforetax["state"] = "disabled"
                self.Option_1_counter_display["state"] = "disabled"
                self.Option_2_counter_display["state"] = "disabled"
                self.Option_3_counter_display["state"] = "disabled"
                self.Taxwithoutprice["state"] = "disabled"
                self.Orderingbutton["state"] = "disabled"
                self.Orderingbuttonfinal["state"] = "disabled"
                self.total -= (self.Option_1_counter * 11.39)
                self.Option_1_counter = 0
                self.Option_1_counter_display = self.addButton(text = "Number of time you ordered option 1:" + str(self.Option_1_counter), row = 6,
                                    column = 0,state="disabled")
                self.total -= (self.Option_2_counter * 11.39)
                self.Option_2_counter = 0
                self.Option_2_counter_display = self.addButton(text = "Number of time you ordered option 2:" + str(self.Option_2_counter), row = 7,
                                    column = 0,state="disabled")
                self.total -= (self.Option_3_counter * 11.39)
                self.Option_3_counter = 0
                self.Option_3_counter_display = self.addButton(text = "Number of time you ordered option 3:" + str(self.Option_1_counter), row = 8,
                                    column = 0,state="disabled")
                self.Pricebeforetax = self.addButton(text = "Current price before tax %.2f" % self.total, row = 2,
                                    column = 0,state="disabled")
                self.Taxwithoutprice = self.addButton(text = "Current Tax %.2f" %(self.total * self.tax), row = 3, column = 0, state="disabled")
            self.myLabel = self.addLabel(text = "Hello Valued Customer, this app will let you order a burger and have it delivered to you",
                                       row = 0, column = 0, #all of these labels and buttons are here to give the user something to use.
                                       sticky = "NSEW",
                                       columnspan = 1)
            self.Menuoptions = self.addButton(text = "Menu", row = 1,
                                    column = 0, command = Menu)
            self.Pricebeforetax = self.addButton(text = "Current price before tax " + str(self.total), row = 2,
                                    column = 0,state= "disabled")
            self.Taxwithoutprice = self.addButton(text = "Current Tax " + str(self.total * self.tax), row = 3,
                                    column = 0,state= "disabled")
            self.Orderingbutton = self.addButton(text = "Place your order", row = 4,
                                    column = 0,state= "disabled", command=Order)
            self.Orderingbuttonfinal = self.addButton(text = "Confirm order", row = 5,
                                    column = 0,state= "disabled", command=orderplaced)                                                
            self.Option_1_counter_display = self.addButton(text = "Number of time you ordered option 1:" + str(self.Option_1_counter), row = 6,
                                    column = 0,state= "disabled")
            self.Option_2_counter_display = self.addButton(text = "Number of time you ordered option 2:" + str(self.Option_2_counter), row = 7,
                                    column = 0,state= "disabled")
            self.Option_3_counter_display = self.addButton(text = "Number of time you ordered option 3:" + str(self.Option_3_counter), row = 8,
                                    column = 0,state= "disabled")                        
            self.Option_1 = self.addButton(text = "Option 1", row = 1,
                                    column = 1, command = Menu_option_1, state= "disabled")
            self.Option_1_display = self.addButton(text = "Double Decker Double Pounder 11.39$", row = 2,
                                    column = 1, command = Menu_option_1, state= "disabled")
            self.imageLabel1 = self.addLabel (text="",row=3,column=1)
            self.Option1imange = PhotoImage(file="Option1gif.gif")
            self.imageLabel1["image"] = self.Option1imange
            self.Option_2 = self.addButton(text = "Option 2", row = 1,
                                    column = 2, command = Menu_option_2, state="disabled")
            self.Option_2_display = self.addButton(text = "Cheesemegedon - 11.76$", row = 2,
                                    column = 2, command = Menu_option_2, state="disabled")
            self.imageLabel2 = self.addLabel (text="",row=3,column=2)
            self.Option2image = PhotoImage(file="Option2gif.gif")
            self.imageLabel2["image"] = self.Option2image                    
            self.Option_3 = self.addButton(text = "Option 3", row = 1,
                                    column = 3, command = Menu_option_3, state= "disabled")
            self.Option_3_display = self.addButton(text = "Bacons revenge - 17.91$", row = 2,
                                    column = 3, command = Menu_option_3, state= "disabled")
            self.imageLabel3 = self.addLabel (text="",row=3,column=3)
            self.Option3image = PhotoImage(file="Option3gif.gif")
            self.imageLabel3["image"] = self.Option3image
def main(): #actually runs the GUI
    BODA().mainloop()
if __name__ == "__main__":
    for i in range(1,2):
        main()

        