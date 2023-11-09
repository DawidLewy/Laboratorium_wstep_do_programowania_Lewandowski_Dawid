#Zad1
#1)
# wiek = int(input("Podaj swój wiek: "))
#
# if wiek < 4:
#     print("Cena biletu: 0zł")
# elif (wiek >= 4) and (wiek <= 18):
#     print("Cena biletu: 10zł")
# elif wiek > 18:
#     print("Cena biletu: 20zł")


#2)
# litera = input("Podaj litere: ")
#
# if litera.islower():
#     print("Litera jest mała")
# elif not litera.islower():
#     print("Litera jest duża")


#3)
# print("Jaką operacje chcesz wykonać?")
# print("1) Dodawanie")
# print("2) Odejmowanie")
# print("3) Mnożenie")
# print("4) Dzielenie")
# print("5) Potęgowanie")
# opcja = int(input("Wypisz numer operacji: "))
# x = int(input("Podaj argument 1: "))
# y = int(input("Podaj argument 2: "))
#
# if opcja == 1:
#     print(f"Wynik: {x + y}")
# elif opcja == 2:
#     print(f"Wynik: {x - y}")
# elif opcja == 3:
#     print(f"Wynik: {x * y}")
# elif opcja == 4:
#     print(f"Wynik: {x / y}")
# elif opcja == 5:
#     print(f"Wynik: {x ** y}")


#4)
# import math
#
# a = int(input("Podaj współczynnik a: "))
# b = int(input("Podaj współczynnik b: "))
# c = int(input("Podaj współczynnik c: "))
#
# #Aby obliczyć równanie a*x^2 + b*x + c = 0, musimy najpierw obliczyć deltę, a później wyznaczyć z niej miejsca zerowe(czyli nasze x)
#
# delta = b**2 - 4*a*c
# #Ma 2 rozwiązania
# if delta > 0:
#     pierwiastek_delta = math.sqrt(delta)
#     print(delta)
#     print(pierwiastek_delta)
#     x1 = (-b - pierwiastek_delta) / float(2*a)
#     x2 = (-b + pierwiastek_delta) / float(2*a)
#     print(f"Rozwiązaniami tego równania kwadratowego są: x1: {x1} lub x2: {x2}")
# #Ma 1 rozwiązanie
# elif delta == 0:
#     x = -b / float(2*a)
#     print(f"Rozwiązaniem tego równania kwadratoego jest x: {x}")
# #Nie ma rozwiązań
# elif delta < 0:
#     print("To równanie kwadratowe nie ma rozwiązań")

#5)
# x = int(input("Podaj x: "))
# y = int(input("Podaj y: "))
# z = int(input("Podaj z: "))
#
#
# print(x, y, z)
#
# if x > y:
#     x, y = y, x
#
# if y > z:
#     y, z = z, y
#
# if x > y:
#     x, y = y, x
#
# print(x, y, z)

############################################
#Zadania dodatkowe

#Zad 1

#a)
# x > 0 => a(x) = 2x
# x = 0 => a(x) = 0
# x < 0 => a(x) = -3x
# x podaje użytkownik, y-wartość funkcji dla podanego x

# x = int(input("Podaj liczbę: "))
#
# if x > 0:
#     y = 2 * x
# elif x == 0:
#     y = 0
# elif x < 0:
#     y = -3 * x
#
# print(f"Wartość funkcji dla podanego x wynsoi: {y}")

#b)
# x >= 1 => y = x**2
# x < 1 => y = x
# y - wartość funkcji

# x = int(input("Podaj wartość x: "))
#
# if x >= 1:
#     y = x**2
# elif x < 1:
#     y = x
#
# print(y)

#c)

# x = int(input("Podaj wartość x: "))
#
# if x > 2:
#     y = 2 + x
# elif x == 2:
#     y = 8
# elif x < 2:
#     y = x - 4
#
# print(y)

#Zad2

# print("Zdanie logiczne p - Czy pada deszcz? ")
# print("Zdanie ligiczne q - Czy jest autobus na przystanku? ")
# p = bool(int(input("Podaj wartość logiczną p(w postaci 0 lub 1): ")))
# q = bool(int(input("Podaj wartość logiczną q(w postaci 0 lub 1: ")))
#
# if p and q:
#     print("Weź parasol. Dostaniesz się na uczelnie.")
# elif p and not q:
#     print("Nie dostaniesz się na uczelnię.")
# elif not p and q:
#     print("Dostaniesz się na uczelnię. Miłego dnia i pięknej pogody.")


#Zad 3

# letter = input("Podaj literę: ")
#
# if letter.islower():
#     letter = letter.upper()
# elif not letter.islower():
#     letter = letter.lower()
#
# print(letter)