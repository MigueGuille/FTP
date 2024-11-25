from pyftpdlib.authorizers import DummyAuthorizer
import psycopg2
from db.dbConnect import get_db_connection

class DatabaseAuthorizer(DummyAuthorizer):
    def validate_authentication(self, username, password, handler):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT password FROM users WHERE username = %s", (username,))
        result = cur.fetchone()
        cur.close()
        conn.close()
        if result is None:
            return False
        if result[0] == password:
            # Añadir el usuario al authorizer si la autenticación es exitosa
            if not self.has_user(username):
                self.add_user(username, password, homedir='files', perm='elradfmw')
            return True
        return False