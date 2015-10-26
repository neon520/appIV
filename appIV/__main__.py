
import datetime
import jinja2
import os
import webapp2
import cgi


from gestorbd import *



template_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.getcwd()))


def validaTexto(texto):
    if len(texto)>0:
        return True
    else:
        return False


class Empresa(webapp2.RequestHandler):

    def get(self):

        #Obtenemos todos los Alumnos registrados en el sistema.
        resultados = GestorEmpresa.getEmpresas()

        templateVars = {"empresas" : resultados}

        template = template_env.get_template('templates/empresas.html')
        #Cargamos la plantilla y le pasamos los datos cargardos
        self.response.out.write(template.render(templateVars))

class Usuario(webapp2.RequestHandler):

    def get(self):

        #Obtenemos todos los Alumnos registrados en el sistema.
        resultados = GestorUsuario.getUsuarios()

        templateVars = {"usuarios" : resultados}

        template = template_env.get_template('templates/usuarios.html')
        #Cargamos la plantilla y le pasamos los datos cargardos
        self.response.out.write(template.render(templateVars))

class Calificar(webapp2.RequestHandler):

    def get(self):

        #Obtenemos todos los Alumnos registrados en el sistema.
        resultados = GestorCalificar.getCalis()

        templateVars = {"calificaciones" : resultados}

        template = template_env.get_template('templates/calificaciones.html')
        #Cargamos la plantilla y le pasamos los datos cargardos
        self.response.out.write(template.render(templateVars))


class WebUsuario(webapp2.RequestHandler):
    
    '''
    def get(self):
        template=template_env.get_template('templates/registroUsuario.html')
        self.response.out.write(template.render())
    '''
    
    def get(self):
        template=template_env.get_template('templates/registroUsuario.html')
        self.response.out.write(template.render())
    '''
    def post(self):


        nombreUsuario = validaTexto(self.request.get('nombre'))
        dniUsuario = validaTexto(self.request.get('dni'))

        if not(nombreUsuario and dniUsuario):
            template=template_env.get_template('templates/registroUsuario.html')
            self.response.out.write(template.render())
        else:
            #Grabamos los datos en la base de datos.
            user.nuevoUsuario(self.request.get('nombre'))#, self.request.get('dni'))

            #Enviamos mensaje de aceptacion.
            self.response.out.write('<html><body>You wrote:<pre>')
            self.response.out.write(self.request.get('nombre'))
            self.response.out.write('</pre></body></html>')
    '''
    def post(self):
        nombreUsuario=validaTexto(self.request.get('nombre'))

        if not nombreUsuario:
            self.get(self)
        else:
            GestorUsuario.nuevoUsuario(self.request.get('nombre'))

            self.response.out.write('<html><body>You wrote:<pre>')
            self.response.out.write(self.request.get('nombre'))
            self.response.out.write('</pre></body></html>')

class WebEmpresa(webapp2.RequestHandler):

    '''
    def get(self):
        template=template_env.get_template('templates/registroEmpresa.html')
        self.response.out.write(template.render())
    '''

    def get(self):
        template=template_env.get_template('templates/registroEmpresa.html')
        self.response.out.write(template.render())

    def post(self):

        nombreEmpresa = validaTexto(self.request.get('nombre'))
        idEmpresa = validaTexto(self.request.get('id'))

        if not(nombreEmpresa and idEmpresa):
            template=template_env.get_template('templates/registroEmpresa.html')
            self.response.out.write(template.render())
        else:
            #Grabamos los datos en la base de datos.
            GestorEmpresa.nuevaEmpresa(int(self.request.get('id')),self.request.get('nombre'))#, self.request.get('dni'))

            #Enviamos mensaje de aceptacion.
            self.response.out.write('<html><body>You wrote:<pre>')
            self.response.out.write(self.request.get('nombre'))
            self.response.out.write('</pre></body></html>')

class WebCalificar(webapp2.RequestHandler):


    def get(self):
        template=template_env.get_template('templates/registroCalificar.html')
        self.response.out.write(template.render())

    def post(self):

        nombreUsuario = validaTexto(self.request.get('nombre'))
        idEmpresa = validaTexto(self.request.get('id'))
        nota = validaTexto(self.request.get('nota'))

        if not(nombreUsuario and idEmpresa and nota):
            template=template_env.get_template('templates/registroCalificar.html')
            self.response.out.write(template.render())
        else:
            #Grabamos los datos en la base de datos.
            GestorCalificar.nuevaCali(self.request.get('nombre'),int(self.request.get('id')),self.request.get('nota'))#, self.request.get('dni'))

            #Enviamos mensaje de aceptacion.
            self.response.out.write('<html><body>You wrote:<pre>')
            self.response.out.write(self.request.get('nombre'))
            self.response.out.write(self.request.get('id'))
            self.response.out.write(self.request.get('nota'))
            self.response.out.write('</pre></body></html>')

class WebBorrarCali(webapp2.RequestHandler):
    def get(self):
        template=template_env.get_template('templates/borrarCalificacion.html')
        self.response.out.write(template.render())

    def post(self):

        nombreUsuario=validaTexto(self.request.get('nombre'))
        idEmpresa=validaTexto(self.request.get('id'))

        if not(nombreUsuario and idEmpresa):
            template=template_env.get_template('templates/borrarCalificacion.html')
            self.response.out.write(template.render())
        else:
            GestorCalificar.borrarCali(self.request.get('nombre'),int(self.request.get('id')))

            self.response.out.write('<html><body>Calificacion anulada</body></html>')
'''
ge=GestorEmpresa()
gc=GestorCalificar()

ge.nuevaEmpresa(80,"Cali")
gc.nuevaCali("Pepe",80,8)
gc.borrarCali("Pepe",80)
'''


class MainPage(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/base.html')
        '''
        user = self.session.get('user')
        template_values = {
            'user': user
            }
        '''
        self.response.out.write(template.render())


app = webapp2.WSGIApplication([('/', MainPage),
                                      ('/registroUsuario', WebUsuario),
                                      ('/registroEmpresa', WebEmpresa),
                                      ('/registroCalificar', WebCalificar),
                                      ('/empresas', Empresa),
                                      ('/usuarios', Usuario),
                                      ('/calificaciones', Calificar),
                                      ('/borrarCalificacion', WebBorrarCali)],debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')

if __name__ == '__main__':
    main()