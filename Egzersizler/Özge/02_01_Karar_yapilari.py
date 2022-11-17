x = input("Üçgenin ilk açısını giriniz:")
y = input("Üçgenin ikinci açısını giriniz:")   
if(x and y) and (x.isdigit() and y.isdigit()):
    x,y = int(x),int(y)
    liste = [x,y,180-(x+y)]
    if x + y < 180:
        acilar = set(liste)
        if len(acilar) == 1:
            print("Eşkenar")
        elif len(acilar) == 2:
            print("İkizkenar")
        else:
            print("Çeşitkenar")
        if 90 in acilar:
            print("Dik")
    else: 
        print("Açı değer hatası")
else:
    print("Uygun değer girilmedi")