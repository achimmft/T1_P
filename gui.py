from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from tkinter import font



class MainPage:

    def __init__(self):
        self.fullScreenState = False
        self.win = tk.Tk()
        self.w = self.win.winfo_width()
        self.h = self.win.winfo_height()
        self.win.attributes("-fullscreen", self.fullScreenState)
        self.full()
        self.win.title("EmpTrak")
        #self.iconbitmap("icon.ico")


        self.f1 = tk.Frame(self.win, width = self.w) 
        self.f1.pack(side = TOP, fill = X)
        self.f15 = tk.Frame(self.win)
        self.f15.pack(side = TOP)
        self.f2 = tk.Frame(self.win)
        self.f2.pack(side = TOP, expand = TRUE)
        self.f3 = tk.Frame(self.win)
        self.f3.pack(side = TOP, expand = TRUE)
        self.f4 = tk.Frame(self.win) 
        self.f4.pack(side = TOP, expand = TRUE)
        self.f5 = tk.Frame(self.win)
        self.f5.pack(side = TOP, fill = X)

        style = Style()
        times = tk.font.Font(family = "Times", size = 14, weight = "bold")
        lucinda = tk.font.Font(family = "Lucinda Grande", size = 14, weight = "bold")
        kinnari = tk.font.Font(family = "Kinnari", size = 45, weight = "bold")
        ubuntu = tk.font.Font(family = "Ubuntu", size = 12, weight = "bold")

        #style.configure("emplab", 'underline')
        self.emplabel = tk.Label(self.f1, text = "EmpTrak \n        ______________________", height = 3, bg = "green", borderwidth = 10, relief = "groove")
        self.emplabel['font']= kinnari
        self.emplabel.pack(fill = X)
        
        self.searchlabel = tk.Label(self.f2, text = "Enter last Name or ID", height = 5, fg = "black")
        self.searchlabel['font'] = times
        self.searchlabel.pack(side = LEFT, padx = 7)
        self.search = tk.Entry(self.f2, text = 50)
        self.search.pack(side = LEFT, expand = True, ipady = 5, ipadx = 30)
        self.search['font'] = lucinda
        self.searchbut = tk.Button(self.f2, text = "Search")
        self.searchbut.pack(side= RIGHT)
        self.searchbut['font'] = times

        self.add = tk.Button(self.f3, text = "Add New Employee", command = self.add_emp)
        self.add['font'] = times
        self.add.pack(side = LEFT)

        self.back = tk.Button(self.f4, text = "Previous")
        self.back['font'] = times
        self.back.pack(side = RIGHT, pady = 30, padx = 20)
        self.help = tk.Button(self.f4, text = "Help")
        self.help['font'] = times
        self.help.pack(side = RIGHT, pady = 30, padx = 20)
        self.emplist = tk.Button(self.f4, text = "Employee Database")
        self.emplist.pack(side = LEFT, padx = 50)
        self.emplist["font"] = times

        self.bl = tk.Frame(self.f5, bg = "black")
        self.bl.pack(fill = X, side = TOP)
        self.bl = tk.Label(self.f5, bg= "Dark Green")
        self.bl.pack(fill = X)



        self.win.mainloop()

    def full(self):
        '''Makes the GUI fullSceen'''
        self.w, self.h = self.win.winfo_screenwidth(), self.win.winfo_screenheight()
        self.win.geometry("%dx%d" % (self.w, self.h))

        self.win.bind("<f>", self.toggle_fullscreen)
        self.win.bind("<Escape>", self.quit_fullscreen)



    def toggle_fullscreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.win.attributes("-fullscreen", self.fullScreenState)


    def quit_fullscreen(self, event):

        self.w, self.h = self.win.winfo_screenwidth(), self.win.winfo_screenheight()
        self.win.geometry("%dx%d" % (self.w, self.h))
        self.fullScreenState = False
        self.win.attributes("-fullscreen", self.fullScreenState)

    def add_emp(self):
        AddNewEmp()


class AddNewEmp():
    """Add New Employee window to enter in employee info"""
    def __init__(self):
        #creates add employee window
        self.fullScreenState = False
        self.addwin = tk.Tk()
        self.w = self.addwin.winfo_width()
        self.h = self.addwin.winfo_height()
        self.addwin.attributes("-fullscreen", self.fullScreenState)
        self.full()
        self.addwin.title("Add New Emplopyee")

        #fonts
        times1 = tk.font.Font(family = "arial", size = 12)
        times = tk.font.Font(family = "Times", size = 14, weight = "bold")
        lucinda = tk.font.Font(family = "Lucinda Grande", size = 15, weight = "bold")
        kinnari = tk.font.Font(family = "Kinnari", size = 45, weight = "bold")
        ubuntu = tk.font.Font(family = "Ubuntu", size = 15)
        arial = tk.font.Font(family = "Arial", size = 12)
        arial2 = tk.font.Font(family = "Arial", size = 13)

        #frames for add employee window       
        self.f1 = tk.Frame(self.addwin, width = self.w) 
        self.f1.grid(row = 0, sticky = W)
        self.f2 = tk.Frame(self.addwin)
        self.f2.grid(row = 1, sticky = W)
        self.f3 = tk.Frame(self.addwin)
        self.f3.grid(row = 2, sticky = W)
        self.f4 = tk.Frame(self.addwin) 
        self.f4.grid(row = 3, sticky = W)
        self.f5 = tk.Frame(self.addwin)
        self.f5.grid(row = 4)

        #Add employee label at top
        self.col = tk.Label(self.f1, text = "Add New Employee", bg = "Black", fg = "white")
        self.col.grid(row = 0, column = 1, pady = 35, sticky = W, ipadx = self.w/2, ipady = 15)
        self.col["font"] = times

        #Employee entry fields
        self.firstlab = tk.Label(self.f2, text = "First Name")
        self.firstlab.grid(row = 0, column = 0)
        self.firstlab["font"] = arial
        self.first = tk.Entry(self.f2, text = 30)
        self.first.grid(row = 0, column = 1, padx = 10)
        self.first['font'] = lucinda

        self.lastlab = tk.Label(self.f2, text = "Last Name")
        self.lastlab.grid(row = 0, column = 2, padx = 10)
        self.lastlab["font"] = arial
        self.last = tk.Entry(self.f2, text = 30)
        self.last.grid(row = 0, column = 3)
        self.last['font'] = lucinda

        self.idlab = tk.Label(self.f2, text = "Employee ID")
        self.idlab.grid(row = 1, column = 0, padx = 10, pady = 20)
        self.idlab["font"] = arial
        self.id = tk.Entry(self.f2, text = 30)
        self.id.grid(row = 1, column = 1)
        self.id['font'] = lucinda

        self.streetlab = tk.Label(self.f2, text = "Street Address")
        self.streetlab.grid(row =3, column = 0, padx = 10, pady = 20)
        self.streetlab["font"] = arial
        self.street = tk.Entry(self.f2, text = 30)
        self.street.grid(row = 3, column = 1)
        self.street['font'] = lucinda

        self.citylab = tk.Label(self.f2, text = "City")
        self.citylab.grid(row =3, column = 2, padx = 10)
        self.citylab["font"] = arial
        self.city = tk.Entry(self.f2, text = 30)
        self.city.grid(row = 3, column = 3)
        self.city['font'] = lucinda

        self.statelab = tk.Label(self.f2, text = "State")
        self.statelab.grid(row =3, column = 4, padx = 10)
        self.statelab["font"] = arial
        self.state = tk.Entry(self.f2, text = 30)
        self.state.grid(row = 3, column = 5)
        self.state['font'] = lucinda

        self.ziplab = tk.Label(self.f2, text = "Zip Code")
        self.ziplab.grid(row =3, column = 6, padx = 10)
        self.ziplab["font"] = arial
        self.zip = tk.Entry(self.f2, text = 30)
        self.zip.grid(row = 3, column = 7)
        self.zip['font'] = lucinda

        #selective buttons for employee payment delivery type
        self.i = IntVar() #links any radiobutton with the variable = i
        self.paymentlab = tk.Label(self.f3, text = "Select Payment Type:")
        self.paymentlab.grid(row = 0, column = 0, pady = 20, padx = 50)
        self.paymentlab["font"] = ubuntu
        self.depositbutton = tk.Radiobutton(self.f3, text = "Direct Deposit", value = 1, variable = self.i)
        self.depositbutton.grid(row = 1, column = 0, padx = 10)
        self.depositbutton["font"] = times1
        self.mailbutton = tk.Radiobutton(self.f3, text = "Mail", value = 2, variable = self.i)
        self.mailbutton.grid(row = 2, column = 0, padx = 10, pady = 5)
        self.mailbutton["font"] = times1

        #employee payment entry fields
        self.accountlab = tk.Label(self.f3, text = "Bank Account Number")
        self.accountlab.grid(row = 1, column = 2, padx = 20)
        self.accountlab["font"] = arial
        self.account = tk.Entry(self.f3, text = 30)
        self.account.grid(row = 1, column = 3)
        self.account["font"] = lucinda
        
        self.banklab = tk.Label(self.f3, text = "Bank Routing Number")
        self.banklab.grid(row = 1, column = 4, padx = 20)
        self.banklab["font"] = arial
        self.bank = tk.Entry(self.f3, text = 30)
        self.bank.grid(row = 1, column = 5)
        self.bank["font"] = lucinda

        #selective buttons for employee type
        self.v = IntVar() #links any radiobutton with the variable = v
        self.paymentlab = tk.Label(self.f4, text = "Select Employee Type:")
        self.paymentlab.grid(row = 0, column = 0, pady = 10, padx = 50)
        self.paymentlab["font"] = ubuntu
        self.mailbutton = tk.Radiobutton(self.f4, text = "Salary", value = 2, variable = self.v)
        self.mailbutton.grid(row = 1, column = 0, padx = 10, pady = 5)
        self.mailbutton["font"] = times1
        self.depositbutton = tk.Radiobutton(self.f4, text = "Hourly", value = 1, variable = self.v)
        self.depositbutton.grid(row = 2, column = 0, padx = 10)
        self.depositbutton["font"] = times1
        self.mailbutton = tk.Radiobutton(self.f4, text = "Commission", value = 2, variable = self.v)
        self.mailbutton.grid(row = 3, column = 0, padx = 10, pady = 5)
        self.mailbutton["font"] = times1

        #employee type entry fields
        self.salarylab = tk.Label(self.f4, text = "Annual Salary")
        self.salarylab.grid(row = 1, column = 4, padx = 20)
        self.salarylab["font"] = arial
        self.salary = tk.Entry(self.f4, text = 30)
        self.salary.grid(row = 1, column = 5)
        self.salary["font"] = lucinda

        self.Hourlylab = tk.Label(self.f4, text = "Hourly Rate")
        self.Hourlylab.grid(row = 2, column = 4, padx = 20, pady = 10)
        self.Hourlylab["font"] = arial
        self.Hourly = tk.Entry(self.f4, text = 30)
        self.Hourly.grid(row = 2, column = 5)
        self.Hourly["font"] = lucinda

        self.commlab = tk.Label(self.f4, text = "Comminssion Rate")
        self.commlab.grid(row = 3, column = 4, padx = 20)
        self.commlab["font"] = arial
        self.comm = tk.Entry(self.f4, text = 30)
        self.comm.grid(row = 3, column = 5)
        self.comm["font"] = lucinda

        self.submitbutton = tk.Button(self.f5, text = "Submit Changes")
        self.submitbutton.grid(row = 0, column = 0)
        self.submitbutton["font"] = arial2

        self.addwin.mainloop()

    def full(self):
        '''Makes the GUI fullSceen'''
        self.w, self.h = self.addwin.winfo_screenwidth(), self.addwin.winfo_screenheight()
        self.addwin.geometry("%dx%d" % (self.w, self.h))

        #self.fullScreenState = True
        #self.addwin.attributes("-fullscreen", self.fullScreenState)

        self.addwin.bind("<f>", self.toggle_fullscreen)
        self.addwin.bind("<Escape>", self.quit_fullscreen)



    def toggle_fullscreen(self, event):
        """if key <f> is pressed then window switches full screen on and off"""
        self.fullScreenState = not self.fullScreenState
        self.addwin.attributes("-fullscreen", self.fullScreenState)


    def quit_fullscreen(self, event):
        """if key <Escape> is pressed then window leaves fullscreen"""
        self.w, self.h = self.addwin.winfo_screenwidth(), self.addwin.winfo_screenheight()
        self.addwin.geometry("%dx%d" % (self.w, self.h))
        self.fullScreenState = False
        self.addwin.attributes("-fullscreen", self.fullScreenState)



class SearchEmployee:
    pass

def main():
    """instantiate and pop up the window."""
    
    MainPage()
    #FullScreen(tk.Tk())
    #AddNewEmp()

if __name__ == "__main__":
    main()
    
