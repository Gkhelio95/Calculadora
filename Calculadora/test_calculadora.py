import unittest
from Calculadra import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_sumar(self):
        self.assertEqual(self.calc.sumar(2, 3), 5)
        self.assertEqual(self.calc.sumar(-2, -3), -5)
        self.assertEqual(self.calc.sumar(0, 0), 0)

    def test_restar(self):
        self.assertEqual(self.calc.restar(10, 4), 6)
        self.assertEqual(self.calc.restar(-1, -1), 0)
        self.assertEqual(self.calc.restar(0, 5), -5)

    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(3, 7), 21)
        self.assertAlmostEqual(self.calc.multiplicar(2.5, 4.2), 10.5)
        self.assertEqual(self.calc.multiplicar(-2, 3), -6)

    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)
        self.assertAlmostEqual(self.calc.dividir(5.5, 2.2), 2.5, places=2)
        self.assertEqual(self.calc.dividir(-6, 2), -3)

    def test_dividir_por_cero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.dividir(5, 0)

if __name__ == '__main__':
    unittest.main()
