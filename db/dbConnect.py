import psycopg2
from config import config

def get_db_connection():
    conn = psycopg2.connect(
        host=config.DB_HOST,
        database=config.DB_NAME,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        options="-c client_encoding=UTF8"
    )
    return conn