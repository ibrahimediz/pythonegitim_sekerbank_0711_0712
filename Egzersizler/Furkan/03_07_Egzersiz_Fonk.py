giris= input("TC giriniz: ")
tc=[]
kontrol1 = []
kontrol2 =[]
tc = list(giris)
for i in range(0,9,2):
    kontrol1.append(tc[i])
for i in range(1,8,2):
    kontrol2.append(tc[i])

sonuc = (int(sum(kontrol1))*7 - int(kontrol2))


if giris.isdigit():
    if len(tc) == 11:
        if tc[0] != '0':
            if sonuc % 10 == tc[9]:
                print("Başarılı")
        else:
            print("0 olamaz")
    else:
        print("11 haneli olmalı")          
else:
    print("Sayı Giriniz")


