import mysql.connector
from scrapyspider import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

cnx = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOSTS, database=MYSQL_DB)
cur = cnx.cursor(buffered=True)

class Sql:

    @classmethod
    def insert_book_info(cls, name, chapter, author, recommend, length, time, status):
        sql = 'INSERT INTO books (`name`, `chapter`, `author`, `recommend`,`length`, `time`, `status`)' \
              ' VALUES (%(name)s, %(chapter)s, %(author)s, %(recommend)s, %(length)s, %(time)s, %(status)s)'
        value = {
            'name': name,
            'chapter': chapter,
            'author': author,
            'recommend': recommend,
            'length': length,
            'time': time,
            'status': status
        }
        cur.execute(sql, value)
        cnx.commit()

