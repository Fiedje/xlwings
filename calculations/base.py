from pace.insurancemath.netpresentvalues import NetpresentValues
from calculations.contract import Contract
from calculations.product import Product


class Base(NetpresentValues, Contract, Product):
    def __init__(self, product, contract):
        for key, value in vars(product).items():
            setattr(self, key, value)
        for key, value in vars(contract).items():
            setattr(self, key, value)
        NetpresentValues.__init__(self, table=(self.aos + self.geschlecht), interest=self.rz * 100.0)
