from kivi_paperi_sakset import KiviPaperiSakset

class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def __init__(self):
        KiviPaperiSakset.pelaa(self)
    
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = input("Toisen pelaajan siirto: ")
        return tokan_siirto

