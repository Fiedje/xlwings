from calculations.technische_daten import *
from calculations.tarif import Tarif
from calculations import contract
from calculations import product
import xlwings as xl
import sys
import os
sys.path.append(os.pardir)


K2_08 = Tarif(product.K2_08, contract.ID_51)


wb = xl.Book("calculations/referenzrechner.xlsx")
try:
    sht = wb.sheets["K2_08"]
    sht.clear()
except ValueError:
    sht = wb.sheets.add("K2_08")

info_line = 3
def append_value(label, value):
    sht.range("A" + str(info_line)).value = label
    sht.range("B" + str(info_line)).value = value
    globals()["info_line"] = info_line + 1


append_value("Jahresbeitrag", K2_08.jahresbtg)
append_value("Jahresbeitrag_o_Ratzu", K2_08.jahresbtg_o_Rat)
append_value("Jahresbeitrag_o_sumrab_ratzu", K2_08.jahresbtg_o_SumRat)
append_value("AK_Volumen", K2_08.ak_volumen)
append_value("Versicherungssumme", K2_08.versicherungsSumme)
append_value("Alter", K2_08.alter)
append_value("Vertragslaufzeit", K2_08.vertragslaufzeit)
append_value("Beitragslaufzeit", K2_08.beitragslaufzeit)
if K2_08.geschlecht == "F":
    append_value("Geschlecht", "Weiblich")
elif K2_08.geschlecht == "M":
    append_value("Geschlecht", "Männlich")
append_value("Rechnungszins", K2_08.rz)
append_value("res_alpha", K2_08.res_alpha)
append_value("ink_beta", K2_08.ink_beta)
append_value("bpfl_gamma", K2_08.bpfl_gamma)
append_value("bfr_gamma", K2_08.bfr_gamma)
append_value("ratzu", K2_08.ratenzuschlag())
append_value("sumrab", K2_08.sumrabatt)
append_value("Zinsüberschuss", K2_08.zinsueberschuss)
append_value("Risikoüberschuss", K2_08.risikoueberschuss)
append_value("Ansammlungszins", K2_08.ansammlungszins)
append_value("Schlussüberschussabzinssatz", K2_08.schlussueberschusssabzinssatz)
append_value("Schlussüberschussanteilssatz", K2_08.schlussueberschusssatzanteilssatz)
append_value("Grundüberschuss", K2_08.grundueberschuss)


sht.range("D2").value = "Monat"
sht.range("E2").value = "Jahr"
sht.range("F2").value = "Datum"

sht.range("H2").value = "lbw"
sht.range("I2").value = "lbw_jahr"
sht.range("J2").value = "lbw_jahr_n"
sht.range("K2").value = "bbw"
sht.range("L2").value = "bbw_jahr"
sht.range("M2").value = "bbw_jahr_n"
sht.range("O2").value = "VerAns"
sht.range("P2").value = "sgaerr"
sht.range("R2").value = "tarres"
sht.range("S2").value = "offene AK"
sht.range("T2").value = "Garres"
sht.range("U2").value = "Min. RKW"
sht.range("V2").value = "Stornoabschlag"
sht.range("W2").value = "RKW"
sht.range("X2").value = "Sue"
sht.range("Y2").value = "Akt_leist"
sht.range("AA2").value = "Grundüberschuss"
sht.range("AB2").value = "Risikoüberschuss"
sht.range("AC2").value = "Zinsüberschuss"
sht.range("AD2").value = "Gesamter Überschuss"
sht.range("AF2").value = "akla"
sht.range("AG2").value = "inka"
sht.range("AH2").value = "ratzu"
sht.range("AI2").value = "sumrab"
sht.range("AJ2").value = "vwSum"
sht.range("AK2").value = "Res_Beginn"
sht.range("AL2").value = "Res_Beginn_Jahr"
sht.range("AM2").value = "Res_End"
sht.range("AN2").value = "Res_End_Jahr"
sht.range("AO2").value = "rzres"
sht.range("AP2").value = "Risikobeitrag"
sht.range("AQ2").value = "Sparbeitrag"
sht.range("AR2").value = "Risk. Kapital"

for x in range(max(K2_08.beitragslaufzeit, K2_08.vertragslaufzeit) * 12 + 1):
    line = str(3 + x)
    sht.range("D" + line).value = monat(x)
    sht.range("E" + line).value = jahr(x)

    sht.range("H" + line).value = K2_08.lbw(x)
    sht.range("I" + line).value = K2_08.lbw_jahr(x)
    sht.range("J" + line).value = K2_08.lbw_jahr_n(x)
    sht.range("K" + line).value = K2_08.bbw(x)
    sht.range("L" + line).value = K2_08.bbw_jahr(x)
    sht.range("M" + line).value = K2_08.bbw_jahr_n(x)

    sht.range("O" + line).value = K2_08.verAns(x)
    sht.range("P" + line).value = K2_08.sgaerr(x)

    sht.range("R" + line).value = K2_08.tarres(x)
    sht.range("S" + line).value = K2_08.offene_AK(x)
    sht.range("T" + line).value = K2_08.garres(x)
    sht.range("U" + line).value = K2_08.rkw_min(x)
    sht.range("V" + line).value = K2_08.stoab(x)
    sht.range("W" + line).value = K2_08.rkw(x)
    sht.range("X" + line).value = K2_08.sue(x)
    sht.range("Y" + line).value = K2_08.akt_leist(x)

    sht.range("AA" + line).value = K2_08.uebV_Grund(x)
    sht.range("AB" + line).value = K2_08.uebV_Risk(x)
    sht.range("AC" + line).value = K2_08.uebV_Zins(x)
    sht.range("AD" + line).value = K2_08.uebV_Ges(x)

    sht.range("AF" + line).value = K2_08.akla(x)
    sht.range("AG" + line).value = K2_08.inka(x)
    sht.range("AH" + line).value = K2_08.ratzu(x)
    sht.range("AI" + line).value = K2_08.sumrab(x)
    sht.range("AJ" + line).value = K2_08.vwSum(x)

    sht.range("AK" + line).value = K2_08.res_begin(x)
    sht.range("AL" + line).value = K2_08.res_beginn_jahr(x)
    sht.range("AM" + line).value = K2_08.res_end(x)
    sht.range("AN" + line).value = K2_08.res_end_jahr(x)

    sht.range("AO" + line).value = K2_08.rzres(x)
    sht.range("AP" + line).value = K2_08.rb(x)
    sht.range("AQ" + line).value = K2_08.sb(x)
    sht.range("AR" + line).value = K2_08.risk_kapital(x)
sht.autofit()

sht.range("A1").value = "Allgemeine Daten"
sht.range("D1").value = "technische Daten"
sht.range("H1").value = "Barwerte"
sht.range("O1").value = "Nachschüssige Überschusszahlung"
sht.range("R1").value = "Beispielrechnung"
sht.range("AA1").value = "Vorschüssige Überschusszuteilung"
sht.range("AF1").value = "Beitragszerlegung"
sht.range("A1:AZ1").api.Font.Bold = True
sht.range("A2:AZ2").api.Font.Italic = True
wb.save()
