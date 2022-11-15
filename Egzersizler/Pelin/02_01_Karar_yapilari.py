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

#elif
a=2
sonuc= "çift" if a%2==0 else "tek" # tek satırda if else
print(sonuc)
_not = input("notunuzu giriniz:")
_not = int(_not) if _not and _not.isdigit() else -1
if 85<= _not <=100:
    print("AA")
else:
    if 70<= _not <=84:
        print("BB")
    else:
        if 55<= _not <=69:
            print("CC")
        else:
            print("not giriniz")

if 85<= _not <=100:
    print("AA")
elif 70<= _not <=84:
        print("BB")
elif 55<= _not <=69:
        print("CC")
else:
     print("not giriniz")



