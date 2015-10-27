import unittest
import webapp2
import __main__

class TestStringMethods(unittest.TestCase):
        def test_empresas(self):
            request = webapp2.Request.blank('/empresas')
            response = request.get_response(__main__.app)
            self.assertTrue('Empresas registradas' in response.body)

        def test_borrarCalificacion(self):
            request = webapp2.Request.blank('/borrarCalificacion')
            response = request.get_response(__main__.app)
            self.assertTrue('Borrado de una Calific' in response.body)

        def test_calificaciones(self):
            request = webapp2.Request.blank('/calificaciones')
            response = request.get_response(__main__.app)
            self.assertTrue('Calificaciones registradas' in response.body)

        def test_registroCalificar(self):
            request = webapp2.Request.blank('/registroCalificar')
            response = request.get_response(main.app)
            self.assertTrue('Registro de una Calific' in response.body)

        def test_registroEmpresa(self):
            request = webapp2.Request.blank('/registroEmpresa')
            response = request.get_response(__main__.app)
            self.assertTrue('Registro de la empresa' in response.body)

        def test_registroUsuario(self):
            request = webapp2.Request.blank('/registroUsuario')
            response = request.get_response(__main__.app)
            self.assertTrue('Registro de alumno' in response.body)

        def test_base(self):
            request = webapp2.Request.blank('/')
            response = request.get_response(__main__.app)
            self.assertTrue('n de empresas' in response.body)

if __name__ == '__main__':
    unittest.main()