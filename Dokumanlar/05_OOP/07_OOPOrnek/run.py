# "/workspace/pythonegitim_sekerbank_0711_0712/Dokumanlar/05_OOP/07_OOPOrnek/db/chinook.db"
# "Dokumanlar/05_OOP/07_OOPOrnek/db/dbTool.py"

# test = dbTool.DBTool("Dokumanlar/05_OOP/07_OOPOrnek/db/chinook.db") # => test için yazıldı
# print(test.select("SELECT customerid,FirstName,LastName,email FROM customers LIMIT 5"))
from db import dbTool
import csv
import json
import time
from datetime import datetime
import os
class DB2CSV:
    def __init__(self,filename="res.csv",dbAddress="empty.py"):
        self.filename = filename
        self.__timestamp = None
        self.dbObj = dbTool.DBTool(dbAddress)


    def getData(self,query):
        return self.dbObj.select(query)
        

    def writeData(self,param=0,limits=5):
        """
        a = 0
        w = 1
        r = 2
        x = 3
        """
        modeList = ["a+","w+","r+","x+"] 
        myFile = open(self.filename,modeList[param],encoding="UTF-8")
        kayitlar = self.getData(f"""
                                SELECT InvoiceId,
                                CustomerId,
                                InvoiceDate,
                                BillingCity,
                                Total
                                FROM invoices
                                LIMIT {limits}""")
        # for item in kayitlar: # 1st option
        #     print(*item,sep=";",file=open(self.filename,modeList[param],encoding="UTF-8"))
        for item in kayitlar: # [(1,ali,veli),(2,ayşe,veli)]
            veri = {"InvoiceId":item[0],
            "CustomerId":item[1],
            "InvoiceDate":item[2],
            "BillingCity":item[3],
            "Total":item[4]}
            print(*item,sep=";",file=open(self.filename+".csv",modeList[param],encoding="UTF-8"))
            print(json.dumps(veri, indent=4,),end=",\n",file=open(self.filename+".json",modeList[param],encoding="UTF-8"))



if __name__ == "__main__":
    zaman = datetime.now()
    yol = os.path.join(*map(str,[zaman.year,zaman.month,zaman.day,zaman.hour]))
    if not os.path.exists(yol):
        os.makedirs(os.path.join(*map(str,[zaman.year,zaman.month,zaman.day,zaman.hour])))

    tool1 = DB2CSV(f"{yol}/{time.time()}","Dokumanlar/05_OOP/07_OOPOrnek/db/chinook.db")
    tool1.writeData(0,100)
