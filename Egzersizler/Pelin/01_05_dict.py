#dict veri tipi : dictionary
sozluk = {}
sozluk = {"1":"Bir"}
#         key value
#           item
#Erişim ve get fonksiyonu
sozluk = {"1":"Bir","2":"İki"}
print(sozluk["1"])#key değeri üzerinden value döndürür
sozluk = {"1":"Bir","2":"İki","1":"One"}
print(sozluk["1"])#key değeri üzerinden value döndürür. en son ekleneni döndürür
sozluk = {"1":"Bir","2":"İki"}
#print(sozluk.get["1"])#Bir
sozluk = {"1":"Bir","2":"İki"}
#print(sozluk["3"])#none
sozluk = {"1":"Bir","2":"İki"}
print(sozluk.setdefault("3","three"))# sözlükte 3 yoksa ekler ve three valuesuyla ekler
#UPDATE
a = {"1":"Bir","2":"İki","3":"Üç","5":"Beş"}
b={"1":"Bir","2":"İki","3":"Three","4":"Four"}
a.update(b) # olanı yazarım, farklı varsa güncellerim, yeniyi eklerim
print(a)
#popitem
b={"1":"Bir","2":"İki","3":"Three","4":"Four"}
b.popitem()# en son eklenen elemanı çıkartır
#pop
b={"1":"Bir","2":"İki","3":"Three","4":"Four"}
print(b.pop("2"))#verilen anahtarı değeri ile birlikte siler
#fromkeys




