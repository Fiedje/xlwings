from calculations.technische_daten import *
from calculations.base import Base


class Barwerte(Base):
    def __init__(self, product, contract):
        Base.__init__(self, product, contract)

        self.lbw_jahr_ = []
        for j in range(self.laufzeit()):
            i = j * 12
            year_xk = self.alter + jahr(i) - 1
            year_xn = self.alter + self.vertragslaufzeit
            year_xm = self.alter + self.beitragslaufzeit

            Dxk = self.Dx(year_xk)
            Dxn = self.Dx(year_xn)

            Mxk = self.Mx(year_xk)
            Mxn = self.Mx(year_xn)

            Nxk = self.Nx(year_xk)
            Nxn = self.Nx(year_xn)
            Nxm = self.Nx(year_xm)

            f1 = (Dxn + Mxk - Mxn) / Dxk
            f2 = self.bfr_gamma * ((Nxk - Nxn) / Dxk - (Nxk - Nxm) / Dxk)
            f3 = self.bpfl_gamma * (Nxk - Nxm) / Dxk

            if jahr(i) < self.beitragslaufzeit:
                self.lbw_jahr_.append(f1 + f2 + f3)
            else:
                self.lbw_jahr_.append(f1 + f2)

        self.bbw_jahr_ = []
        for j in range(self.beitragslaufzeit):
            i = j * 12

            year_xk = self.alter + jahr(i) - 1
            year_xm = self.alter + self.beitragslaufzeit

            Nxk = self.Nx(year_xk)
            Nxm = self.Nx(year_xm)
            Dxk = self.Dx(year_xk)

            self.bbw_jahr_.append((1 - self.ink_beta) * (Nxk - Nxm) / Dxk)

    def lbw_jahr(self, i):
        if 1 <= jahr(i) < len(self.lbw_jahr_):
            return self.lbw_jahr_[jahr(i) - 1]
        else:
            return 0

    def lbw_jahr_n(self, i):
        return self.lbw_jahr(i + 12)

    def lbw(self, i):
        t = k1m(i) / 12.0
        return (1 - t) * self.lbw_jahr(i) + t * self.lbw_jahr_n(i)

    def bbw_jahr(self, i):
        if 1 <= jahr(i) < len(self.bbw_jahr_):
            return self.bbw_jahr_[jahr(i) - 1]
        else:
            return 0

    def bbw_jahr_n(self, i):
        return self.bbw_jahr(i + 12)

    def bbw(self, i):
        t = k1m(i) / 12.0
        return (1.0 - t) * self.bbw_jahr(i) + t * self.bbw_jahr_n(i)
