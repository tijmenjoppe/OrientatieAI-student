""" coding=utf-8

Analytical Skills - practicum 1: getallen

(c) 2019 Hogeschool Utrecht
Bart van Eijkelenburg (bart.vaneijkelenburg@hu.nl)
Tijmen Muller (tijmen.muller@hu.nl)


Naam:
Klas: 
Studentnummer:
"""

"""
    LET OP: JE MAG VOOR DEZE OPDRACHT GEEN (extra) MODULES IMPORTEREN!

    Practicum 1: Werk onderstaande functies uit.

        floor(real):
            Return het grootste gehele getal, dat kleiner dan of gelijk is aan real (reël getal).

        ceil(real):
            Return het kleinste gehele getal, groter dan of gelijk aan real (reël getal).

        div(n):
            Return een (natuurlijk) gesorteerde verzameling (lijst) van delers van n. 
            Het getal a ∈ N is een deler van n ∈ N, als er een b ∈ N is, zodat a · b = n.

        is_prime(n):
            Return True als n ∈ N een priemgetal is, anders False.

        primefactors(n):    
            Return een (natuurlijk) gesorteerde verzameling (lijst) van priemfactoren van n. 
            Return [n] als n een priemgetal is, of n == 1. Tip: maak gebruik van de functie 'is_prime(n)'

        primes_under_30():  
            Return alle priemgetallen kleiner dan 30.

        gcd(a, b):          
            Return de grootste grootste gemene deler, ggd (ofwel greatest common divisor, gcd) is. 
            Je hebt twee opties voor deze opgave;
                1. Je programmeert hier het algoritme van Euclides (niet behandeld)
                    zie: https://nl.wikipedia.org/wiki/Algoritme_van_Euclides
                2. Je bedenkt zelf een oplossing waarbij je gebruik maakt van de eerder 
                    geschreven methode div(n) om de gcd te bepalen.

        lcm(a, b):
            Return het kleinste gemene veelvoud, kvg (ofwel least common multiple).

        add_frac(n1, d1, n2, d2):
            Return de sommatie van twee breuken als breuk.
            *n1* is de teller van de eerste breuk, *d1* is de noemer van de eerste breuk.
            *n2* is de teller van de tweede breuk, *d2* is de noemer van de eerste breuk.
            De returnwaarde bestaat uit eerste de teller en dan de noemer van het resultaat.
            Bijvoorbeeld: 3/4 + 1/6 = 11/12
                     dan: add_frac(3, 4, 1, 6) = 11, 12
"""


def floor(real):
    """ Return het grootste gehele getal, dat kleiner dan of gelijk is aan real (reëel getal). """

    return 0


def ceil(real):
    """ Return het kleinste gehele getal, groter dan of gelijk aan real (reëel getal). """

    return 0


def div(n):
    """ Return een (natuurlijk) gesorteerde verzameling (lijst) van delers van n. 
        Het getal a ∈ N is een deler van n ∈ N, als er een b ∈ N is, zodat a · b = n. """
    
    divisors = []
    return sorted(divisors)


def is_prime(n):
    """ Return True als n ∈ N een priemgetal is, anders False.
        Je kunt gebruik maken van de functie 'div(n)' om te bepalen of n een priem is.
        Optioneel: bedenk een efficiënter alternatief. """

    return False


def primefactors(n):
    """ Return een (natuurlijk) gesorteerde verzameling (lijst) van priemfactoren van n. 
        Return [n] als n een priemgetal is, of n == 1. Tip: maak gebruik van de functie 'is_prime(n)' """

    factors = []
    return sorted(factors)


def primes_under_30():
    """ Return alle priemgetallen kleiner dan 30. """

    primes = []
    return primes


def gcd(a, b):
    """ Return de grootste grootste gemene deler, ggd (ofwel greatest common divisor, gcd) is. """

    return 1


def lcm(a, b):
    """ Return het kleinste gemene veelvoud, kvg (ofwel least common multiple). """

    return 1


def add_frac(n1, d1, n2, d2):
    """ Return de sommatie van twee breuken als breuk.
        *n1* is de teller van de eerste breuk, *d1* is de noemer van de eerste breuk.
        *n2* is de teller van de tweede breuk, *d2* is de noemer van de eerste breuk.
        De returnwaarde bestaat uit eerste de teller en dan de noemer van het resultaat.
        Bijvoorbeeld: 3/4 + 1/6 = 11/12
                 dan: add_frac(3, 4, 1, 6) = 11, 12
    """

    return 1, 1


"""
========================================================================================================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""


def my_assert_args(function, args, expected_output):
    argstr = str(args).replace(',)', ')')
    assert function(*args) == expected_output, "Fout: {}{} geeft {} in plaats van {}".format(function.__name__, argstr, function(*args), expected_output)


def test_floor():
    testcases = [((1.0,),    1),
                 ((1.05,),   1),
                 ((1.95,),   1),
                 ((-1.0,),  -1),
                 ((-1.05,), -2),
                 ((-1.95,), -2)]

    for case in testcases:
        my_assert_args(floor, case[0], case[1])


def test_ceil():
    testcases = [((1.0,),    1),
                 ((1.05,),   2),
                 ((1.95,),   2),
                 ((-1.0,),  -1),
                 ((-1.05,), -1),
                 ((-1.95,), -1)]

    for case in testcases:
        my_assert_args(ceil, case[0], case[1])


def test_div():
    testcases = [ 
        ((1,),   [1]),
        ((2,),   [1, 2]),
        ((3,),   [1, 3]),
        ((4,),   [1, 2, 4]),
        ((8,),   [1, 2, 4, 8]),
        ((12,),  [1, 2, 3, 4, 6, 12]),
        ((19,),  [1, 19]),
        ((25,),  [1, 5, 25]),
        ((929,), [1, 929]),
        ((936,), [1, 2, 3, 4, 6, 8, 9, 12, 13, 18, 24, 26, 36, 39, 52, 72, 78, 104, 117, 156, 234, 312, 468, 936])
    ]

    for case in testcases:
        my_assert_args(div, case[0], sorted(case[1]))


def test_primefactors():
    testcases = [ 
        ((1,),    [1]),
        ((2,),    [2]),
        ((3,),    [3]),
        ((4,),    [2, 2]),
        ((8,),    [2, 2, 2]),
        ((12,),   [2, 2, 3]),
        ((2352,), [2, 2, 2, 2, 3, 7, 7]),
        ((9075,), [3, 5, 5, 11, 11])
    ]

    for case in testcases:
        my_assert_args(primefactors, case[0], sorted(case[1]))


def test_primes_under_30():
    expected_output = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert sorted(primes_under_30()) == expected_output, "Fout: primes_under_30() geeft {} in plaats van {}".format(primes_under_30(), expected_output)


def test_gcd():
    testcases = [ 
        ((60, 70), 10)
    ]
    
    for case in testcases:
        my_assert_args(gcd, case[0], case[1])


def test_lcm():
    testcases = [ 
        ((15, 27), 135)
    ]

    for case in testcases:
        my_assert_args(lcm, case[0], case[1])


def test_add_frac():
    testcases = [
        ((1, 2, 1, 4), (3, 4)),
        ((3, 4, 1, 6), (11, 12)),
        ((1, 6, 3, 4), (11, 12))
    ]

    for case in testcases:
        my_assert_args(add_frac, case[0], case[1])


if __name__ == '__main__':
    try: 
        print("\x1b[0;32m")

        test_floor()
        print("Je functie floor() werkt goed!")

        test_ceil()
        print("Je functie ceil() werkt goed!")

        test_div()
        print("Je functie div(n) werkt goed!")

        test_primefactors()
        print("Je functie primefactors(n) werkt goed!")

        test_primes_under_30()
        print("Je functie primes_under_30() werkt goed!")

        test_gcd()
        print("Je functie gcd(a, b) werkt goed!")

        test_lcm()
        print("Je functie lcm(a, b) werkt goed!")

        test_add_frac()
        print("Je functie add_frac(n1, d1, n2, d2) werkt goed!")

        print("Gefeliciteerd, alles lijkt te werken! Lever je werk nu in op Canvas...")
        
    except AssertionError as ae:
        print("\x1b[0;31m" + str(ae))
