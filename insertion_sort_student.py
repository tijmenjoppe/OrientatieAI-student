#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Opgave: insertion sort

(c) 2019 Hogeschool Utrecht
Tijmen Muller (tijmen.muller@hu.nl)


Let op! Je mag voor deze opgave geen extra modules importeren met 'import'.
"""


def insert(lst, grens, waarde):
    """
    Voeg de waarde (int) in op de juiste plek van het gesorteerde deel van lijst lst.
    Er wordt gekeken vanaf gegeven index grens (int).
    """
    # De lijst *lst* is gesorteerd van lst[0] t/m lst[grens]
    # Het element *waarde* wordt ingevoegd op de juiste plek in bovengenoemde gesorteerde deel,
    # dus hierna is de lijst *lst* gesorteerd van lst[0] t/m lst[grens+1]

    # Aanpak: begin bij index *grens* en verplaats elementen groter dan *waarde* naar rechts.
    # Als je een waarde tegenkomt die kleiner is dan *waarde* (of het begin van lijst *lst*),
    # dan voeg je *waarde* in op de vrijgekomen plek.
    return None     # De functie retourneert niets


def insertion_sort(lst):
    """
    Sorteer gegeven lijst lst met het insertion sort algoritme.
    Zorg dat de gegeven lijst niet verandert, maar geef een nieuwe, gesorteerde variant van de lijst terug.
    """
    # Kopieer de originele lijst
    lst_sorted = lst.copy()

    # Retourneer een gesorteerde variant van de lijst
    return lst_sorted


"""
==========================[ HU TESTRAAMWERK ]================================
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
        f"Fout: insert({lst_test}, 4, 2) geeft {lst_res} in plaats van {lst_correct}"

    lst_test = lst_res.copy()
    insert(lst_res, 5, 9)
    lst_correct = [2, 3, 5, 7, 9, 11, 13, 14]
    assert lst_res == lst_correct, \
        f"Fout: insert({lst_test}, 5, 9) geeft {lst_res} in plaats van {lst_correct}"

    lst_test = lst_res.copy()
    insert(lst_res, 6, 14)
    lst_correct = [2, 3, 5, 7, 9, 11, 13, 14]
    assert lst_res == lst_correct, \
        f"Fout: insert({lst_test}, 6, 14) geeft {lst_res} in plaats van {lst_correct}"


def test_insertion_sort():
    lst_test = random.choices(range(-99, 100), k=6)
    lst_copy = lst_test.copy()
    lst_output = insertion_sort(lst_test)

    assert lst_copy == lst_test, "Fout: insertion_sort(lst) verandert de inhoud van lijst lst"
    assert lst_output == sorted(lst_test), \
        f"Fout: insertion_sort({lst_test}) geeft {lst_output} in plaats van {sorted(lst_test)}"


if __name__ == '__main__':
    try:
        print("\x1b[0;32m")

        test_insert()
        print("Je functie insert() werkt goed!")

        test_insertion_sort()
        print("Je insertion sort algoritme werkt goed!\n\nKnap gedaan!\n")

        print("\x1b[0;30m")
        aantal = int(input("Hoeveel getallen zal ik sorteren? "))
        lijst = random.choices(range(0, 100), k=aantal)

        print(f"De lijst: \n\t{lijst}")
        gesorteerde_lijst = insertion_sort(lijst)
        print(f"is na sortering: \n\t{gesorteerde_lijst}")

    except AssertionError as ae:
        print("\x1b[0;31m")
        print(str(ae))
