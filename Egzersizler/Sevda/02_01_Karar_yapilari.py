i=2
if i%2==0:
    print(i)

    yas= input("yasiniz:")
    if yas:
        if yas.isdigit():
            yas=int(yas)
            if yas<30 and yas>18:
                print("Z kuşağındasınız :)")
            else: 
                print("Z kusagi degilsiniz ")
        else:
            print("Numerik deger girilmeli.")
    else:    
        print("Değer girmediniz")

aciListesi=list(map(int,input("acilari giriniz").split(",")))
if aciListesi[0]+aciListesi[1]+aciListesi[2]==180:
  if aciListesi[0]==aciListesi[1]==aciListesi[2]:
    print("Eşkenar Üçgen")
  elif aciListesi[0]==aciListesi[1] or aciListesi[0]==aciListesi[2] or aciListesi[1]==aciListesi[2]:
    if aciListesi[0]==90 or aciListesi[1]==90 or aciListesi[2]==90:
      print("ikizkenar Dik Üçgen")
    else :
      print("ikizkenar Üçgen")
  else:
    print("Çeşitkenar Üçgen")
else: print("Açılar hatalı")


