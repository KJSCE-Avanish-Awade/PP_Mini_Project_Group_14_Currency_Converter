##This is the main code file
from gettext import install
import pip


import tkinter as tk
from tkinter import *
import tkinter.messagebox

#GUI Starts from here
gui = tk.Tk()

gui.title("Currency Converter")

Tops = Frame(gui, bg = '#e6e5e5', pady=2, width=1850, height=100, relief="ridge")
Tops.grid(row=0, column=0)

headlabel = tk.Label(Tops, font=('lato black', 19, 'bold'), text='		Currency Converter',
					bg='#e6e5e5', fg='black')
headlabel.grid(row=1, column=0, sticky=W)

variable1 = tk.StringVar(gui)
variable2 = tk.StringVar(gui)

variable1.set("Currency")
variable2.set("Currency")

#Function To For Real Time Currency Conversion starts here

def RealTimeCurrencyConversion():
	from forex_python.converter import CurrencyRates
	c = CurrencyRates()

	from_currency = variable1.get()
	to_currency = variable2.get()

	if (Amount1_field.get() == ""):
		tkinter.messagebox.showinfo("Error !!", "Amount Not Entered.\n Please a valid amount.")

	elif (from_currency == "currency" or to_currency == "currency"):
		tkinter.messagebox.showinfo("Error !!",
									"Currency Not Selected.\n Please select FROM and TO Currency form menu.")
	else:
		new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
		new_amount = float("{:.4f}".format(new_amt))
		Amount2_field.insert(0, str(new_amount))

#clearing all the data entered by the user

def clear_all():
	Amount1_field.delete(0, tk.END)
	Amount2_field.delete(0, tk.END)

#GUI Layout
CurrenyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"]

gui.configure(background='#e6e5e5')
gui.geometry("700x440")

Label_1 = Label(gui, font=('lato black', 27, 'bold"), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=1, column=0, sticky=W)

label1 = tk.label(gui, font=('lato black', 15, 'bold'), text="\t Amount : ", bg="#e6e5e5", fg="black")
label1.grid(row=2, column=0, sticky=W)

label1 = tk.label(gui, font=('lato black', 15, 'bold'), text="\t From Currency : ", bg="#e6e5e5", fg="black")
label1.grid(row=3, column=0, sticky=w)
			   
label1 = tk.Label(gui, font=('lato black', 15, 'bold'), text="\t To Currency : ", bg="#e6e5e5", fg="black")
label1.grid(row=4, column=0, sticky=w)

label1 = tk.Label(gui, font=('lato black', 15, 'bold'), text="\t Converted", bg="#e6e5e5", fg="black")
label1.grid(row=8, column=0, sticky=W)

label1 = tk.Label(gui, font=('lato black', 15, 'bold'), text="\t Amount : ", bg="#e6e5e5", fg="black")
label1.grid(row=9, column=0, sticky=W)

Label_1 = Label(gui, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=5, column=0, sticky=W)
label1 = tk.Label(gui, font=('lato black', 15, 'bold'), text="\t To Currency : ", bg="#e6e5e5", fg="black")
label1.grid(row=4, column=0, sticky=W)

label1 = tk.Label(gui, font=('lato black', 15, 'bold'), text="\t Converted", bg="#e6e5e5", fg="black")
label1.grid(row=8, column=0, sticky=W)

label1 = tk.Label(gui, font=('lato black', 15, 'bold'), text="\t Amount : ", bg="#e6e5e5", fg="black")
label1.grid(row=9, column=0, sticky=W)

Label_1 = Label(gui, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=5, column=0, sticky=W)

Label_1 = Label(gui, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=7, column=0, sticky=W)
