#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Oefening: Lineaire regressie

(c) 2023 Hogeschool Utrecht,
Peter van den Berg (petervandenberg@hu.nl)


Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""


def gradient_descent(x, y, num_iterations=1000, learning_rate=0.0001):
    """
    Traint de coefficienten a en b voor het lineaire regressiemodel ŷ = a + b * x met de gradient descent methode.

    Args:
        x (list): de onafhankelijke waarden van de observaties
        y (list): de afhankelijke waarden van de observaties
        num_iterations (int): aantal iteraties om te leren
        learning_rate (float): leerconstante

    Returns:
        [float, float]: de berekende coefficienten
    """
    coefficients = [0, 0]
    
    return coefficients


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


def test_gradient_descent():    
    data = {
        'presence': [29, 36, 41, 45, 48, 50, 56, 61, 67, 67, 67, 71, 75, 79, 83, 88],
        'grade': [4.1, 4.3, 4.0, 5.2, 4.8, 4.9, 5.9, 5.2, 4.9, 5.7, 6.2, 6.1, 4.4, 6.1, 6.8, 6.9]
    }

    testcases = [
        ((data['presence'], data['grade'], 1), [0.00195707, 0.07867846]),
        ((data['presence'], data['grade'], 10), [0.00402798, 0.07866434]),
        ((data['presence'], data['grade'], 100), [0.02463723, 0.07842538]),
        ((data['presence'], data['grade'], 1000), [0.22125887, 0.07614560]),
        ((data['presence'], data['grade'], 10000), [1.48364100, 0.06150855]),
        ((data['presence'], data['grade'], 100000), [2.40810075, 0.05078965]),
    ]

    for case in testcases:
        __my_assert_args(gradient_descent, case[0], case[1])
    return 1


def __main():
    try:
        print("\x1b[32m")

        test_gradient_descent()
        print("Je functie gradient_descent() werkt goed!")

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
