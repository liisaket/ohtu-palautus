from tekoaly import Tekoaly
from kivi_paperi_sakset import KiviPaperiSakset


class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.tekoaly = Tekoaly()
        KiviPaperiSakset.pelaa(self)

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto