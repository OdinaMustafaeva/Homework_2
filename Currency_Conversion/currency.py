# Imports
import json
import requests
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, Label, Entry, Button, StringVar, ttk, END

# Key and URl
KEY = "BTKV3uhi07DRpb8foxJ028Sgs7fcNO80qHLUnf9T"

url = f"https://api.freecurrencyapi.com/v1/latest"

resp = requests.get(
    url,
    params={"apikey": KEY}
)
currency = json.dumps(resp.json())
currency_read = json.loads(currency)

# Key country
keys = list(dict(currency_read)['data'].keys())

# Tk window
wn = tk.Tk()
# Window style
wn.title("Currency")
wn.geometry("400x300")
wn.configure(bg='limegreen')

# Money
label_money = Label(wn, text='Money', fg='green', bg='limegreen', font=(11))
label_money.grid(row=0, column=0)

# Money Entry
entry_money = Entry(wn, bg='white', fg='black', borderwidth=4)
entry_money.grid(row=0, column=2)

# Country name one
label_country_name_one = Label(wn, text='money  Country', bg='limegreen', fg='black')
label_country_name_one.grid(row=5, column=0, pady=20)

# Country Combobox one
combobox_country_one = ttk.Combobox(wn, values=keys, background='yellow')
combobox_country_one.grid(row=5, column=2, pady=20)

# Country name two
label_country_name_two = Label(wn, text='to Country  money', bg='limegreen', fg='black')
label_country_name_two.grid(row=8, column=0, pady=20)

# Country Combobox two
combobox_country_two = ttk.Combobox(wn, values=keys, background='yellow')
combobox_country_two.grid(row=8, column=2, pady=20)


# funk name
def know_money():
    try:
        money_one = float(dict(currency_read['data']).get(f"{combobox_country_one.get()}"))
        money_two = float(dict(currency_read['data']).get(f"{combobox_country_two.get()}"))
        solve_money = float(entry_money.get())
    except TypeError:
        messagebox.showerror("NameError", "check your info one more time!")
    else:
        all_math = money_two / money_one * solve_money
        enter_money = Label(wn, text=f"{float(all_math)}", font=(13), bg='limegreen', fg='red')
        enter_money.grid(row=20, column=0)
        entry_money.delete(0, END)


# Go button
go_Button = Button(wn, text='Enter', bg='Yellow', fg='Black', width=10, command=know_money)
go_Button.grid(row=10, column=6, pady=20, padx=50)

# Main run
if __name__ == '__main__':
    wn.mainloop()
