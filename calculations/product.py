from calculations.xml_parser import parse


class Product:
    def __init__(self):
        self.tarifName: str = None
        self.tarifNummer: int = None
        self.rz: float = None
        self.rz2: float = None
        self.aos: str = None
        self.aos2: str = None
        self.Modifikation_fuer_gar_Rentenfaktor: float = None
        self.res_alpha: float = None
        self.lr_alpha: float = None
        self.bei_alpha: float = None
        self.alpha_min: float = None
        self.alpha_mindauer: float = None
        self.alpha_maxdauer: float = None
        self.ink_beta: float = None
        self.beta_min: float = None
        self.beta_mindauer: float = None
        self.beta_maxdauer: float = None
        self.bpfl_gamma: float = None
        self.bfr_gamma: float = None
        self.bfr_gamma_Bonus: float = None
        self.rent_gamma: float = None
        self.gamma_abs: float = None
        self.gamma_fvm: float = None
        self.gamma_ufa: float = None
        self.gamma_an: float = None
        self.ratenzuschlaege: dict = dict()
        self.praemienrabatt: float = None
        self.nachschuessiger_Kostenueberschuss: float = None
        self.vorschuessiger_Kostenueberschuss: float = None
        self.zinsueberschuss: float = None
        self.risikoueberschuss: float = None
        self.ansammlungszins: float = None
        self.schlussueberschusssabzinssatz: float = None
        self.schlussueberschusssatzanteilssatz: float = None
        self.grundueberschuss: float = None
        self.direktgutschrift: float = None
        self.stosatz: float = None
        self.mindestrente: float = None
        self.rentengarantiezeit: float = None
        self.prozentsatz_min_risk_lst: float = None
        self.prozentsatz_min_tod_lst: float = None
        self.unisexpara: float = None
        self.sizu: float = None
        self.param_rissel: float = None


def create_from_xml(path):
    return parse(Product(), path)
