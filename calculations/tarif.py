from calculations.ueberschusszuteilung import Ueberschusszuteilung


class Tarif(Ueberschusszuteilung):
    def __init__(self, product, contract):
        Ueberschusszuteilung.__init__(self, product, contract)
