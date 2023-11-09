
import random
import math


#Zad 1
# print(type(1 + 2)) #<-- Zwraca int
# print(type(1 + 4.5)) #<-- Zwraca float
# print(type(3 / 2)) #<-- Zwraca float
# print(type(4 / 2)) #<-- Zwraca float
# print(type(3 // 2)) #<-- Zwraca int, bez reszty z dzielenia
# print(type(-3 // 2)) #<-- Zwraca int ujemny
# print(type(11 % 2)) #<-- Zwraca int, jest to reszta z dzielenia
# print(type(2 ** 10)) #<-- Zwraca int, jest to potęgowanie 2^10
# print(type(8 ** (1/3))) #<-- Zwraca float, jest to potęgowanie od ułamka liczby 1/3, czyli inaczej pierwiastek 3 stopnia z 8


#Zad 2
# int(3.0) <-- Zamienia liczbę typu float(liczbę zmienno-przecinkową) na int(liczbę całkowitą)
# float(3) <-- Zamienia liczbę typu int(liczbę całkowitą) na float(liczbę zmienno-przecinkową)
# float("3") <-- Zamienia stringa(tekst) na floata(liczbę zmienno-przecinkową)
# str(12.4) <-- Zamienia floata(liczbę zmienno-przecinkową) na stringa(tekst)
# bool(0) <-- Zamienia liczbę(lub tekst) na wartość logiczną True lub False, w tym przypadku zamieni 0 na False. (Każda liczba większa od 0 da wartość True, a 0 daje False)(Każdy string, który nie jest pusty(np. "Hej"), da wartość True, natomiast pusty string("") daje wartość 0)


# Zad 3
# x = float(input("Podaj długość 1 boku: "))
# y = float(input("Podaj długość 2 boku: "))
# z = x * y
# obwod = (2 * x) + (2 * y)
# print(f"Pole prostokąta wynosi: {z}")
# print(f"Obwód wynosi: {obwod}")

#Zad 4
# s = int(input("Podaj drogę do pokonania mierzoną w km: "))

#Zad 4.1
# s = random.randint(1, 100000)
# spalanie = int(input("Podaj średnie spalanie: "))
# cena = 6.5
# zuzycie = (spalanie * s) / 100
# koszty = cena * zuzycie
# print(f"Przewidywane koszty: {koszty:.2f} zł")
# print(f"Przewidywane zużycie paliwa: {zuzycie:.2f} litrów")


#Zad 5
# Zrobione powyżej

#Zadanie dodatkowe

#Zad1
# a = int(input("Podaj wartość a: "))
# b = int(input("Podaj wartość b: "))
# #Rownanie : 0 = ax + b
# x = -b / a
#
# print(f"Rozwiązaniem funkcji liniowej jest x równy: {x:.2f}") #<-- Wynik w postaci l. dziesięten z 2 miejscami po przecinku
# print(f"Rozwiązaniem funkcji liniowej jest x równy: -{b}/{a}") #<-- Wynik w postaci ułamka
#
#
# # Zad 2
# a = int(input("Podaj a: "))
# b = int(input("Podaj b: "))
# c = int(input("Podaj c: "))
# p = (a + b + c) / 2
#
# Pole = math.sqrt(p*(p - a)*(p - b)*(p - c))
#
# print(f"Pole trojkata: {Pole:.2f}")
#
# #Zad 3
# x = int(input("Podaj 1 liczbe: "))
# y = int(input("Podaj 2 liczbe: "))
#
# print(f"Dodawanie: {x + y}")
# print(f"Odejmowanie: {x - y}")
# print(f"Mnożenie: {x * y}")
# print(f"Dzielenie: {x / y}")