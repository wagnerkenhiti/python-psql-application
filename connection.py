import os,psycopg2


class connection_db:
    def __init__(self):
        self.connect_db = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="mysecretpassword",
            host = "localhost"
        )
    
    def __enter__(self) :
        return self.connect_db

    def __exit__(self,*args):
        self.connect_db.close()