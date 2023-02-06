from calculations.technische_daten import *
from calculations.barwerte import Barwerte


class Beitraege(Barwerte):
    def __init__(self, product, contract):
        Barwerte.__init__(self, product, contract)

        self.jahresbtg_o_SumRat = round(
            self.versicherungsSumme * self.lbw(0) / (self.bbw(0) - self.vertragslaufzeit * self.res_alpha) * 100) / 100

        self.ak_volumen = round((self.beitragslaufzeit * self.jahresbtg_o_SumRat) * self.res_alpha * 100) / 100

        if self.jahresbtg_o_SumRat <= 3000:
            self.sumrabatt = -0.003
        elif self.jahresbtg_o_SumRat <= 4000:
            self.sumrabatt = -0.002
        elif self.jahresbtg_o_SumRat <= 5000:
            self.sumrabatt = -0.001
        elif self.jahresbtg_o_SumRat <= 10000:
            self.sumrabatt = 0.0005
        elif self.jahresbtg_o_SumRat <= 25000:
            self.sumrabatt = 0.0013
        elif self.jahresbtg_o_SumRat <= 50000:
            self.sumrabatt = 0.0017
        else:
            self.sumrabatt = 0.002

        self.jahresbtg_o_Rat = self.jahresbtg_o_SumRat + self.versicherungsSumme * self.sumrabatt

        if self.zahlungsweise == "EINMALBETRAG":
            self.jahresbtg = self.jahresbtg_o_Rat
        else:
            self.jahresbtg = round((self.jahresbtg_o_Rat + self.jahresbtg_o_Rat * self.ratenzuschlag())
                                   / self.zw() * 100) / 100 * self.zw()

        if self.zahlungsweise == "EINMALBETRAG":
            self.btg = self.jahresbtg
        else:
            self.btg = self.jahresbtg / self.zw()

    def akla(self, i):
        if jahr(i) <= self.beitragslaufzeit:
            return round(getTimeFraction(i) * self.versicherungsSumme * self.bpfl_gamma * 100) / 100
        else:
            return 0

    def inka(self, i):
        if jahr(i) <= self.beitragslaufzeit:
            return round(getTimeFraction(i) * self.jahresbtg_o_SumRat * self.ink_beta * 100) / 100
        else:
            return 0

    def ratzu(self, i):
        if jahr(i) <= self.beitragslaufzeit:
            return getTimeFraction(i) * self.jahresbtg_o_Rat * self.ratenzuschlag()
        else:
            return 0

    def sumrab(self, i):
        if jahr(i) <= self.beitragslaufzeit:
            return getTimeFraction(i) * self.versicherungsSumme * self.sumrabatt
        else:
            return 0

    def vwSum(self, i):
        return self.akla(i) + self.inka(i) + self.ratzu(i) + self.sumrab(i)

    def res_begin(self, i):
        if jahr(i) < self.vertragslaufzeit:
            return self.versicherungsSumme * self.lbw(i) - self.jahresbtg_o_SumRat * self.bbw(i)
        else:
            return 0

    def res_beginn_jahr(self, i):
        return self.res_begin((jahr(i) - 1) * 12)

    def res_end(self, i):
        return self.res_begin(i + 1)

    def res_end_jahr(self, i):
        return self.res_begin(jahr(i) * 12)

    def rb(self, i):
        if jahr(i) <= self.beitragslaufzeit:
            return getTimeFraction(i) * (1.0 / (1 + self.rz)) * self.qx(self.alter + jahr(i)) \
                   * (self.versicherungsSumme - self.res_end(i))
        else:
            return 0

    def rzres(self, i):
        if jahr(i) <= self.beitragslaufzeit:
            return (1.0 - 1.0 / (1.0 + self.rz)) * self.res_end_jahr(i)
        else:
            return 0

    def sb(self, i):
        if jahr(i) <= self.beitragslaufzeit:
            return getTimeFraction(i) * (self.res_end_jahr(i) - self.res_beginn_jahr(i) - self.rzres(i))
        else:
            return 0

    def risk_kapital(self, i):
        if jahr(i) <= self.vertragslaufzeit:
            return self.versicherungsSumme - self.res_end(i)
        else:
            return 0