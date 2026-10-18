import random
import tkinter as tk
from tkinter import messagebox


def dobas():
    try:
        darab = int(darab_bevitel.get())
    except ValueError:
        messagebox.showerror('Hiba', 'Nem számot adtál meg!')
        return

    if darab < 1:
        messagebox.showerror('Hiba', 'Legalább 1 dobást adj meg!')
        return

    eredmenyek = {i: 0 for i in range(1, 7)}
    for _ in range(darab):
        eredmenyek[random.randint(1, 6)] += 1

    szoveg = ''
    for i in range(1, 7):
        szoveg += f'{i}-es = {eredmenyek[i]} db\n'
    dobas_eredmenye.config(text=szoveg)


ablak = tk.Tk()
ablak.title('Kockázás')
ablak.geometry('520x380')

cim = tk.Label(ablak, text='Kockajáték', font=('Arial', 16, 'bold'))
cim.pack(pady=10)

keret = tk.Frame(ablak)
keret.pack(fill='x', padx=60, pady=10)

darab_bevitel = tk.Entry(keret, width=12)
darab_bevitel.insert(0, '50')
darab_bevitel.pack(side='left')

kilepes_gomb = tk.Button(keret, text='Kilépés', width=10, command=ablak.destroy)
kilepes_gomb.pack(side='right')

dobas_gomb = tk.Button(keret, text='Dobás', width=10, command=dobas)
dobas_gomb.pack(side='right', padx=20)

dobas_eredmenye = tk.Label(ablak, text='', font=('Arial', 14, 'bold'), justify='left')
dobas_eredmenye.pack(pady=15)

ablak.mainloop()
