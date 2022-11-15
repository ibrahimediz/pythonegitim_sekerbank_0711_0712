liste = ["Abdullah","Anıl","Burak","Cem","Cihan","Emre","Dilay",
"Eyuphan","Furkan","İsmail","Nafiz","Özge","Pelin","Sevda","Fırat","Ediz","Serap"]
import os
dosyaismi = "01_06_set_and_others.py"
for item in liste:
    if not os.path.exists(os.path.join("Egzersizler",item)):
        os.mkdir(os.path.join("Egzersizler",item))
    open(os.path.join("Egzersizler",item,dosyaismi),"a+")


