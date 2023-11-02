import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_etsi_palauttaa_pelaajan(self):
        pelaaja = self.stats.search("Kurri")
        self.assertEqual(pelaaja.name, "Kurri")
        self.assertEqual(pelaaja.team, "EDM")
        self.assertEqual(pelaaja.goals, 37)
        self.assertEqual(pelaaja.assists, 53)
    
    def test_etsi_palauttaa_none(self):
        pelaaja = self.stats.search("Griezmann")
        self.assertEqual(pelaaja, None)
    
    def test_tiimit_loytyy(self):
        pelaajat = self.stats.team("EDM")
        self.assertEqual(len(pelaajat), 3)
    
    def test_parhaat_pisteet(self):
        parhaat = self.stats.top(3)
        self.assertEqual(["Gretzky", "Lemieux", "Yzerman"], [i.name for i in parhaat])