from calculations.technische_daten import *
from calculations.beispielrechnung import Beispielrechnung


class Ueberschusszuteilung(Beispielrechnung):
    def __init__(self, product, contract):
        Beispielrechnung.__init__(self, product, contract)

    # Vorschuessig
    def uebV_Grund(self, i):
        if jahr(i) <= self.beitragslaufzeit and monat(i) == 1:
            return round(self.versicherungsSumme * self.grundueberschuss * 100) / 100
        else:
            return 0

    def uebV_Risk(self, i):
        if 3 <= jahr(i) <= self.vertragslaufzeit and monat(i) == 1:
            return round(self.jahresbtg_o_SumRat * self.risikoueberschuss * 100) / 100
        else:
            return 0

    def uebV_Zins(self, i):
        if 4 <= jahr(i) <= self.vertragslaufzeit and monat(i) == 1:
            return round(self.tarres(i - 12) * self.zinsueberschuss * 100) / 100
        else:
            return 0

    def uebV_Ges(self, i):
        return self.uebV_Grund(i) + self.uebV_Risk(i) + self.uebV_Zins(i) + self.verAns(i)

    # Nachschuessig
    def verAns(self, i):
        if monat(i) == 1 < jahr(i) <= self.vertragslaufzeit:
            return self.uebV_Ges(i - 12) * (1.0 + self.ansammlungszins)
        else:
            return 0

    def sgaerr(self, i):
        if 2 <= jahr(i - 1) <= self.vertragslaufzeit:
            return jahr(i - 1) * self.versicherungsSumme * self.schlussueberschusssatzanteilssatz
        else:
            return 0
