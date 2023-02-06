from calculations import xml_parser


class Contract:
    def __init__(self):
        self.testfallName: str = None
        self.tarifName: str = None
        self.testfallNummer: int = None
        self.alter: str = None
        self.geschlecht: str = None
        self.geburtsjahr: int = None
        self.beitrag: float = None
        self.versicherungsSumme: float = None
        self.rentenhoehe: float = None
        self.zahlungsweise: str = None
        self.zahlungsweise_exkasso: str = None
        self.renteneintrittsalter: int = None
        self.vertragsbeginn: str = None
        self.vertragslaufzeit: int = None
        self.beitragslaufzeit: int = None
        self.beitragsfreie_zeit: int = None
        self.ako_verteilung: str = None
        self.garantieniveau: float = None
        self.risikoklasse: int = None
        self.uebersterblichkeit: int = None
        self.ueberschussverwendungssystem: str = None
        self.antsatzfonds: float = None
        self.fondsverteilung: float = None

    def zw(self):
        if self.zahlungsweise == "MONATLICH":
            return 12
        if self.zahlungsweise == "VIERTELJAEHRLICH":
            return 4
        if self.zahlungsweise == "HALBJAEHRLICH":
            return 2
        if self.zahlungsweise == "JAEHRLICH":
            return 1
        if self.zahlungsweise == "EINMALBETRAG":
            return 0

    def ratenzuschlag(self):
        if self.zahlungsweise == "MONATLICH":
            return 0.05
        if self.zahlungsweise == "VIERTELJAEHRLICH":
            return 0.03
        if self.zahlungsweise == "HALBJAEHRLICH":
            return 0.02
        return 0

    def laufzeit(self):
        return max(self.vertragslaufzeit, self.beitragslaufzeit) + 1


def create_from_xml(path):
    return xml_parser.parse(Contract(), path)
