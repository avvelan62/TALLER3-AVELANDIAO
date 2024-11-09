import unittest
from huron import Huron

class TestHuron(unittest.TestCase):
    def setUp(self) -> None:
        pass
    
    def tearDown(self) -> None:
        pass

    def test_hacer_sonido_boa(self):
        huron = Huron("Crash", 2, 2.1, "Uruguay", 12.2)
        self.assertEqual(huron.hacer_sonido(), "¡Eek, Eek!")

    def test_calcular_flete_boa(self):
        huron = Huron("Crash", 2, 2.1, "Uruguay", 12.2)
        self.assertEqual(huron.calcular_flete(huron._impuestos, huron._peso), 25.62)
    

if __name__ == '__main__':
    unittest.main()