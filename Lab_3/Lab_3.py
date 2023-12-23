#Zad 1
# names = ["Kasia", "Basia", "Marian", "Paweł"]

#a)
# names.sort()
# print(names)

#b)
# names.append("Marek")
# names.append("Darek")
# last_name = names.pop()
# print(last_name)

#c)
# names.insert(2, "Kuba")
# print(names)

#d)
# names.reverse()
# double_names = names * 2
# print(double_names)


#Zad 2

# tekst = "Rzeszów jest piękny"
#
# #a)
# print(tekst[0])
#
# #b)
# print(f"'{tekst[6]}', '{tekst[9]}', '{tekst[12]}', '{tekst[1]}'")

#Zad 3

# tekst = "Python jest super"
#
# #a)
#
# print(tekst[0])
# print(tekst[-1])
#
# #b)
# print(tekst[0: : 2])
#
# #c)
# print(tekst[1: : 3])
#
# #d)
# print(tekst[10: :])
#
# #e)
# print(tekst[::-1])

#Zad 4

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

#####################################
#Krotki, dict
#####################################

#Zad 1

#Program:

import random
#
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# my_list = []
# random_word = ''
# n = int(input("Podaj wielkość listy: "))
# x = int(input("Podaj maksymalną wiekość elementu w liście: "))
#
# for i in range(n):
#     random_length = random.randint(1, x)
#     for j in range(random_length):
#         random_word += random.choice(alphabet)
#     my_list.append(random_word)
#     random_word = ''
#
# my_tuple = tuple(my_list)
# print(my_tuple)

#a)
# sum = 0
# for i in range(len(my_tuple)):
#     sum += len(my_tuple[i])
#
# print(f"Suma znaków w krtoce: {sum}")

#b)

# sum_k = 0
#
# for i in range(len(my_tuple)):
#     for j in my_tuple[i]:
#         if 'k' == j:
#             sum_k += 1
# print(f"Liczba litery 'k' w krotce: {sum_k}")

#c)

# sum_kt = 0
#
# for i in range(len(my_tuple)):
#     count_kt = my_tuple[i].count('kt')
#     sum_kt += count_kt
# print(f"Suma 'kt' w krotce: {sum_kt}")

#d)

# s = int(input("Wyrazy o jakiej długości chcesz sprawdzić: "))
# sum = 0
#
# for i in range(len(my_tuple)):
#     if s == len(my_tuple[i]):
#         sum += 1
#
# print(f"Elemntów o długości {s} w krotce jest: {sum}")


#Zad 2

# grocery_list = {"Mleko": 3, "Chleb": 5, "Kurczak": 22, "Makaron": 3, "Ryż": 4, "Jabłka": 3, "Banany": 6, "Warzywa": 15}
#
# sum = 0
#
# for value in grocery_list.values():
#     sum += value
#
# print(f"Te zakupy będą cię kosztować {sum} zł")


# #Zad 3
#
# rachunki_za_prad = {"czerwiec": 120, "lipiec": 110, "sierpień": 98, "wrzesień": 115, "październik": 86, "listopad": 140, "grudzień": 130}
#
# #a)
#
# print(rachunki_za_prad.values())
# max_value = max(rachunki_za_prad.values())
# min_value = min(rachunki_za_prad.values())
# suma = sum(rachunki_za_prad.values())
#
# wartosc_srednia = suma / len(rachunki_za_prad.values())
#
# print(f"Największy rachunek za prąd: {max_value} zł")
# print(f"Najmniejszy rachunek za prąd: {min_value} zł")
# print(f"Suma wszystkich rachunków za prąd: {suma} zł")
# print(f"Wartość średnia rachunku za prąd: {wartosc_srednia:.2f} zł")
#
# #b)
#
# ostatni_miesiac = list(rachunki_za_prad.values())[-1]
#
# if ostatni_miesiac > wartosc_srednia:
#     print("Zacznij oszczędzać")
# else:
#     print("Jesteś bezpieczny")

# #Zad 4
#
# a = random.randint(3, 7)
# b = random.randint(3, 7)
#
# X =[]
# Y =[]
#
# for i in range(a):
#     random_number = random.randint(0, 10)
#     X.append(random_number)
#
# for i in range(b):
#     random_number = random.randint(0, 10)
#     Y.append(random_number)
#
# print(f"Zbiór X: {X}")
# print(f"Zbiór Y: {Y}")
#
# #a)
#
# if 5 in X:
#     print("Zbiór X zawiera liczbę 5")
# else:
#     print("Zbiór X nie zawiera liczby 5")
#
# #b)
#
# is_subset_X = set(X).issubset(set(Y))
#
# if is_subset_X:
#     print("Zbiór X jest podzbiorem zbioru Y")
# else:
#     print("Zbiór X nie jest podzbiorem zbioru Y")
#
# #c)
#
# is_subset_Y = set(Y).issubset(set(X))
#
# if is_subset_Y:
#     print("Zbiór Y jest podzbiorem zbioru X")
# else:
#     print("Zbiór Y nie jest podzbiorem zbioru X")
#
# #d)
#
# is_superset_X = set(X).issuperset(set(Y))
#
# if is_superset_X:
#     print("Zbiór X jest nadzbiorem zbioru Y")
# else:
#     print("Zbiór X nie jest nadzbiorem zbioru Y")
#
# #e)
#
# is_superset_Y = set(Y).issuperset(set(X))
#
# if is_superset_Y:
#     print("Zbiór Y jest nadzbiorem zbioru X")
# else:
#     print("Zbiór Y nie jest nadzbiorem zbioru X")
#
#
# #f)
#
# wynik_sumy = set(X).union(set(Y))
# print(f"Suma zbiorów X oraz Y: {wynik_sumy}")
#
# #g)
#
# różnica_zbiorów_x_y = set(X).difference(set(Y))
# print(f"Różnica zbiorów X oraz Y: {różnica_zbiorów_x_y}")
#
# #h)
#
# roznica_zbiorow_y_x = set(Y).difference(set(X))
# print(f"Różnica zbiorów Y oraz X: {roznica_zbiorow_y_x}")
#
# #i)
#
# iloczyn_zbiorow = set(X).intersection(set(Y))
# print(f"Iloczyn zbiorów X oraz Y: {iloczyn_zbiorow}")
#
# #j)
#
# roznica_symetryczna = set(X).symmetric_difference(set(Y))
# print(f"Różnica symetryczna zbiorów X oraz Y: {roznica_symetryczna}")
#
# #k)
#
# max_X = max(X)
# max_Y = max(Y)
#
# if max_X >= max_Y:
#     print(f"Najwięszka wartość obydwu zbiorów to: {max_X}")
# else:
#     print(f"Najwięszka wartość obydwu zbiorów to: {max_Y}")
#
# #l)
#
# first_element = X[0]
# del X[0]
#
# Y.append(first_element)
# print(f"Zbiór X: {X}")
# print(f"Zbiór Y: {Y}")
#
# #m)
#
# Y = X.copy()
# print(f"Zbiór X: {X}")
# print(f"Zbiór Y po skopiowaniu: {Y}")
#
# #n)
#
# X.clear()
# Y.clear()
# print(f"Wyczyszczony zbiór X: {X}")
# print(f"Wyczyszczony zbiór Y: {Y}")
