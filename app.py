from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from fraktale import *
from turtle import *

root = Tk()
root.title("Fraktale")
root.geometry("800x600")

style = ttk.Style(root)
root.tk.call('source', 'azure-dark.tcl')
style.theme_use('azure-dark')

title = ttk.Label(root, text="FRAKTALE", anchor="center", font="Calibri 42")
title.grid(row=0, column=2, columnspan=2, ipady=30)

sw = BooleanVar()
rodzaj = IntVar()


def checkradiobuttons():
    if rodzaj.get() == 0:
        messagebox.showerror("BRAK DANYCH!", "Nic nie zaznaczyłeś!")
        return False
    else:
        return True


def switchfunction():
    if sw.get():
        switch.config(text='ON')
        penup()
        hideturtle()
        clear()
    else:
        switch.config(text='OFF')
        penup()
        hideturtle()
        clear()


def vartracer():
    if sw.get():
        return False
    else:
        return True


def start():
    penup()
    tracer(False)
    goto(0, 0)
    pendown()
    clear()
    setheading(180)
    showturtle()
    speed(float(spinbox.get()))

    if checkradiobuttons():
        if rodzaj.get() == 1:
            dlugosc = 5
            stopien = 12
            if dlugoscentry.get() != "" and stopienentry.get() != "":
                dlugosc = int(dlugoscentry.get())
                stopien = int(stopienentry.get())
            elif dlugoscentry.get() != "" and stopienentry.get() == "":
                dlugosc = int(dlugoscentry.get())
            elif dlugoscentry.get() == "" and stopienentry.get() != "":
                stopien = int(stopienentry.get())

            rysuj = Fraktale(dl=dlugosc, st=stopien)
            var = vartracer()
            tracer(var)
            rysuj.levy()

        elif rodzaj.get() == 2:
            dlugosc = 300
            stopien = 5
            if dlugoscentry.get() != "" and stopienentry.get() != "":
                dlugosc = int(dlugoscentry.get())
                stopien = int(stopienentry.get())
            elif dlugoscentry.get() != "" and stopienentry.get() == "":
                dlugosc = int(dlugoscentry.get())
            elif dlugoscentry.get() == "" and stopienentry.get() != "":
                stopien = int(stopienentry.get())

            rysuj = Fraktale(dl=dlugosc, st=stopien)
            var = vartracer()
            tracer(var)
            rysuj.sierpinski("trojkat")

        elif rodzaj.get() == 3:
            dlugosc = 300
            stopien = 3
            if dlugoscentry.get() != "" and stopienentry.get() != "":
                dlugosc = int(dlugoscentry.get())
                stopien = int(stopienentry.get())
            elif dlugoscentry.get() != "" and stopienentry.get() == "":
                dlugosc = int(dlugoscentry.get())
            elif dlugoscentry.get() == "" and stopienentry.get() != "":
                stopien = int(stopienentry.get())

            rysuj = Fraktale(dl=dlugosc, st=stopien)
            var = vartracer()
            tracer(var)
            rysuj.sierpinski("dywan")

        elif rodzaj.get() == 4:
            dlugosc = 100
            stopien = 4
            if dlugoscentry.get() != "" and stopienentry.get() != "":
                dlugosc = int(dlugoscentry.get())
                stopien = int(stopienentry.get())
            elif dlugoscentry.get() != "" and stopienentry.get() == "":
                dlugosc = int(dlugoscentry.get())
            elif dlugoscentry.get() == "" and stopienentry.get() != "":
                stopien = int(stopienentry.get())

            rysuj = Fraktale(dl=dlugosc, st=stopien)
            var = vartracer()
            tracer(var)
            rysuj.cantor()

        elif rodzaj.get() == 5:
            dlugosc = 100
            stopien = 6
            if dlugoscentry.get() != "" and stopienentry.get() != "":
                dlugosc = int(dlugoscentry.get())
                stopien = int(stopienentry.get())
            elif dlugoscentry.get() != "" and stopienentry.get() == "":
                dlugosc = int(dlugoscentry.get())
            elif dlugoscentry.get() == "" and stopienentry.get() != "":
                stopien = int(stopienentry.get())

            rysuj = Fraktale(dl=dlugosc, st=stopien)
            var = vartracer()
            tracer(var)
            rysuj.drzewo_rek()

        elif rodzaj.get() == 6:
            dlugosc = 100
            stopien = 6
            if dlugoscentry.get() != "" and stopienentry.get() != "":
                dlugosc = int(dlugoscentry.get())
                stopien = int(stopienentry.get())
            elif dlugoscentry.get() != "" and stopienentry.get() == "":
                dlugosc = int(dlugoscentry.get())
            elif dlugoscentry.get() == "" and stopienentry.get() != "":
                stopien = int(stopienentry.get())

            rysuj = Fraktale(dl=dlugosc, st=stopien)
            var = vartracer()
            tracer(var)
            rysuj.platek()

        elif rodzaj.get() == 7:
            dlugosc = 5
            stopien = 12
            if dlugoscentry.get() != "" and stopienentry.get() != "":
                dlugosc = int(dlugoscentry.get())
                stopien = int(stopienentry.get())
            elif dlugoscentry.get() != "" and stopienentry.get() == "":
                dlugosc = int(dlugoscentry.get())
            elif dlugoscentry.get() == "" and stopienentry.get() != "":
                stopien = int(stopienentry.get())

            rysuj = Fraktale(dl=dlugosc, st=stopien)
            var = vartracer()
            tracer(var)
            rysuj.krzywa_smoka()


# RAMKA PARAMETRY
parametry = ttk.LabelFrame(root, height=350, width=175, text="PARAMETRY:")
parametry.grid(row=1, column=1, ipadx=10)

pustemiejsce1 = Label()
pustemiejsce1.grid(row=0, column=0, ipadx=40)
pustemiejsce2 = Label()
pustemiejsce2.grid(row=2, column=2, ipadx=50)
pustemiejsce3 = Label()
pustemiejsce3.grid(row=2, column=5, ipadx=50)

dlugosctext = ttk.Label(parametry, text="DLUGOSC", font="Calibri 11")
dlugosctext.grid(row=0, pady=5, column=1)
dlugoscentry = ttk.Entry(parametry, justify="center")
dlugoscentry.grid(row=1, column=1)

pustepole1 = Label(parametry)
pustepole1.grid(row=0, column=0, padx=10)
pustepole2 = Label(parametry)
pustepole2.grid(row=2, column=1, pady=5)
stopientext = Label(parametry, text="STOPIEN", font="Calibri 11")
stopientext.grid(row=3, column=1)
stopienentry = ttk.Entry(parametry, justify="center")
stopienentry.grid(row=4, column=1)

pustepole3 = Label(parametry)
pustepole3.grid(row=5, pady=5, column=1)

spinboxtext = Label(parametry, text="SZYBKOSC", font="Calibri 11")
spinboxtext.grid(row=6, column=1)
spinbox = ttk.Spinbox(parametry, from_=0.5, to=10.5, increment=0.5)
spinbox.insert(0, '0')
spinbox.grid(row=7, column=1)

pustepole4 = Label(parametry)
pustepole4.grid(row=8, column=1)

animacjetext = Label(parametry, text="POMIN ANIMACJE", font="Calibri 11")
animacjetext.grid(row=9, column=1)
switch = ttk.Checkbutton(parametry, text="ON", style="Switch", variable=sw)
switch.grid(row=10, column=1)
switch.invoke()
switch.config(command=switchfunction)
pustepole5 = Label(parametry)
pustepole5.grid(row=11)

# RAMKA FRAKTALE
wyborfraktali = ttk.LabelFrame(root, height=350, width=400, text="WYBIERZ FRAKTAL: ")
wyborfraktali.grid(row=1, column=3, columnspan=2, rowspan=3)

pustepole6 = Label(wyborfraktali, width=30)
pustepole6.grid(row=0, pady=3, padx=50)
pustepole7 = Label(wyborfraktali)
pustepole7.grid(row=2, pady=3, padx=50)
pustepole8 = Label(wyborfraktali)
pustepole8.grid(row=4, pady=3, padx=50)
pustepole9 = Label(wyborfraktali)
pustepole9.grid(row=6, pady=3, padx=50)
pustepole10 = Label(wyborfraktali)
pustepole10.grid(row=8, pady=3, padx=50)
pustepole11 = Label(wyborfraktali)
pustepole11.grid(row=10, pady=3, padx=50)
pustepole12 = Label(wyborfraktali)
pustepole12.grid(row=12, pady=3, padx=50)
pustepole13 = Label(wyborfraktali)
pustepole13.grid(row=14, pady=3, padx=50)

levy = ttk.Radiobutton(wyborfraktali, text="1 - Krzywa Lévy’ego", variable=rodzaj, value=1)
levy.grid(row=1, sticky="n")
sierptroj = ttk.Radiobutton(wyborfraktali, text="2 - Trójkąt Sierpińskiego", variable=rodzaj, value=2)
sierptroj.grid(row=3, sticky="n")
sierpdyw = ttk.Radiobutton(wyborfraktali, text="3 - Dywan Sierpińskiego", variable=rodzaj, value=3)
sierpdyw.grid(row=5, sticky="n")
cantor = ttk.Radiobutton(wyborfraktali, text="4  -  Zbiór Cantora", variable=rodzaj, value=4)
cantor.grid(row=7, sticky="n")
drzewo = ttk.Radiobutton(wyborfraktali, text="5 - Drzewo rekurencyjne", variable=rodzaj, value=5)
drzewo.grid(row=9, sticky="n")
platek = ttk.Radiobutton(wyborfraktali, text="6  -  Płatek Kocha", variable=rodzaj, value=6)
platek.grid(row=11, sticky="n")
smok = ttk.Radiobutton(wyborfraktali, text="7  -  Krzywa smoka", variable=rodzaj, value=7)
smok.grid(row=13, sticky="n")

# Przycisk rysuj
pustemiejsce4 = Label(root)
pustemiejsce4.grid(row=2, column=1)
rysujtext = ttk.LabelFrame(root, text="RYSUJ:", width=135, height=85)
rysujtext.grid(row=3, column=1)
start = ttk.Button(rysujtext, text='START', style='AccentButton', command=start)
start.grid(row=3, column=1)

root.mainloop()
mainloop()
