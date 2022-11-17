aci1=30
aci2=60
aci3=180-aci1+aci2
if aci1==aci2 and aci1==60:
   print("eşkenar üçgen")
elif aci1==aci2 and aci1!=60:
   print("ikizkenar üçgen")
elif aci1==90 or aci2==90









yas=input("yas bilgisini giriniz:")
if yas:
   if yas.isdigit():
      yas=int(yas)
      if yas>18 and yas<30:
         print("z kusagisiniz")
      else:
         print("farkli bir kusaksiniz")
   else:
       print("Numerik deger girmediniz!")
else:
    print("Deger girmediniz!")