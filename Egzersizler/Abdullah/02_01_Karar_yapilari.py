yas = input("Yaşınızı Giriniz:")
if yas:
    if yas.isdigit():
       yas=int(yas)
       if yas >= 18 and yas >= 30:
           print (f"Yaş{yas } Z kuşağı")
       else:
         print (f"Yaş{yas } Z kuşağı değil")
    else :
         print ("Numerik değer girin")
else:
     print ("Değer giriniz")


