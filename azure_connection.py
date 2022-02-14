import pyodbc
import getpass

server = 'comp4522group6.database.windows.net'
database = '4522_Covid'
username = 'dbadmin'
password = getpass.getpass()
driver = '{ODBC Driver 17 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT TOP 50 * FROM [dbo].[lga-coverage-AHS]")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()