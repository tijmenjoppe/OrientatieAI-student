"""
Analytical Skills - opgave insertion sort

(c) 2019 Hogeschool Utrecht
Tijmen Muller (tijmen.muller@hu.nl)
"""

import random

def insert(lst, grens, waarde):
    """ Voegt de waarde op de juiste plek in het gesorteerde deel van lijst lst """
    # De lijst *lst* is gesorteerd van lst[0] t/m lst[grens]
    # Het element *waarde* wordt ingevoegd op de juiste plek in bovengenoemde gesorteerde deel,
    # dus hierna is de lijst *lst* gesorteerd van lst[0] t/m lst[grens+1]

    # Aanpak: begin bij index *grens* en verplaats elementen groter dan *waarde* naar rechts.
    # Als je een waarde tegenkomt die kleiner is dan *waarde* (of het begin van lijst *lst*),
    # dan voeg je *waarde* in op de vrijgekomen plek.

    pass


def insertion_sort(lst):
    """ Implementatie van het insertion sort algoritme die gegeven lijst lst sorteert """
    pass


"""
========================================================================================================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
def test_insert():
    lst_test = [3, 5, 7, 11, 13, 2, 9, 14]

    insert(lst_test, 4, 2)
    lst_correct = [2, 3, 5, 7, 11, 13, 9, 14]
    assert lst_test == lst_correct, "\x1b[0;31mFout: insert(lst_test, 4, 2) geeft {} in plaats van {}".format(lst_test, lst_correct)

    insert(lst_test, 5, 9)
    lst_correct = [2, 3, 5, 7, 9, 11, 13, 14]
    assert lst_test == lst_correct, "\x1b[0;31mFout: insert(lst_test, 5, 9) geeft {} in plaats van {}".format(lst_test, lst_correct)

    insert(lst_test, 6, 14)
    lst_correct = [2, 3, 5, 7, 9, 11, 13, 14]
    assert lst_test == lst_correct, "\x1b[0;31mFout: insert(lst_test, 6, 14) geeft {} in plaats van {}".format(lst_test, lst_correct)


def test_insertion_sort():
    lst_test = random.sample(range(-99, 100), 6)
    lst_copy = lst_test.copy()
    insertion_sort(lst_test)
    assert lst_test == sorted(lst_copy), "\x1b[0;31mFout: insertion_sort({}) geeft {} in plaats van {}".format(lst_copy, lst_test, sorted(lst_copy))


if __name__ == '__main__':
    try:
        test_insert()
        print("\x1b[0;32mJe functie insert() werkt goed!")

        test_insertion_sort()
        print("\x1b[0;32mJe insertion sort algoritme werkt goed!\n\nKnap gedaan!\n")
    except AssertionError as ae:
        print(ae)

    aantal = int(input("\x1b[0;30mHoeveel getallen zal ik sorteren? "))
    lst = list(range(aantal))
    random.shuffle(lst)

    print("De lijst: \n" + str(lst))
    insertion_sort(lst)
    print("is na sortering: \n" + str(lst))

