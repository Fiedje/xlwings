def monat(i: int):
    return 1 + i % 12


def jahr(i: int):
    return int(1 + i / 12)


def jahr_v(i: int):
    return jahr(i - 12)


def jahr_n(i: int):
    return jahr(i + 12)


def k1m(i: int):
    return monat(i) - 1


def k2m(i: int):
    return monat(i) % 12


def k1j(i: int):
    return jahr(i) - 1


def k2j(i: int):
    if monat(i) == 12:
        return jahr(i)
    else:
        return jahr(i) - 1


def getTimeFraction(i):
    return k2j(i) - k1j(i) + (k2m(i) - k1m(i)) / 12.0


def getZahlungsweiseNumber(s):
    if s == "MONATLICH":
        return 12
    if s == "VIERTELJAEHRLICH":
        return 4
    if s == "HALBJAEHRLICH":
        return 2
    if s == "JAEHRLICH":
        return 1
    if s == "EINMALBETRAG":
        return 0
