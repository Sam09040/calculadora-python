import unittest
from calculadora import logaritmo_base10

class TestCalculadora(unittest.TestCase):
    def teste_logaritmo_base10(self):
        # Teste com valor 100
        resultado = logaritmo_base10(100)
        esperado = 2.0
        self.assertEqual(resultado, esperado, f"Esperado: {esperado}, mas obtido: {resultado}")
        
    def teste_logaritmo_base10_erro(self):
        # Teste com valor 0
        assert(logaritmo_base10(0) == "Erro: Logaritmo de número não positivo")
        # Teste com valor negativo
        assert(logaritmo_base10(-5) == "Erro: Logaritmo de número não positivo")
