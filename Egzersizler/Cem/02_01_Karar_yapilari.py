
while True:
    try:
        #yas = int(input("Plese enter a age: "))
        yas = 20
        print("veri tipi basarili",yas)
        if int(yas)>= 18 and int(yas)<=30:
            print("z kusağısınız yasınız: ",yas)
        elif int(yas)>30:
            print("30'dan büyük")
        else:
            print("18'den büyük")
        break
    except ValueError:
        print("Please enter a valid integer")
        

#İki Açısı Girilen Bir Üçgenin türünü ekrana yazdıran Python programını yazınız
#1. Eşkenar Üçgen
#2. Dik Üçgen
#3. İkizkenar Üçgen
#4. Çeşitkenar Üçgen
#<br>02_01_Karar_yapilari.py` dosyasına yaptığımız çalışmaları kaydedebiliriz

aci_bir = 50
aci_iki = 60
aci_toplam = 180
aci_uc = aci_toplam - aci_bir - aci_iki

if aci_bir == aci_iki and aci_bir == aci_uc:
    print("eşitkenar üçgen")
elif aci_bir == aci_iki:
    print("ikizkenar üçgen")
elif aci_bir != aci_iki != aci_uc:
    print("çeşitkenar üçgen")
elif aci_bir == "90" or aci_iki == "90" or aci_uc == "90":
    print("dik_acidir")
print(aci_bir,aci_iki,aci_uc)