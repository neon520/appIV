import sure
import webapp2
import gestorhtml

class TestStringMethods:
        def test_empresas(self):
            request = webapp2.Request.blank('/empresas')
            response = request.get_response(gestorhtml.Server())
            #self.assertTrue('Empresas registradas' in response.body)
            (response.body).should.contain('Empresas registradas')

        def test_borrarCalificacion(self):
            request = webapp2.Request.blank('/borrarCalificacion')
            response = request.get_response(gestorhtml.Server())
            #self.assertTrue('Borrado de una Calific' in response.body)
            (response.body).should.contain('Borrado de una Calific')

        def test_calificaciones(self):
            request = webapp2.Request.blank('/calificaciones')
            response = request.get_response(gestorhtml.Server())
            #self.assertTrue('Calificaciones registradas' in response.body)
            (response.body).should.contain('Calificaciones registradas')

        def test_registroCalificar(self):
            request = webapp2.Request.blank('/registroCalificar')
            response = request.get_response(gestorhtml.Server())
            #self.assertTrue('Registro de una Calific' in response.body)
            (response.body).should.contain('Registro de una Calific')

        def test_registroEmpresa(self):
            request = webapp2.Request.blank('/registroEmpresa')
            response = request.get_response(gestorhtml.Server())
            #self.assertTrue('Registro de la empresa' in response.body)
            (response.body).should.contain('Registro de la empresa')

        def test_registroUsuario(self):
            request = webapp2.Request.blank('/registroUsuario')
            response = request.get_response(gestorhtml.Server())
            #self.assertTrue('Registro de alumno' in response.body)
            (response.body).should.contain('Registro de alumno')

        def test_base(self):
            request = webapp2.Request.blank('/')
            response = request.get_response(gestorhtml.Server())
            #self.assertTrue('n de empresas' in response.body)
            (response.body).should.contain('n de empresas')

