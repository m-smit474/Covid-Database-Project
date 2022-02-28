import pyodbc
import getpass
import pandas as pd

server = 'comp4522group6.database.windows.net'
database = '4522_Covid'
username = 'dbadmin'
password = getpass.getpass()
driver = '{ODBC Driver 17 for SQL Server}'

dir = "C:/Users/smith/OneDrive/Documents/Comp 4522/Data/"
vaccine_df = pd.read_csv(dir + "lga-coverage.csv")
cases_timeseries_df = pd.read_csv(dir + "COVID-19 Cases.csv")

print(vaccine_df.head())
print(cases_timeseries_df.head())


#Clean data
trimmed_vaccine_df = vaccine_df[["Local Code","Age Group","1 dose","2 doses","3 doses"]].copy()
cases_timeseries_df.drop(columns=["Admin2","FIPS","Combined_Key","Table_Names","Prep_Flow_Runtime"], inplace=True)

print(trimmed_vaccine_df.head())
print(cases_timeseries_df.head())

with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT TOP 50 * FROM [dbo].[lga-coverage-AHS]")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()