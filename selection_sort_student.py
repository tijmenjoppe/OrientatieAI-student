"""
Oriëntatie op AI

Opgave: selection sort

(c) 2019 Hogeschool Utrecht
Tijmen Muller (tijmen.muller@hu.nl)


Let op! Je mag voor deze opgave geen extra modules importeren met 'import'.
"""


def swap(lst, index1, index2):
    """ Verwissel de waardes op positie index1 (int) en index2 (int) in lijst lst. """
    lst[index1] = lst[index2]


def find_index_of_minimum(lst, start_index=0):
    """ Vind de locatie van het minimum in lijst lst vanaf een gegeven start_index (int). """
    minimum = lst[start_index]
    index_of_minimum = start_index

    # Doorloop de lijst lst vanaf start_index en
    # update minimum en index_of_minimum waar nodig.

    return index_of_minimum


def selection_sort(lst):
    """
    Sorteer gegeven lijst lst met het selection sort algoritme.

    Zorg dat de gegeven lijst niet verandert, maar geef een nieuwe, gesorteerde variant van de lijst terug.
    """
    # Implementeer selection sort met behulp van
    # swap() en find_index_of_minimum()
    return


"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import random


def test_swap():
    lst_test = [4, 9, 7]
    swap(lst_test, 0, 1)
    assert lst_test == [9, 4, 7], "Fout: swap([4, 9, 7], 0, 1) geeft {} in plaats van {}".format(lst_test, [9, 4, 7])

    lst_test = [4, 9, 7]
    swap(lst_test, 1, 2)
    assert lst_test == [4, 7, 9], "Fout: swap([4, 9, 7], 1, 2) geeft {} in plaats van {}".format(lst_test, [4, 7, 9])

    lst_test = [4, 9, 7]
    swap(lst_test, 0, 2)
    assert lst_test == [7, 9, 4], "Fout: swap([4, 9, 7], 0, 2) geeft {} in plaats van {}".format(lst_test, [7, 9, 4])


def test_find_index_of_minimum():
    lst_test = [18, 6, 21, 44, 9, 14]
    assert find_index_of_minimum(lst_test, 0) == 1, \
        f"Fout: find_index_of_minimum({lst_test}, 0) geeft {find_index_of_minimum(lst_test, 0)} in plaats van 1"
    assert find_index_of_minimum(lst_test, 2) == 4, \
        f"Fout: find_index_of_minimum({lst_test}, 2) geeft {find_index_of_minimum(lst_test, 2)} in plaats van 4"
    assert find_index_of_minimum(lst_test, 3) == 4, \
        f"Fout: find_index_of_minimum({lst_test}, 3) geeft {find_index_of_minimum(lst_test, 3)} in plaats van 4"


def test_selection_sort():
    lst_test = random.choices(range(-99, 100), k=6)
    lst_copy = lst_test.copy()
    lst_output = selection_sort(lst_test)

    assert lst_copy == lst_test, "Fout: my_sort(lst) verandert de inhoud van lijst lst"
    assert lst_output == sorted(lst_test), \
        f"Fout: selection_sort({lst_test}) geeft {lst_output} in plaats van {sorted(lst_test)}"


if __name__ == '__main__':
    try:
        print("\x1b[0;32m")

        test_swap()
        print("Je functie swap() werkt goed!")

        test_find_index_of_minimum()
        print("Je functie find_index_of_minimum() werkt goed!")

        test_selection_sort()
        print("Je selection sort algoritme werkt goed!\n\nKnap gedaan!\n")

        print("\x1b[0;30m")
        aantal = int(input("Hoeveel getallen zal ik sorteren? "))
        lijst = random.choices(range(0, 100), k=aantal)

        print(f"De lijst: \n\t{lijst}")
        gesorteerde_lijst = selection_sort(lijst)
        print(f"is na sortering: \n\t{gesorteerde_lijst}")

    except AssertionError as ae:
        print("\x1b[0;31m")
        print(ae)
