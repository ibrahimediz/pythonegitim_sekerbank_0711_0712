i=0
toplam=0
for i in range(201):
    if i%2 ==0:
        toplam = toplam + i
print(toplam)
print(sum(range(0,201,2)))

var1=input("Metni giriniz ")
sesliHarfler = "aeıioöuüAEIİOÖUÜ"
sayi = 0
for item in var1:
    if item in sesliHarfler:
        sayi += 1
print(sayi)



