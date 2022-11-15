#Libraries
import pyodbc
import pandas as pd

class Database():

    def __init__(self):
        from  ..keyvault.secrets import KeyVault

        self.server = KeyVault().getSecret('SqlServer')
        self.database = KeyVault().getSecret('Sqldb')
        self.username = KeyVault().getSecret('Sqladmin')
        self.password = KeyVault().getSecret('SqlPwd')

        self.connection_string = (
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server
            +';DATABASE='+self.database
            +';UID='+self.username
            +';PWD='+ self.password)


    def ExecuteQuery(self, Query):
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute(Query)
            cursor.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def truncate_table(self, table):
        '''
        Truncat a table in Sql server
        param:
            table: string --> name of table
        '''

        query = f'''
                truncate table [{table}]
        '''
        try:
            conn = pyodbc.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute(query)
            cursor.commit()
        except Exception as e:
                    print(e)

    def InsertCSVData(self,csvfile, table):
        '''
        load csv into a table
        param:
            csvfile: string
            table: string
        '''
        df = pd.read_csv(csvfile)
        tablename = table
        columns = list(df.keys()[1:])
        payload = ''
        for index, row in df.iterrows():
            record = '('
            for i,column in enumerate(columns):
                record += "'"+str(row[column]).replace("'"," ")+"'" + ','
            record = record[:-1]
            payload += record+'),'+'\n'

            if index % 1000 == 0:
                query = f'''
                INSERT INTO [{tablename}]
                VALUES
                {payload[:-2]}
                '''
                try:
                    conn = pyodbc.connect(self.connection_string)
                    cursor = conn.cursor()
                    cursor.execute(query)
                    cursor.commit()
                except Exception as e:
                    print(e)

                payload = ''

        if len(payload) > 0:
                query = f'''
                INSERT INTO [{tablename}]
                VALUES
                {payload[:-2]}
                '''
                try:
                    conn = pyodbc.connect(self.connection_string)
                    cursor = conn.cursor()
                    cursor.execute(query)
                    cursor.commit()
                except Exception as e:
                    print(e)


    def InsertJsonData(self,jsonfile, table):
        '''
        load jsonfile into a table
        param:
            csvfile: string
            table : string
        '''
        df = pd.read_json(jsonfile)
        tablename = table
        columns = list(df.keys())
        payload = ''
        for index, row in df.iterrows():
            record = '('
            for i,column in enumerate(columns):
                record += "'"+str(row[column]).replace("'"," ")+"'" + ','
            record = record[:-1]
            payload += record+'),'+'\n'

            if index % 1000 == 0:
                query = f'''
                INSERT INTO [{tablename}]
                VALUES
                {payload[:-2]}
                '''
                try:
                    conn = pyodbc.connect(self.connection_string)
                    cursor = conn.cursor()
                    cursor.execute(query)
                    cursor.commit()
                except Exception as e:
                    print(e)

                payload = ''

        if len(payload) > 0:
                query = f'''
                INSERT INTO [{tablename}]
                VALUES
                {payload[:-2]}
                '''
                try:
                    conn = pyodbc.connect(self.connection_string)
                    cursor = conn.cursor()
                    cursor.execute(query)
                    cursor.commit()
                except Exception as e:
                    print(e)

    def InsertDf(self,df, table):
        '''
        Insert Data Frame into Sql table
        param:
            df: string --> name of dataframe
            table: string --> name of table in SQL
        '''
        tablename = table
        columns = list(df.keys())
        payload = ''
        for index, row in df.iterrows():
            record = '('
            for i,column in enumerate(columns):
                record += "'"+str(row[column]).replace("'"," ")+"'" + ','
            record = record[:-1]
            payload += record+'),'+'\n'

            if index % 1000 == 0:
                query = f'''
                INSERT INTO [{tablename}]
                VALUES
                {payload[:-2]}
                '''
                try:
                    conn = pyodbc.connect(self.connection_string)
                    cursor = conn.cursor()
                    cursor.execute(query)
                    cursor.commit()
                except Exception as e:
                    print(e)

                payload = ''

        if len(payload) > 0:
                query = f'''
                INSERT INTO [{tablename}]
                VALUES
                {payload[:-2]}
                '''
                try:
                    conn = pyodbc.connect(self.connection_string)
                    cursor = conn.cursor()
                    cursor.execute(query)
                    cursor.commit()
                except Exception as e:
                    print(e)