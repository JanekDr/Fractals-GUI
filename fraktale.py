from turtle import *
from math import sqrt


class Fraktale:
    def __init__(self, st, dl):
        self.st = st
        self.dl = dl

    def levy(self):
        penup()
        goto(100, 100)
        pendown()

        def krzywa_levego(st, dl):
            if st == 0:
                forward(dl)
                return
            else:
                left(45)
                krzywa_levego(st - 1, dl)
                right(90)
                krzywa_levego(st - 1, dl)
                left(45)

        krzywa_levego(self.st, self.dl)

    def sierpinski(self, typ):

        def trojkat(x, y, dl):
            up()
            goto(x, y)
            down()
            goto(x + dl, y)
            goto(x + dl / 2, y + dl * sqrt(3) / 2)
            goto(x, y)

        def kwadrat(x, y, dl):
            up()
            goto(x, y)
            down()
            goto(x + dl, y)
            goto(x + dl, y + dl)
            goto(x, y + dl)
            goto(x, y)

        def trojkat_sierp(x, y, dl, st):
            if st == 1:
                trojkat(x, y, dl)
                return
            trojkat(x, y, dl)
            trojkat_sierp(x, y, dl / 2, st - 1)
            trojkat_sierp(x + dl / 2, y, dl / 2, st - 1)
            trojkat_sierp(x + dl / 4, y + dl * sqrt(3) / 4, dl / 2, st - 1)
            penup()

        def dywan(x, y, dl, st):
            if st == 0:
                kwadrat(x, y, dl)
                return
            kwadrat(x, y, dl)
            dywan(x, y, dl / 3, st - 1)
            dywan(x + dl / 3, y, dl / 3, st - 1)
            dywan(x + dl * 2 / 3, y, dl / 3, st - 1)
            dywan(x + dl * 2 / 3, y + dl / 3, dl / 3, st - 1)
            dywan(x + dl * 2 / 3, y + dl * 2 / 3, dl / 3, st - 1)
            dywan(x + dl / 3, y + dl * 2 / 3, dl / 3, st - 1)
            dywan(x, y + dl * 2 / 3, dl / 3, st - 1)
            dywan(x, y + dl / 3, dl / 3, st - 1)
            penup()

        if typ == "dywan":
            dywan(-150, -100, self.dl, self.st)
        else:

            trojkat_sierp(-150, -100, self.dl, self.st)

    def cantor(self):

        def rys_linie(x1, y1, x2, y2):
            up()
            goto(x1, y1)
            down()
            goto(x2, y2)

        def zbior_cantora(st, x1, y1, dl):
            if st == 0:
                return
            else:
                x2, y2 = x1 + dl / 3, y1
                rys_linie(x1, y1, x2, y2)
                zbior_cantora(st - 1, x1, y1 - 50, dl / 3)
                zbior_cantora(st - 1, x1 + 2 * dl / 3, y1 - 50, dl / 3)
                rys_linie(x1, y1, x2 + 2 * dl / 3, y2)
                penup()

        zbior_cantora(self.st, -100, 50, self.dl)

    def drzewo_rek(self):
        left(90)

        def drzewo(dl, st, kat):
            if st == 0:
                color("green")
                dot(5)
                color("black")
                return
            forward(dl)
            right(kat)
            drzewo(dl * 0.8, st - 1, kat)
            left(2 * kat)
            drzewo(dl * 0.8, st - 1, kat)
            right(kat)
            backward(dl)

        drzewo(self.dl, self.st, 30)

    def platek(self):

        def platek_kocha(dl, step):
            if step == 0:
                forward(dl)
                return
            else:
                dl /= 3
                platek_kocha(dl, step-1)
                left(60)
                platek_kocha(dl, step-1)
                right(120)
                platek_kocha(dl, step-1)
                left(60)
                platek_kocha(dl, step-1)

        for i in range(4):
            platek_kocha(self.dl, self.st)
            right(90)

    def krzywa_smoka(self):

        def krzywa(st, dl, strona):
            if st == 0:
                forward(dl)
                return
            else:
                left(45 * strona)
                krzywa(st - 1, dl, -1)
                right(90 * strona * -1)
                krzywa(st - 1, dl, 1)
                left(45 * strona)
        krzywa(self.st, self.dl, 1)


