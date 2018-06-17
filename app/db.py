import psycopg2


conn = psycopg2.connect(dbname="debateit", host="localhost", port=5432, user="pguser", password="pguser")
