yas = input("Yaşınızı Giriniz:")
if yas:
    if yas.isdigit():
        yas=int(yas)
    if yas >= 18 and yas >= 30:
     print (f"Z kuşağı")
    else:
         print (f"Z kuşağı değil")
else :
     print ("Numerik değer girin")
else:
     print ("Değer giriniz")


yas = input("yaş giriniz:")
if yas:
    if yas.isdigit():
        yas=int(yas)
        if yas>18 and yas<30: # 18 < yas < 30
            print(f"yaşınız: {yas }  ve Z kuşağısınız")
        else:
             print(f"yaşınız: {yas }  ve Z kuşağı değilsiniz")
    else:
        print("numerik değer girmediniz")        
else:
    print("değer girmediniz")