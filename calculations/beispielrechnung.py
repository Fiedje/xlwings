from calculations.technische_daten import *
from calculations.beitraege import Beitraege


class Beispielrechnung(Beitraege):
    def __init__(self, product, contract):
        Beitraege.__init__(self, product, contract)

    def tarres(self, i):
        if k1j(i) <= self.vertragslaufzeit:
            return self.versicherungsSumme * self.lbw(i) - self.jahresbtg_o_SumRat * self.bbw(i)
        else:
            return 0

    def offene_AK(self, i):
        if jahr(i) <= 5:
            a = round(self.ak_volumen * 100 / 60.0) / 100
            return (5.0 * 12.0 - (k1j(i) * 12.0 + k1m(i))) * a
        else:
            return 0

    def garres(self, i):
        return self.offene_AK(i) + self.tarres(i)

    def rkw_min(self, i):
        if jahr(i) <= self.vertragslaufzeit:
            a = self.garres(i) - 0.015 * (self.versicherungsSumme - self.garres(i))
            return a
            # return max(a, 0) # EXCEL SHEET HAT DAS NICHT DRIN ...
        else:
            return 0

    def stoab(self, i):
        if jahr(i) <= self.vertragslaufzeit and k1j(i) < min(20.0, 2.0 * self.vertragslaufzeit / 3.0):
            return self.garres(i) - self.rkw_min(i)
        else:
            return 0

    def rkw(self, i):
        return round(max(self.tarres(i) - self.stoab(i), self.rkw_min(i)) * 100) / 100

    def sue(self, i):
        if jahr(i - 1) <= self.vertragslaufzeit:
            return self.sgaerr(i) * ((1 / (1 + self.schlussueberschusssabzinssatz)) ** (self.vertragslaufzeit - jahr(i - 1)))
            # return self.sgaerr(i) * (1.0 / (1.0 + self.schlussueberschusssabzinssatz))\
            #       ** (self.vertragslaufzeit - jahr_v(i))
        else:
            return 0

    def akt_leist(self, i):
        if k1j(i) <= self.vertragslaufzeit:
            if monat(i) == 1:
                return self.versicherungsSumme + self.verAns(i) + self.sue(i)
            else:
                return self.akt_leist(i - 1)
        else:
            return 0
