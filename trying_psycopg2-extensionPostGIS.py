import psycopg2

connection = psycopg2.connect(
    dbname='chapter12',
    host="localhost",
    user='postgres',
    password='adminpass',
    port="5432")
cursor = connection.cursor()
cursor.execute('CREATE EXTENSION postgis')
connection.close()
