import os,psycopg2


class connection_db:
    def __init__(self):
        self.connect_db = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host = os.getenv("POSTGRES_HOST")
        )
    
    def __enter__(self) :
        return self.connect_db

    def __exit__(self,*args):
        self.connect_db.close()
