#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Bonusvraag: k-Nearest Neighbors

(c) 2023 Hogeschool Utrecht
Peter van den Berg (petervandenberg@hu.nl)

Opdracht: werk onderstaande functies uit.


Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""


def euclidean_distance(x1, x2):
    """
    Bereken de euclidische afstand tussen twee datapunten (https://en.wikipedia.org/wiki/Euclidean_distance).

    Args:
        x1 (list of int): het eerste datapunt.
        x2 (list of int): het tweede datapunt.

    Returns:
        float: De berekende euclidische afstand.
    """
    distance = 0.0
    return distance


def k_nearest_neighbors(x_train, y_train, x_test, k=3):
    """
    Voorspel de labels van datapunten uit x_test op basis van de labels (y_train)
    van de k dichtstbijzijnde datapunten uit x_train met het K-nearest neighbors algoritme
    (zie https://medium.com/swlh/k-nearest-neighbor-ca2593d7a3c4).

    Args:
        x_train (list of list of int): een lijst met datapunten waarvan het label bekend is.
        y_train (list of int): een lijst met labels die bij bovenstaande datapunten horen.
        x_test (list of list of int): een lijst met datapunten waarvan de labels voorspeld moeten worden.
        k (int): het aantal datapunten uit x_train dat gebruikt wordt voor het voorspellen van het label (standaard 3).

    Returns:
        list of string: De voorspelde labels voor de datapunten uit X_test.
    """
    predictions = []

    return predictions


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
    is_float = type(expected_output) is float
    is_float_list = type(expected_output) is list and all([type(item) is float for item in expected_output])
    if is_float:
        # Vergelijk bij float als return-type op 7 decimalen om afrondingsfouten te omzeilen
        assert round(output - expected_output, 7) == 0, msg
    elif is_float_list:
        # Vergelijk bij floatlijst als return-type op 7 decimalen om afrondingsfouten te omzeilen
        assert [round(x - y, 7) for x, y in zip(output, expected_output)] == [0.0] * len(output), msg
    else:
        assert output == expected_output, msg


def test_euclidean_distance():
    testcases = [
        (([1, 2, 3], [4, 5, 6]), 5.1961524),
        (([0, 0, 0], [0, 0, 0]), 0.0),
        (([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), 0.0),
        (([1, 2, 3], [1, 2, 3, 4, 5]), 0.0),
        (([1, 2, 3, 5, 7, 11, 12], [1, 1, 2, 3, 4, 5, 8]), 8.1853528),
    ]

    for case in testcases:
        __my_assert_args(euclidean_distance, case[0], case[1])
    return 1


def test_k_nearest_neighbors():
    testcases = [
        ([[[1, 2], [3, 4], [5, 6]], ["appel", "peer", "appel"], [[2, 3]], 2], ["appel"]),
        ([[[-1, -2], [-3, -4], [-5, -6]],
          ["tablet", "tablet", "mobiel"],
          [[-2, -3], [-4, -5]], 1],
         ["tablet", "tablet"]),
        ([[[2, -3], [7, -4], [11, -6]], ["vrolijk", "boos", "boos"], [[1, -3], [10, -6]], 1], ['vrolijk', 'boos']),
        ([
             [[2, 3], [5, -4], [1, 6], [5, 3], [9, -40], [15, -16]],
             ["goud", "zilver", "brons", "goud", "zilver", "brons"],
             [[5, -4], [10, -6], [11, -30], [-7, 6]], 1],
         ['zilver', 'zilver', 'zilver', 'brons']),
        ([
             [[2, 3], [5, -4], [1, 6], [5, 3], [9, -40], [15, -16]],
             ["goud", "zilver", "brons", "goud", "zilver", "brons"],
             [[2, 3], [11, -30], [-7, 6]], 3],
         ['goud', 'zilver', 'goud']),
    ]

    for case in testcases:
        __my_assert_args(k_nearest_neighbors, case[0], case[1])
    return 1


def __main():
    try:
        print("\x1b[32m")

        test_euclidean_distance()
        print("Je functie euclidean_distance() werkt goed!")

        test_k_nearest_neighbors()
        print("Je functie k_nearest_neighbors() werkt goed!")

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
