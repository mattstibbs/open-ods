import psycopg2, psycopg2.pool, psycopg2.extras
from urllib.parse import urlparse as urlparse
import logging
import openods.config as config

log = logging.getLogger('__name__')
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
log.addHandler(ch)

print(config.DATABASE_URL)
url = urlparse(config.DATABASE_URL)


def get_connection():
    try:
        conn = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )
        log.info("Connected to database")

    except psycopg2.Error as e:
        log.warning("I am unable to connect to the database")

    return conn