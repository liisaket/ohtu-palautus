from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

def luo_peli(tyyppi):
    if tyyppi == "a":
        KPSPelaajaVsPelaaja()
    if tyyppi == "b":
        KPSTekoaly()
    if tyyppi == "c":
        KPSParempiTekoaly()
    
    return None