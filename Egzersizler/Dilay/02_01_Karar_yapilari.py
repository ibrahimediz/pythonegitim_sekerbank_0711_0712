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