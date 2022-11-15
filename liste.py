liste = ["Abdullah","Anıl","Burak","Cem","Cihan","Emre","Dilay",
"Eyuphan","Furkan","İsmail","Nafiz","Özge","Pelin","Sevda","Fırat","Ediz","Serap"]
import os
dosyaismi = "02_01_Karar_yapilari.py"
for item in liste:
    if not os.path.exists(os.path.join("Egzersizler",item)):
        os.mkdir(os.path.join("Egzersizler",item))
    open(os.path.join("Egzersizler",item,dosyaismi),"a+")


