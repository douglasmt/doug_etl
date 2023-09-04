import unittest

from unit_test_atividades import comer, dormir


class AtividadesTeste(unittest.TestCase):

    # Testes para dormir
    def test_comida_saudavel(self):
        """Teste da comida saudável"""
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.'
        )

    def test_comida_gostosa(self):
        """Teste da comida gostosa"""
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),
            'Estou comendo pizza porque a gente só vive uma vez.'
        )

    # Testes para dormir
    def test_dormir_pouco(self):
        """Teste do sono insuficiente"""
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir por 4 horas. :('
        )

    def test_dormir_muito(self):
        """Teste do sono excessivo"""
        self.assertEqual(
            dormir(10),
            'Puts, dormi muito e atrasei para o trabalho!'
        )


if __name__ == '__main__':
    unittest.main()

