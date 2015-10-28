
from gestorhtml import *





def main():
    from paste import httpserver
    app = Server()
    httpserver.serve(app, host='127.0.0.1', port='8080')

if __name__ == '__main__':
    main()