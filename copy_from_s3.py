import pymonetdb
from smart_open import open
import time

connection = pymonetdb.connect(username="monetdb", password="monetdb",
                               hostname="localhost", database="s3temp")

connection.set_autocommit(False)
cursor = connection.cursor()
step = 0

start_time = time.time()

for line in open('s3://my-monetdb-temp-csv-s3bucket/example2.csv'):
    step += 1
    cursor.execute("INSERT INTO gama VALUES(%(line)s)", parameters={'line': line})
    if step >= 10000:
        connection.commit()
        step = 0


connection.commit()
