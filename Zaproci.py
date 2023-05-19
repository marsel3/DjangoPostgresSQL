
import psycopg2
from psycopg2 import Error


class DataBase:
    def __init__(self):
        self.connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="1234",
                                  host="127.0.0.1",
                                  port="5433",
                                  database="sport")
        self.cursor = self.connection.cursor()


    def team_games(self):
        with self.connection:
            self.cursor.execute('''SELECT * FROM "CreateDatabase_vidsporta" WHERE "vidsporta_type"=TRUE''')
            return [i[0] for i in self.cursor.fetchall()]


    def solo_games(self):
        with self.connection:
            self.cursor.execute('''SELECT * FROM "CreateDatabase_vidsporta" WHERE "vidsporta_type"=FALSE''')
            return [i[0] for i in self.cursor.fetchall()]


    def treners(self):
        with self.connection:
            self.cursor.execute('''SELECT * FROM "CreateDatabase_trener"''')
            return self.cursor.fetchall()


db = DataBase()

print('TEAM:   ', db.team_games())
print('SOLO:   ', db.solo_games())
print('TRENER: ', db.treners())


treners = {
}





