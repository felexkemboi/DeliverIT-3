import psycopg2

DB_HOST = 'localhost'
DB_USERNAME = 'gitau'
DB_NAME = 'deliverit'
DB_PASS = '#darkmoon'
DB_PORT = 5432

url = "dbname = 'deliverit' host = localhost \
port = '5432' user = 'gitau' password = '#darkmoon'"
# Create database connection
con = psycopg2.connect(url)

# Creating the cursor
cur = con.cursor()

# Executing an SQL Query
# result = con.execute()
# Closes the databse connection
con.close()