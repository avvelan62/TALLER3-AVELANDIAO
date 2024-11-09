import unittest
from boa_constricutor import Boa_Constrictor

class TestBoa(unittest.TestCase):
    def setUp(self) -> None:
        pass
    
    def tearDown(self) -> None:
        pass
    
    def test_hacer_sonido_boa(self):
        boa = Boa_Constrictor("Snake", 6, 12.1, "Argentina", 240.1)
        self.assertEqual(boa.hacer_sonido(), "¡Tsss!")

    def test_calcular_flete_boa(self):
        boa = Boa_Constrictor("Snake", 6, 12.1, "Argentina", 240.1)
        self.assertEqual(boa.calcular_flete(boa._impuestos, boa._peso), 2905.21)
    
    def test_alimentar_boa(self):
        boa = Boa_Constrictor("Snake", 6, 12.1, "Argentina", 240.1)
        boa.comer_raton(1)
        self.assertEqual(boa.contar_ratones_comidos(), 1)


if __name__ == '__main__':
    unittest.main()