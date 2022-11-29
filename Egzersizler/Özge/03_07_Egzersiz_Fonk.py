tc = "10000000146" ##input("TCKN giriniz: ")
tek = sum(int(i) for i in tc[0:9:2])
cift = sum(int(i) for i in tc[1:8:2])
toplam = sum(int(i) for i in tc[0:10])
print(tek)
print(cift)
print(toplam)

if tc.isdigit():
    if len(tc) == 11:
        if tc[0] != 0:
            tek = sum(int(i) for i in tc[0:9:2])
            cift = sum(int(i) for i in tc[1:8:2])
            toplam = sum(int(i) for i in tc[0:10])
            if (tek*7-cift) % 10 == tc[9] and toplam % 10 == tc[10]:
                print("TCKN doğru")
            else:
                print("TCKN yanlış")
        else:
            print("İlk hane 0 olamaz")
    else:
        print("TCKN 11 haneli olmalı")
else:
    print("TCKN rakamsal değer olmalı")

