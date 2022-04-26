from fraktale import *

print("#" * 50)
print("#" + " " * 10 + "1 - Krzywa Lévy’ego" + " " * (53 - len("1 - Krzywa Lévy’ego") - 15) + "#")
print("#" + " " * 10 + "2 - Trójkąt Sierpińskiego" + " " * (53 - len("2 - Trójkąt Sierpińskiego") - 15) + "#")
print("#" + " " * 10 + "3 - Dywan Sierpińskiego" + " " * (53 - len("3 - Dywan Sierpińskiego") - 15) + "#")
print("#" + " " * 10 + "4 - Zbiór Cantora" + " " * (53 - len("4 - Zbiór Cantora") - 15) + "#")
print("#" + " " * 10 + "5 - Drzewo rekurencyjne" + " " * (53 - len("5 - Drzewo rekurencyjne") - 15) + "#")
print("#" + " " * 10 + "6 - Płatek Kocha" + " " * (53 - len("6 - Płatek Kocha") - 15) + "#")
print("#" + " " * 10 + "7 - Krzywa smoka" + " " * (53 - len("7 - Krzywa smoka") - 15) + "#")
print("#" * 50)

wybor = int(input("Wybierz fraktal: "))

tab = {1, 2, 3, 4, 5, 6, 7}

while wybor not in tab:
    wybor = int(input("Spróbuj ponownie: "))
    if wybor in tab:
        break

if wybor == 1:
    print("Wybrałeś Krzywą Lévy’ego!")
    print()
    parametry = input("Czy chcesz podac parametry? (y/n)")
    if input("Czy chcesz pominąć animacje(y/n)? ") == "y":
        tracer(False)

    if parametry == "y":
        dlugosc = int(input("Podaj długość (optymalna to 5): "))
        stopien = int(input("Podaj stopień (optymalny to 12): "))
        rysuj = Fraktale(dl=dlugosc, st=stopien)
        rysuj.levy()
    else:
        rysuj = Fraktale(dl=5, st=12)
        rysuj.levy()

elif wybor == 2:
    print("Wybrałeś Trójkąt Sierpińskiego!")
    print()
    parametry = input("Czy chcesz podac parametry? (y/n)")
    if input("Czy chcesz pominąć animacje(y/n)? ") == "y":
        tracer(False)

    if parametry == "y":
        dlugosc = int(input("Podaj długość (optymalna to 300): "))
        stopien = int(input("Podaj stopień (optymalny to 5): "))
        rysuj = Fraktale(dl=dlugosc, st=stopien)
        rysuj.sierpinski("trojkat")
    else:
        rysuj = Fraktale(dl=300, st=5)
        rysuj.sierpinski("trojkat")

elif wybor == 3:
    print("Wybrałeś Dywan Sierpińskiego!")
    print()
    parametry = input("Czy chcesz podac parametry? (y/n)")
    if input("Czy chcesz pominąć animacje(y/n)? ") == "y":
        tracer(False)

    if parametry == "y":
        dlugosc = int(input("Podaj długość (optymalna to 300): "))
        stopien = int(input("Podaj stopień (optymalny to 4): "))
        rysuj = Fraktale(dl=dlugosc, st=stopien)
        rysuj.sierpinski("dywan")
    else:
        rysuj = Fraktale(dl=300, st=4)
        rysuj.sierpinski("dywan")

elif wybor == 4:
    print("Wybrałeś zbiór Cantora!")
    print()
    parametry = input("Czy chcesz podac parametry? (y/n)")
    if input("Czy chcesz pominąć animacje(y/n)? ") == "y":
        tracer(False)

    if parametry == "y":
        dlugosc = int(input("Podaj długość (optymalna to 100): "))
        stopien = int(input("Podaj stopień (optymalny to 5): "))
        rysuj = Fraktale(dl=dlugosc, st=stopien)
        rysuj.cantor()
    else:
        rysuj = Fraktale(dl=300, st=4)
        rysuj.cantor()

elif wybor == 5:
    print("Wybrałeś drzewo rekurencyjne!")
    print()
    parametry = input("Czy chcesz podac parametry? (y/n)")
    if input("Czy chcesz pominąć animacje(y/n)? ") == "y":
        tracer(False)

    if parametry == "y":
        dlugosc = int(input("Podaj długość (optymalna to 100): "))
        stopien = int(input("Podaj stopień (optymalny to 6): "))
        rysuj = Fraktale(dl=dlugosc, st=stopien)
        rysuj.drzewo_rek()
    else:
        rysuj = Fraktale(dl=100, st=6)
        rysuj.drzewo_rek()

elif wybor == 6:
    print("Wybrałeś Płatek Kocha!")
    print()
    parametry = input("Czy chcesz podac parametry? (y/n)")
    if input("Czy chcesz pominąć animacje(y/n)? ") == "y":
        tracer(False)

    if parametry == "y":
        dlugosc = int(input("Podaj długość (optymalna to 100): "))
        stopien = int(input("Podaj stopień (optymalny to 6): "))
        rysuj = Fraktale(dl=dlugosc, st=stopien)
        rysuj.platek()
    else:
        rysuj = Fraktale(dl=100, st=6)
        rysuj.platek()

elif wybor == 7:
    print("Wybrałeś krzywą smoka!")
    print()
    parametry = input("Czy chcesz podac parametry? (y/n)")
    if input("Czy chcesz pominąć animacje(y/n)? ") == "y":
        tracer(False)

    if parametry == "y":
        dlugosc = int(input("Podaj długość (optymalna to 5): "))
        stopien = int(input("Podaj stopień (optymalny to 12): "))
        rysuj = Fraktale(dl=dlugosc, st=stopien)
        rysuj.krzywa_smoka()
    else:
        rysuj = Fraktale(dl=5, st=12)
        rysuj.krzywa_smoka()

mainloop()
