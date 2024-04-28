#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Oefening: getallen

(c) 2023 Hogeschool Utrecht,
Peter van den Berg (peter.vandenberg@hu.nl)
Tijmen Muller (tijmen.muller@hu.nl)


Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""


def floor(real):
    """
    Bepaal het grootste gehele getal (int), dat kleiner dan of gelijk is aan het gegeven reeel getal (float).

    Args:
        real (float): Een reeel getal.

    Returns:
        int: Het grootste gehele getal (int), dat kleiner dan of gelijk is aan het gegeven reeel getal.
    """
    return 0


def rekenkundige_rij(start, verschil, lengte):
    """
    Berekent een rekenkundige rij (an = a0 + n · c) gegeven een startgetal, een verschil en een lengte.

    Args:
        start (int): Het getal waar de rij mee begint
        verschil (int): de stapgrootte van de rij
        lengte (int): de lengte van de rij

    Returns:
        list of int: de rekenkundige rij
    """

    rij = []
    return rij


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


def test_rekenkundige_rij():
    testcases = [
        ((1, 2, 3), [1, 3, 5]),
        ((3, 4, 5), [3, 7, 11, 15, 19]),
        ((3, 5, 7), [3, 8, 13, 18, 23, 28, 33]),
        ((5, 2, 5), [5, 7, 9, 11, 13]),
        ((5, 3, 5), [5, 8, 11, 14, 17]),
        ((10, 10, 10), [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    ]

    for case in testcases:
        __my_assert_args(rekenkundige_rij, case[0], case[1])
    return 1


def __main():
    try:
        print("\x1b[32m")

        test_floor()
        print("Je functie floor() werkt goed!")

        test_rekenkundige_rij()
        print("Je functie rekenkundige_rij() werkt goed!")

    except AssertionError as ae:
        print("\x1b[31m")   # Rode tekstkleur
        if not ae:
            print("Je code veroorzaakt onderstaande AssertionError:")
            raise ae
        else:
            print(ae)
        print("\x1b[0m")    # Reset tekstkleur


if __name__ == '__main__':
    __main()
