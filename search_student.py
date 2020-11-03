#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Opgave: zoeken

(c) 2019 Hogeschool Utrecht
Tijmen Muller (tijmen.muller@hu.nl)


Let op! Je mag voor deze opgave geen extra modules importeren met 'import'.
"""


def linear_search(lst, target):
    """ Bepaal of *target* voorkomt in lijst *lst* door middel van lineair zoeken. """
    return False


def linear_search_index(lst, target):
    """ Geef de positie (m.a.w. index) van *target* in lijst *lst* d.m.v. lineair zoeken. """
    index = 0
    return -1


def binary_search(lst, target):
    """ Bepaal of *target* voorkomt in lijst *lst* door middel van binair zoeken. """
    # stap 1
    mini = 0

    # stap 6(!)
    while False:    # hoelang ga je door met zoeken?
        # stap 2
        # stap 3
        return True
        # stap 4
        # stap 5

    return False


def binary_search_index(lst, target):
    """ Geef de positie (m.a.w. index) van *target* in lijst *lst* d.m.v. binair zoeken. """
    return -1


def linear_search_index_steps(lst, target):
    """
    Geef de positie (m.a.w. index) van *target* in lijst *lst* d.m.v. lineair zoeken,
    én het aantal benodigde stappen.
    """
    index = 0
    steps = 0
    return -1, steps


def binary_search_index_steps(lst, target):
    """
    Geef de positie (m.a.w. index) van *target* in lijst *lst* d.m.v. binair zoeken,
    én het aantal benodigde stappen.
    """
    steps = 0

    return -1, steps


"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import random


def test_linear_search():
    for i in range(10):
        lst_test = random.sample(range(20), 10)
        target = random.randrange(20)
        assert linear_search(lst_test, target) == (target in lst_test), \
            f"Fout: linear_search({lst_test}, {target}) geeft {linear_search(lst_test, target)} " \
            f"in plaats van {target in lst_test}"


def test_linear_search_index():
    for i in range(10):
        lst_test = random.sample(range(20), 10)
        target = random.choice(lst_test)
        assert linear_search_index(lst_test, target) == lst_test.index(target), \
            f"Fout: linear_search_index({lst_test}, {target}) geeft {linear_search_index(lst_test, target)} " \
            f"in plaats van {lst_test.index(target)}"

        lst_test = [0, 1, 2]
        assert linear_search_index(lst_test, 3) == -1, f"Fout: linear_search_index({lst_test}, {3}) geeft " \
                                                       f"{linear_search_index(lst_test, 3)} in plaats van {-1}"


def test_linear_search_index_steps():
    for i in range(10):
        lst_test = random.sample(range(20), 10)
        target = random.choice(lst_test)
        assert linear_search_index_steps(lst_test, target)[0] == lst_test.index(target), \
            f"Fout: linear_search_index_steps({lst_test}, {target}) geeft " \
            f"{linear_search_index_steps(lst_test, target)[0]} in plaats van {lst_test.index(target)}"


def test_binary_search():
    for i in range(10):
        lst_test = sorted(random.sample(range(20), 10))
        target = random.randrange(20)
        assert binary_search(lst_test, target) == (target in lst_test), \
            f"Fout: binary_search({lst_test}, {target}) geeft {binary_search(lst_test, target)} " \
            f"in plaats van {target in lst_test}"


def test_binary_search_index():
    for i in range(10):
        lst_test = sorted(random.sample(range(20), 10))
        target = random.choice(lst_test)
        assert binary_search_index(lst_test, target) == lst_test.index(target), \
            f"Fout: binary_search_index({lst_test}, {target}) geeft {binary_search_index(lst_test, target)} " \
            f"in plaats van {lst_test.index(target)}"

        lst_test = [0, 1, 2]
        assert binary_search_index(lst_test, 3) == -1, \
            f"Fout: binary_search_index({lst_test}, {3}) geeft {binary_search_index(lst_test, 3)} in plaats van {-1}"


def test_binary_search_index_steps():
    for i in range(10):
        lst_test = sorted(random.sample(range(20), 10))
        target = random.choice(lst_test)
        assert binary_search_index_steps(lst_test, target)[0] == lst_test.index(target), \
            f"Fout: binary_search_index_steps({lst_test}, {target}) geeft " \
            f"{binary_search_index_steps(lst_test, target)[0]} in plaats van {lst_test.index(target)}"


if __name__ == '__main__':
    try:
        print("\x1b[0;32m")

        test_linear_search()
        print("Je functie linear_search() werkt goed!")

        test_linear_search_index()
        print("Je functie linear_search_index() werkt goed!")

        test_binary_search()
        print("Je functie binary_search() werkt goed!")

        test_binary_search_index()
        print("Je functie binary_search_index() werkt goed!")

        test_linear_search_index_steps()
        print("Je functie linear_search_index_steps() werkt goed!")

        test_binary_search_index_steps()
        print("Je functie binary_search_index_steps() werkt goed!")

        print("\x1b[0;30m")
        size = int(input("Geef een grootte voor de lijst: "))
        lst_input = list(range(size))
        print("Ik ga zoeken in:", lst_input)
        tgt = int(input("Geef een getal: "))

        (idx, cnt) = linear_search_index_steps(lst_input, tgt)
        print(f"Het lineair zoekalgoritme vond '{tgt}' op index '{idx}' na {cnt} stappen.")

        (idx, cnt) = binary_search_index_steps(lst_input, tgt)
        print(f"Het binair zoekalgoritme vond '{tgt}' op index '{idx}' na {cnt} stappen.")

    except AssertionError as ae:
        print("\x1b[0;31m")
        print(ae)
