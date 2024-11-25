from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os
from ftp.authorizer import DatabaseAuthorizer

# Crear la carpeta 'files' si no existe
if not os.path.exists('files'):
    os.makedirs('files')

# Crear el autorizador
authorizer = DatabaseAuthorizer()

# Configurar el manejador
handler = FTPHandler
handler.authorizer = authorizer

if __name__ == "__main__":
    # Crear el servidor FTP
    server = FTPServer(("0.0.0.0", 2121), handler)

    # Iniciar el servidor
    server.serve_forever()