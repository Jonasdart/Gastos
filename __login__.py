import MySQLdb as mdb

class login():
    def faz_login(self, cred):
        self.lista = cred
        try:
            self.conn = mdb.connect(self.lista[0], self.lista[1], self.lista[2], self.lista[3])
        except:
            raise
        else:
            return self.conn
