from currency_converter import CurrencyConverter
from tkinter import *
import time
def exchange():
    e_eur.delete(0, END)
    e_gbp.delete(0, END)
    e_jpy.delete(0, END)
    e_aud.delete(0, END)
    e_cad.delete(0, END)
    e_cny.delete(0, END)
    e_czk.delete(0, END)
    e_try.delete(0, END)
    e_eur.insert(0, '%.2f' %c.convert(e_usd.get(), 'EUR', 'USD'))
    e_gbp.insert(0, '%.2f' %c.convert(e_usd.get(), 'GBP', 'USD'))
    e_jpy.insert(0, '%.2f' % c.convert(e_usd.get(), 'JPY', 'USD'))
    e_aud.insert(0, '%.2f' % c.convert(e_usd.get(), 'AUD', 'USD'))
    e_cad.insert(0, '%.2f' % c.convert(e_usd.get(), 'CAD', 'USD'))
    e_cny.insert(0, '%.2f' % c.convert(e_usd.get(), 'CNY', 'USD'))
    e_czk.insert(0, '%.2f' % c.convert(e_usd.get(), 'CZK', 'USD'))
    e_try.insert(0, '%.2f' % c.convert(e_usd.get(), 'TRY', 'USD'))

time.sleep(2)

root = Tk()
root.title('Конвертер валют')
root.geometry('350x450+580+180')
root.resizable(width=False, height=False)
root['bg'] = 'black'
c = CurrencyConverter()

header_frame = Frame(root)
header_frame.pack(fill=X)

header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=1)
header_frame.grid_columnconfigure(2, weight=1)

h_currency = Label(header_frame, text='Валюта', bg='green', fg='black', font='Arial 12 bold')
h_currency.grid(row=0, column=0, sticky=EW)
h_course = Label(header_frame, text='Курс', bg='green', fg='black', font='Arial 12 bold')
h_course.grid(row=0, column=1, columnspan=2, sticky=EW)

# EUR курс
eur_currency = Label(header_frame, text='EUR', font='Arial 10')
eur_currency.grid(row=1, column=0, sticky=EW)
eur_one = Label(header_frame, text='1', font='Arial 10')
eur_one.grid(row=1, column=1, sticky=EW)
eur_converted = Label(header_frame, text='%.2f' % c.convert(1, 'EUR', 'USD'), font='Arial 10')
eur_converted.grid(row=1, column=2, sticky=EW)

# GBP курс
gbp_currency = Label(header_frame, text='GBP', font='Arial 10')
gbp_currency.grid(row=2, column=0, sticky=EW)
gbp_one = Label(header_frame, text='1', font='Arial 10')
gbp_one.grid(row=2, column=1, sticky=EW)
gbp_converted = Label(header_frame, text='%.2f' % c.convert(1, 'GBP', 'USD'), font='Arial 10')
gbp_converted.grid(row=2, column=2, sticky=EW)

# JPY курс
jpy_currency = Label(header_frame, text='JPY', font='Arial 10')
jpy_currency.grid(row=3, column=0, sticky=EW)
jpy_one = Label(header_frame, text='1', font='Arial 10')
jpy_one.grid(row=3, column=1, sticky=EW)
jpy_converted = Label(header_frame, text='%.2f' % c.convert(1, 'JPY', 'USD'), font='Arial 10')
jpy_converted.grid(row=3, column=2, sticky=EW)

# AUD курс
aud_currency = Label(header_frame, text='AUD', font='Arial 10')
aud_currency.grid(row=4, column=0, sticky=EW)
aud_one = Label(header_frame, text='1', font='Arial 10')
aud_one.grid(row=4, column=1, sticky=EW)
aud_converted = Label(header_frame, text='%.2f' % c.convert(1, 'AUD', 'USD'), font='Arial 10')
aud_converted.grid(row=4, column=2, sticky=EW)

# CAD курс
cad_currency = Label(header_frame, text='CAD', font='Arial 10')
cad_currency.grid(row=5, column=0, sticky=EW)
cad_one = Label(header_frame, text='1', font='Arial 10')
cad_one.grid(row=5, column=1, sticky=EW)
cad_converted = Label(header_frame, text='%.2f' % c.convert(1, 'CAD', 'USD'), font='Arial 10')
cad_converted.grid(row=5, column=2, sticky=EW)

# CNY курс
cny_currency = Label(header_frame, text='CNY', font='Arial 10')
cny_currency.grid(row=6, column=0, sticky=EW)
cny_one = Label(header_frame, text='1', font='Arial 10')
cny_one.grid(row=6, column=1, sticky=EW)
cny_converted = Label(header_frame, text='%.2f' % c.convert(1, 'CNY', 'USD'), font='Arial 10')
cny_converted.grid(row=6, column=2, sticky=EW)

# CZK курс
czk_currency = Label(header_frame, text='CZK', font='Arial 10')
czk_currency.grid(row=8, column=0, sticky=EW)
czk_one = Label(header_frame, text='1', font='Arial 10')
czk_one.grid(row=8, column=1, sticky=EW)
czk_converted = Label(header_frame, text='%.2f' % c.convert(1, 'CZK', 'USD'), font='Arial 10')
czk_converted.grid(row=8, column=2, sticky=EW)

# TRY курс
try_currency = Label(header_frame, text='TRY', font='Arial 10')
try_currency.grid(row=10, column=0, sticky=EW)
try_one = Label(header_frame, text='1', font='Arial 10')
try_one.grid(row=10, column=1, sticky=EW)
try_converted = Label(header_frame, text='%.2f' % c.convert(1, 'TRY', 'USD'), font='Arial 10')
try_converted.grid(row=10, column=2, sticky=EW)

calc_frame = Frame(root, bg='white')
calc_frame.pack(expand=1, fill=BOTH)
calc_frame.grid_columnconfigure(1, weight=1)

# USD
l_usd = Label(calc_frame, text='Долларов: ', bg='white', fg='black', font='Arial 12 bold')
l_usd.grid(row=0, column=0, padx=10)
e_usd = Entry(calc_frame, justify=CENTER, font='Arial 10')
e_usd.grid(row=0, column=1, columnspan=2, pady=10, padx=10, sticky=EW)

button_calc = Button(calc_frame, text='Конвертировать', command=exchange)
button_calc.grid(row=1, column=1, columnspan=2, sticky=EW, padx=10)

result_frame = Frame(root)
result_frame.pack(expand=1, fill=BOTH, pady=5)
result_frame.grid_columnconfigure(1, weight=1)

# EUR
l_eur = Label(result_frame, text='EUR', font='Arial 10 bold')
l_eur.grid(row=2, column=0)
e_eur = Entry(result_frame, justify=CENTER, font='Arial 10')
e_eur.grid(row=2, column=1, columnspan=2, padx=10, sticky=EW)

# GBP
l_gbp = Label(result_frame, text='GBP', font='Arial 10 bold')
l_gbp.grid(row=3, column=0)
e_gbp = Entry(result_frame, justify=CENTER, font='Arial 10')
e_gbp.grid(row=3, column=1, columnspan=2, padx=10, sticky=EW)

# JPY
l_jpy = Label(result_frame, text='JPY', font='Arial 10 bold')
l_jpy.grid(row=4, column=0)
e_jpy = Entry(result_frame, justify=CENTER, font='Arial 10')
e_jpy.grid(row=4, column=1, columnspan=2, padx=10, sticky=EW)

# AUD
l_aud = Label(result_frame, text='AUD', font='Arial 10 bold')
l_aud.grid(row=4, column=0)
e_aud = Entry(result_frame, justify=CENTER, font='Arial 10')
e_aud.grid(row=4, column=1, columnspan=2, padx=10, sticky=EW)

# CAD
l_cad = Label(result_frame, text='CAD', font='Arial 10 bold')
l_cad.grid(row=5, column=0)
e_cad = Entry(result_frame, justify=CENTER, font='Arial 10')
e_cad.grid(row=5, column=1, columnspan=2, padx=10, sticky=EW)

# CNY
l_cny = Label(result_frame, text='CNY', font='Arial 10 bold')
l_cny.grid(row=6, column=0)
e_cny = Entry(result_frame, justify=CENTER, font='Arial 10')
e_cny.grid(row=6, column=1, columnspan=2, padx=10, sticky=EW)

# CZK
l_czk = Label(result_frame, text='CZK', font='Arial 10 bold')
l_czk.grid(row=8, column=0)
e_czk = Entry(result_frame, justify=CENTER, font='Arial 10')
e_czk.grid(row=8, column=1, columnspan=2, padx=10, sticky=EW)

# TRY
l_try = Label(result_frame, text='TRY', font='Arial 10 bold')
l_try.grid(row=10, column=0)
e_try = Entry(result_frame, justify=CENTER, font='Arial 10')
e_try.grid(row=10, column=1, columnspan=2, padx=10, sticky=EW)

root.mainloop()
