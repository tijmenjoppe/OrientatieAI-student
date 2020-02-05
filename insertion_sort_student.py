#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Analytical Skills
Opgave: insertion sort

(c) 2019 Hogeschool Utrecht
Tijmen Muller (tijmen.muller@hu.nl)


Let op! Je mag voor deze opgave geen extra modules importeren met 'import'.
"""


def insert(lst, grens, waarde):
    """ Voegt de waarde op de juiste plek in het gesorteerde deel van lijst lst """
    # De lijst *lst* is gesorteerd van lst[0] t/m lst[grens]
    # Het element *waarde* wordt ingevoegd op de juiste plek in bovengenoemde gesorteerde deel,
    # dus hierna is de lijst *lst* gesorteerd van lst[0] t/m lst[grens+1]

    # Aanpak: begin bij index *grens* en verplaats elementen groter dan *waarde* naar rechts.
    # Als je een waarde tegenkomt die kleiner is dan *waarde* (of het begin van lijst *lst*),
    # dan voeg je *waarde* in op de vrijgekomen plek.
    return None     # De functie retourneert niets


def insertion_sort(lst):
    """ Implementatie van het insertion sort algoritme -- sortering vind plaats 'in place'. """
    return None     # De functie retourneert niets


"""==============================================[ HU TESTRAAMWERK ]====================================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import random


def test_insert():
    lst_res = [3, 5, 7, 11, 13, 2, 9, 14]
    lst_test = lst_res.copy()
    insert(lst_res, 4, 2)
    lst_correct = [2, 3, 5, 7, 11, 13, 9, 14]
    assert lst_res == lst_correct, \
        "Fout: insert({}, 4, 2) geeft {} in plaats van {}".format(lst_test, lst_res, lst_correct)

    lst_test = lst_res.copy()
    insert(lst_res, 5, 9)
    lst_correct = [2, 3, 5, 7, 9, 11, 13, 14]
    assert lst_res == lst_correct, \
        "Fout: insert({}, 5, 9) geeft {} in plaats van {}".format(lst_test, lst_res, lst_correct)

    lst_test = lst_res.copy()
    insert(lst_res, 6, 14)
    lst_correct = [2, 3, 5, 7, 9, 11, 13, 14]
    assert lst_res == lst_correct, \
        "Fout: insert({}, 6, 14) geeft {} in plaats van {}".format(lst_test, lst_res, lst_correct)


def test_insertion_sort():
    lst_test = random.sample(range(-99, 100), 6)
    lst_copy = lst_test.copy()
    insertion_sort(lst_test)
    assert lst_test == sorted(lst_copy), \
        "Fout: insertion_sort({}) geeft {} in plaats van {}".format(lst_copy, lst_test, sorted(lst_copy))


if __name__ == '__main__':
    try:
        print("\x1b[0;32m")

        test_insert()
        print("Je functie insert() werkt goed!")

        test_insertion_sort()
        print("Je insertion sort algoritme werkt goed!\n\nKnap gedaan!\n")

        print("\x1b[0;30m")
        aantal = int(input("Hoeveel getallen zal ik sorteren? "))
        lst = list(range(aantal))
        random.shuffle(lst)

        print("De lijst: \n" + str(lst))
        insertion_sort(lst)
        print("is na sortering: \n" + str(lst))

    except AssertionError as ae:
        print("\x1b[0;31m")
        print(str(ae))
