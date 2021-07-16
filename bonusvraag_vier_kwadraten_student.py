#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Bonusvraag: vier kwadraten

(c) 2019 Hogeschool Utrecht,
Tijmen Muller (tijmen.muller@hu.nl)


Opdracht: werk onderstaande functies uit.

Je kunt je functies testen met het gegeven raamwerk door het bestand
uit te voeren (of met behulp van pytest, als je weet hoe dat werkt).
Lever je werk in op Canvas als alle tests slagen.

Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""


def vier_kwadraten(kwadraatsom):
    """
    Geef een lijst met vier getallen, zodat de som van de kwadraten van die
    getallen gelijk is aan gegeven kwadraatsom (int).
    """
    return [0, 0, 0, 0]


"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
from functools import reduce
import random
from time import perf_counter


def test_vier_kwadraten():
    # Simulated test cases
    for cnt in range(100):
        n = random.randrange(1, 10)

        for _ in range(4):
            n *= 10
            n += random.randrange(0, 10)

        lst = vier_kwadraten(n)
        assert len(lst) == 4, \
            f"Fout: vier_kwadraten() geeft geen lijst met 4 maar met {len(lst)} getallen, namelijk {lst}"
        assert n == reduce(lambda x, y: x + y, (map(lambda x: x ** 2, lst))), \
            f"Fout: vier_kwadraten({n}) geeft {lst}, maar {lst[0]}² + {lst[1]}² + {lst[2]}² + {lst[3]}² != {n}"


def test_vier_kwadraten_tijd():
    # Test cases
    testcases = [36624, 73504, 54296, 40923, 33504, 42627, 70798, 90815, 55367, 52699]

    for case in testcases:
        print(case)
        lst = vier_kwadraten(case)
        assert len(lst) == 4, \
            f"Fout: vier_kwadraten() geeft geen lijst met 4 maar met {len(lst)} getallen, namelijk {lst}"
        assert case == reduce(lambda x, y: x + y, (map(lambda x: x ** 2, lst))), \
            f"Fout: vier_kwadraten({case}) geeft {lst}, maar {lst[0]}² + {lst[1]}² + {lst[2]}² + {lst[3]}² != {case}"


if __name__ == '__main__':
    try:
        print("\x1b[32m")
        test_vier_kwadraten()
        print("Je functie vier_kwadraten(getal) werkt goed!\n")

        print("\x1b[0m")
        print("Timing van 10 getallen...")

        start_time = perf_counter()
        test_vier_kwadraten_tijd()
        delta_time = perf_counter() - start_time
        print(f"Totale tijd: {delta_time*1000:.0f}ms")

    except AssertionError as ae:
        print("\x1b[31m")
        print(ae)
