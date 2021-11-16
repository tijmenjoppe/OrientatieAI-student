#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Final assignment 1: getallen

(c) 2019 Hogeschool Utrecht,
Bart van Eijkelenburg en
Tijmen Muller (tijmen.muller@hu.nl)


Opdracht:
Werk onderstaande functies uit.
Voeg commentaar toe om je code toe te lichten.

Je kunt je functies testen met het gegeven raamwerk door het bestand
uit te voeren (of met behulp van `pytest`, als je weet hoe dat werkt).
Lever je werk in op Canvas als alle tests slagen.

Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""

# TODO: Vul hier je naam, klas en studentnummer in.
naam = ""
klas = ""
studentnummer = -1


def is_even(n):
    """
    Bepaal of een getal even is.

    Args:
        n (int): Een geheel getal.

    Returns:
        bool: True als even, False als oneven.
    """
    return


def floor(real):
    """ Bepaal het grootste gehele getal (int), dat kleiner dan of gelijk is aan real (float). """
    return


def ceil(real):
    """ Bepaal het kleinste gehele getal (int), groter dan of gelijk aan real (float). """
    return


def div(n):
    """
    Bepaal alle delers van een geheel getal.

    Het positieve gehele getal a is een deler van n, als er een positief geheel getal b is, zodat a × b = n.

    Args:
        n (int): Een geheel getal.

    Returns:
        list: Een gesorteerde lijst met alle delers van `n`.
    """
    divisors = []
    return sorted(divisors)


def is_prime(n):
    """
    Bepaal of gegeven getal een priemgetal is.

    Hint: maak gebruik van de functie `div()`.
    Optioneel: bedenk een efficiënter alternatief.

    Args:
        n (int): Een geheel getal.

    Returns:
        bool: True als het getal een priemgetal is, anders False.
    """
    return


def primes(num):
    """
    Bepaal alle priemgetallen kleiner dan een bepaald geheel getal.

    Hint: Maak gebruik van de functie `is_prime()`.

    Args:
        num (int): Een geheel getal.

    Returns:
        list: Een gesorteerde lijst met alle priemgetallen kleiner dan `num`.
    """
    primelist = []
    return sorted(primelist)


def primefactors(n):
    """
    Bepaal de verzameling van priemfactoren van n.

    Args:
        n (int): Een geheel getal.

    Returns:
        list: Een gesorteerde lijst met alle priemfactoren van n. Als n kleiner
            dan 2, retourneer dan een lege lijst `[]`.
    """
    factors = []
    return sorted(factors)


def gcd(a, b):
    """
    Bepaal de grootste grootste gemene deler (ook wel 'greatest common divisor', gcd) van twee natuurlijke getallen.

    Je hebt twee opties voor deze opgave:
    1.  Je programmeert hier het algoritme van Euclides.
        Zie: https://nl.wikipedia.org/wiki/Algoritme_van_Euclides
    2.  Je bedenkt zelf een oplossing waarbij je gebruik maakt van de eerder
        geschreven methode div(n) om de gcd te bepalen.

    Args:
        a (int): Een geheel getal.
        b (int): Een geheel getal.

    Returns:
        int: De grootste grootste gemene deler.
    """
    return


def lcm(a, b):
    """
    Bepaal het kleinste gemene veelvoud, kgv (ook wel 'least common multiple', lcm) van twee natuurlijke getallen.

    Args:
        a (int): Een geheel getal.
        b (int): Een geheel getal.

    Returns:
        int: Het kleinste gemene veelvoud.
    """
    return


def add_frac(n1, d1, n2, d2):
    """Sommeer twee breuken als breuk. Vereenvoudig de breuk zover als mogelijk.

    Args:
        n1 (int): De teller van de eerste breuk.
        d1 (int): De noemer van de eerste breuk.
        n2 (int): De teller van de tweede breuk.
        d2 (int): De noemer van de tweede breuk.

    Returns:
        tuple: De som *als breuk*, met eerst de teller en dan de noemer van het resultaat.

    Examples:
        Gegeven 1/3 + 1/5 = 8/15, dan

        >> add_frac(1, 3, 1, 5)
        (8, 15)

        Gegeven 1/2 + 1/4 = 3/4, dan

        >> add_frac(1, 2, 1, 4)
        (3, 4)

        Gegeven 2/3 + 3/2 = 13/6, dan

        >> add_frac(2, 3, 3, 2)
        (13, 6)
    """
    return 1, 1


"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""


def __my_assert_args(function, args, expected_output, check_type=True):
    """
    Controleer of gegeven functie met gegeven argumenten het verwachte resultaat oplevert.

    Optioneel wordt ook het return-type gecontroleerd.
    """
    argstr = str(args).replace(',)', ')')
    output = function(*args)

    # Controleer eerst het return-type (optioneel)
    if check_type:
        msg = f"Fout: {function.__name__}{argstr} geeft geen {type(expected_output)} terug als return-type"
        assert type(output) is type(expected_output), msg

    # Controleer of de functie-uitvoer overeenkomt met de gewenste uitvoer
    msg = f"Fout: {function.__name__}{argstr} geeft {output} in plaats van {expected_output}"
    if type(expected_output) is float:
        # Vergelijk bij float als return-type op 7 decimalen om afrondingsfouten te omzeilen
        assert round(output - expected_output, 7) == 0, msg
    else:
        assert output == expected_output, msg


def test_id():
    assert naam != "", "Je moet je naam nog invullen!"
    assert studentnummer != -1, "Je moet je studentnummer nog invullen!"
    assert klas != "", "Je moet je klas nog invullen!"


def test_is_even():
    testcases = [
        ((1,), False),
        ((2,), True),
        ((3,), False),
        ((4,), True)
    ]

    for case in testcases:
        __my_assert_args(is_even, case[0], case[1])


def test_floor():
    testcases = [
        ((1.05,), 1),
        ((1.95,), 1),
        ((-1.05,), -2),
        ((-1.95,), -2),
        ((0.05,), 0),
        ((-0.05,), -1),
        ((0.0, ), 0),
        ((1.0, ), 1),
        ((-1.0, ), -1)
    ]

    for case in testcases:
        __my_assert_args(floor, case[0], case[1])


def test_floor_simulated():
    import random
    import math

    for _ in range(10):
        x = random.uniform(-10.0, 10.0)
        __my_assert_args(floor, (x,), math.floor(x))


def test_ceil():
    testcases = [
        ((1.05,), 2),
        ((1.95,), 2),
        ((-1.05,), -1),
        ((-1.95,), -1),
        ((0.05,), 1),
        ((-0.05,), 0),
        ((0.0, ), 0),
        ((1.0, ), 1),
        ((-1.0, ), -1)
    ]

    for case in testcases:
        __my_assert_args(ceil, case[0], case[1])


def test_ceil_simulated():
    import random
    import math

    for _ in range(10):
        x = random.uniform(-10.0, 10.0)
        __my_assert_args(ceil, (x,), math.ceil(x))


def test_div():
    testcases = [
        ((1,), [1]),
        ((2,), [1, 2]),
        ((3,), [1, 3]),
        ((4,), [1, 2, 4]),
        ((8,), [1, 2, 4, 8]),
        ((12,), [1, 2, 3, 4, 6, 12]),
        ((19,), [1, 19]),
        ((25,), [1, 5, 25]),
        ((929,), [1, 929]),
        ((936,), [1, 2, 3, 4, 6, 8, 9, 12, 13, 18, 24, 26, 36, 39, 52, 72, 78, 104, 117, 156, 234, 312, 468, 936])
    ]

    for case in testcases:
        __my_assert_args(div, case[0], sorted(case[1]))


def test_is_prime():
    testcases = [
        ((1,), False),
        ((2,), True),
        ((3,), True),
        ((4,), False),
        ((5,), True),
        ((6,), False),
        ((9,), False),
        ((29,), True)
    ]

    for case in testcases:
        __my_assert_args(is_prime, case[0], case[1])


def test_primefactors():
    testcases = [
        ((-1,), []),
        ((1,), []),
        ((2,), [2]),
        ((3,), [3]),
        ((4,), [2, 2]),
        ((8,), [2, 2, 2]),
        ((12,), [2, 2, 3]),
        ((2352,), [2, 2, 2, 2, 3, 7, 7]),
        ((9075,), [3, 5, 5, 11, 11])
    ]

    for case in testcases:
        __my_assert_args(primefactors, case[0], sorted(case[1]))


def test_primes():
    testcases = [
        ((1,), []),
        ((2,), []),
        ((3,), [2]),
        ((4,), [2, 3]),
        ((5,), [2, 3]),
        ((6,), [2, 3, 5]),
        ((30,), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
    ]

    for case in testcases:
        __my_assert_args(primes, case[0], sorted(case[1]))


def test_gcd():
    testcases = [
        ((60, 1), 1),
        ((60, 6), 6),
        ((60, 7), 1),
        ((60, 8), 4),
        ((60, 9), 3),
        ((60, 11), 1),
        ((60, 13), 1),
        ((60, 14), 2),
        ((60, 15), 15),
        ((60, 16), 4),
        ((60, 18), 6)
    ]

    for case in testcases:
        __my_assert_args(gcd, case[0], case[1])


def test_gcd_simulated():
    import random
    import math

    for _ in range(10):
        a = random.randrange(3, 201, 3)
        b = random.randrange(4, 201, 4)
        __my_assert_args(gcd, (a, b), math.gcd(a, b))


def test_lcm():
    testcases = [
        ((60, 1), 60),
        ((60, 2), 60),
        ((60, 7), 420),
        ((60, 8), 120),
        ((60, 9), 180),
        ((60, 10), 60),
        ((60, 11), 660),
        ((60, 18), 180)
    ]

    for case in testcases:
        __my_assert_args(lcm, case[0], case[1])


def test_add_frac():
    testcases = [
        ((1, 3, 1, 5), (8, 15)),
        ((1, 2, 1, 4), (3, 4)),
        ((2, 3, 3, 2), (13, 6)),
        ((1, 2, 1, 6), (2, 3)),
        ((3, 4, 1, 6), (11, 12)),
        ((1, 6, 3, 4), (11, 12)),
        ((1, 2, 1, 3), (5, 6)),
        ((1, 2, 2, 3), (7, 6))
    ]

    for case in testcases:
        __my_assert_args(add_frac, case[0], case[1])


def __main():
    """ Test alle functies. """
    # Noodzakelijk voor gekleurde tekst binnen een Windows terminal
    import os
    os.system("")

    try:
        print("\x1b[32m")   # Groene tekstkleur
        test_id()

        test_is_even()
        print("Je functie is_even(n) werkt goed!")

        test_floor()
        test_floor_simulated()
        print("Je functie floor(real) werkt goed!")

        test_ceil()
        test_ceil_simulated()
        print("Je functie ceil(real) werkt goed!")

        test_div()
        print("Je functie div(n) werkt goed!")

        test_is_prime()
        print("Je functie is_prime(n) werkt goed!")

        test_primes()
        print("Je functie primes(num) werkt goed!")

        test_primefactors()
        print("Je functie primefactors(n) werkt goed!")

        test_gcd()
        test_gcd_simulated()
        print("Je functie gcd(a, b) werkt goed!")

        test_lcm()
        print("Je functie lcm(a, b) werkt goed!")

        test_add_frac()
        print("Je functie add_frac(n1, d1, n2, d2) werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken!")
        print("Lever je werk nu in op Canvas...")


    except AssertionError as ae:
        print("\x1b[31m")   # Rode tekstkleur
        print(ae)

    print("\x1b[0m")    # Reset tekstkleur


if __name__ == '__main__':
    __main()
