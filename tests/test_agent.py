import unittest
from agente_ucv.agent import explicar_concepto, calcular_promedio

class TestAgenteUCV(unittest.TestCase):

    def test_explicar_concepto_valido(self):
        resultado = explicar_concepto("api")
        self.assertEqual(resultado["status"], "success")
        self.assertIn("comunicación", resultado["explicacion"])

    def test_explicar_nuevos_conceptos(self):
        resultado = explicar_concepto("docker")
        self.assertEqual(resultado["status"], "success")
        self.assertIn("contenedores", resultado["explicacion"])

    def test_explicar_concepto_inexistente(self):
        resultado = explicar_concepto("inexistente")
        self.assertEqual(resultado["status"], "not_found")

    def test_calcular_promedio_exitoso(self):
        notas = [14, 16, 18]
        resultado = calcular_promedio(notas)
        self.assertEqual(resultado["status"], "success")
        self.assertEqual(resultado["promedio"], 16.0)

    def test_calcular_promedio_validacion_error(self):
        resultado_vacio = calcular_promedio([])
        self.assertEqual(resultado_vacio["status"], "error")
        
        resultado_invalido = calcular_promedio([15, "dieciseis", 18])
        self.assertEqual(resultado_invalido["status"], "error")

if __name__ == '__main__':
    unittest.main()