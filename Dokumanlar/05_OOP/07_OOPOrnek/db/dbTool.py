import sqlite3 as sql

class DBTool:
    def __init__(self,dbAddress="empty.db"):
        self.dbAddress = dbAddress
        self.db = sql.connect(self.dbAddress)
        self.cur = self.db.cursor()
    
    def select(self,query):
        results =  self.cur.execute(query)
        return results.fetchall()

    def __del__(self):
        self.db.close()
print(__name__,"DB Tool dosyasının ismini öğreniyorum")