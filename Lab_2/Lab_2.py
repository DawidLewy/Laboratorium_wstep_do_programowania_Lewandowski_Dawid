#Zad 1

import math
import random
##########################################################################
###Pętle while
##########################################################################
#Zad 1

# a = int(input("Podaj 1 liczbę: "))
# b = int(input("Podaj 2 liczbę: "))
#
# if a > b:
#     while b <= a:
#         print(b)
#         b += 1
#
# elif a == b:
#     print(f"Liczby są równe: {a}")
#
# else:
#     while a <= b:
#         print(a)
#         a += 1

# Zad 2

#Zbiór rozwiązań: [-4;4]

# a = 2
# b = -5
# c = -8
#
# delta = b ** 2 - 4*a*c
#
# pierwiastek_delta = math.sqrt(delta)
# pierwiastek_delta = round(pierwiastek_delta, 1)
#
# x1 = (-b - pierwiastek_delta) / (2 * a)
# x2 = (-b + pierwiastek_delta) / (2 * a)

#Nasze liczby mieszczą się w naszym zbiorze [-4;4], czyli nie trzeba zapisać warunku if else,
#ale dla celu ćwiczeń i tak dodamy te warunki

# if x1 > x2:
#     bigger_int = x1
# else:
#     bigger_int = x2
#
# if x1 < x2:
#     lower_int = x1
# else:
#     lower_int = x2
#
#
# if ((x1 and x2) >= -4) and ((x1 and x2) <= 4):
#     while lower_int <= bigger_int:
#         print(lower_int)
#         lower_int += 0.5
#         lower_int = round(lower_int, 1)


#Zad 3

# a = int(input("Podaj liczbę: "))
# while a > 0:
#     a = int(input("Podaj kolejną liczbę całkowitą: "))

#Zad 4

# a = int(input("Podaj 1 liczbę: "))
# b = int(input("Podaj 2 liczbę: "))
#
# if a > b:
#     while b <= a:
#         if b % 2 != 0:
#             b += 1
#             continue
#         else:
#             print(b)
#         b += 1
# elif a == b and a % 2 == 0:
#     print(f"Liczby są równe {a}")
# else:
#     while a <= b:
#         if a % 2 != 0:
#             a += 1
#             continue
#         else:
#             print(a)
#         a += 1

#########
#Zadania dodatkowe
#########

#Zad 1

# n = int(input("Podaj liczbę studentów: "))
# i = 1
# suma_punktów = 0
#
# while i <= n:
#     punkty_studenta = int(input(f"Punkty {i} studenta: "))
#     suma_punktów += punkty_studenta
#     i += 1
#
# srednia = suma_punktów / n
# print(f"Średnia liczba punktów wynosi: {srednia:.2f}")

#Zad 2

#Z instukcją conitnue

# n = int(input("Podaj liczbę studentów: "))
# i = 1
# suma_punktów = 0
#
# while i <= n:
#     punkty_studenta = int(input(f"Punkty {i} studenta: "))
#     if punkty_studenta < 0 or punkty_studenta > 100:
#         print("Punkty spoza zakresu (0-100), nie dodaję do średniej. Podaj punkty jeszcze raz!")
#         continue
#     else:
#         suma_punktów += punkty_studenta
#     i += 1
#
# srednia = suma_punktów / n
# print(f"Średnia liczba punktów wynosi: {srednia:.2f}")

####
#Pętla nieskończona z intrukcją break
#####

# i = 1
# suma_punktów = 0
#
# while True:
#     punkty_studenta = int(input(f"Punkty {i} studenta: "))
#     if punkty_studenta < 0 or punkty_studenta > 100:
#         print("Punkty spoza zakresu (0-100). Przerywam pętle!")
#         break
#     else:
#         suma_punktów += punkty_studenta
#     i += 1
#
# i -= 1
# srednia = suma_punktów / i
# print(f"Średnia liczba punktów wynosi: {srednia:.2f}")

#####################################################
### Pętle for
#####################################################

#Zad 1

#a)
# for i in range(1, 101):
#     print(i, end = " ")

#b)

# for i in range(100, -1, -1):
#     print(i, end=" ")

#c)

# for i in range(7, 78, 7):
#     print(i, end=" ")

#d)

# for i in range(20, -1, -2):
#     print(i, end=" ")

#Zad 2

# liczba = int(input("Podaj liczbę gwiazdek: "))
#
# for i in range(liczba):
#     for j in range(liczba):
#         print("*", end=' ')
#     print()

#Zad 3

# liczba = int(input("Podaj liczbę gwiazdek: "))
# for i in range(liczba):
#     i += 1
#     for j in range(i):
#         print("*", end=" ")
#     print()

#Zad 4 - ciąg arytmetyczny - dokończ
# an = a1 + (n - 1) *r
# Dane: n, a1, r

# n = int(input("Do którego wyrazu ciągu policzyć: "))
# a = int(input("Podaj pierwszy wyraz ciągu: "))
# r = int(input("Podaj różnicę ciągu: "))
#
# for i in range(1, n+1):
#     an = a + (i - 1) * r
#     print(an)

#Zad 5

# n = int(input("Podaj liczbę, której silnię chcesz obliczyć: "))
#
# silnia = 1
# for i in range(2, n+1):
#     silnia *= i
#
# print(f"{n}! wynosi: {silnia}")

##################
### Zadania dodatkowe
##################

#Zad 1

#Program bez polecenie continue

# while True:
#     liczba = int(input("Podaj liczbę całkowitą: "))
#     if liczba >= 0:
#         print("To jest liczba")
#         pierwiastek_liczby = math.sqrt(liczba)
#         pierwiastek_liczby = round(pierwiastek_liczby, 2)
#         print(f"Pierwiastek twojej liczby: {pierwiastek_liczby}")
#     else:
#         print("Dziękujemy za skorzystanie z naszej aplikacji")
#         break

#Program wykorzystujący polecenie continue

# while True:
#     liczba = int(input("Podaj liczbę całkowitą: "))
#
#     if liczba < 0:
#         print("Dziękujemy za skorzystanie z naszej aplikacji")
#         break
#     elif liczba >= 0:
#         print("To jest liczba")
#         pierwiastek_liczby = math.sqrt(liczba)
#         pierwiastek_liczby = round(pierwiastek_liczby, 2)
#         print(f"Pierwiastek twojej liczby: {pierwiastek_liczby}")
#     else:
#         print("Nieprawidłowa liczba, spróbuj ponownie.")
#         continue

#Zad 2 (Choinka)

# liczba = int(input("Podaj liczbę gwiazdek: "))
#
#
# for i in range(0, liczba+1):
#     for j in range(liczba - i):
#         print(" ", end="")
#     for k in range(i):
#         print("* ", end="")
#     print()

#################################################
### Stringi
#################################################

#Zad 1

# tekst = "Rzeszów jest piękny"

#a)
# print(tekst[0])

#b)
# print(f"'{tekst[6]}', '{tekst[9]}', '{tekst[12]}', '{tekst[1]}'")

#Zad 2

# tekst = "Python jest super"

#a)
# print(tekst[0])

#b)
# print(tekst[-1])

#c)
# print(tekst[0: : 2])

#d)
# print(tekst[1: : 3])

#e)
# print(tekst[10: :])

#f)
# print(tekst[::-1])

#####
#Zadania dodatkowe
#####

#Zad 1

#a)
# imie = input("Podaj imię: ")
# print(f"Witaj, {imie}")

#b)
# wiek = int(input("Podaj wiek: "))
# print(f"Twój wiek to: {wiek}")
#
#c)
# imie = input("Podaj swoje imię: ")
# nazwisko = input("Podaj swoje nazwisko: ")
#
# print(f"Twoje inicjały to: {imie[0].upper()}{nazwisko[0].upper()}")

#c)

# tekst = input("Podaj tekst: ")
# print((tekst + " ") * 5)

#d)

# tekst_1 = input("Podaj tekst: ")
# tekst_2 = input("Podaj tekst: ")
#
# polaczony_tekst = tekst_1 + tekst_2
#
# print(polaczony_tekst)

#e)

# first_word = input("Podaj 1 zdanie: ")
# len_first_word = len(first_word)
# second_word = input("Podaj 2 zdanie: ")
# len_second_word = len(second_word)
# first_half = math.floor(len_first_word/2)
# second_half = math.ceil(len_second_word/2)
# print(first_half)
# print(second_half)
#
# third_word = first_word[0:first_half] + second_word[second_half:]
# print(third_word)