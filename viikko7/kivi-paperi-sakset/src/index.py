from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus == "a":
            KPSPelaajaVsPelaaja()
        elif vastaus == "b":
            KPSTekoaly()
        elif vastaus == "c":
            KPSParempiTekoaly()
        else:
            break


if __name__ == "__main__":
    main()
