#fonksiyonlardan değerleri dışarı aktarma
#return, yield, fonksiyonun type değeri

def fonk(a,b):
    return a+b
print(fonk(2,3))
sonuc= fonk(2,3)
print(sonuc)

#fonksiyonların tipi nasıl değişir
def fonk(a,b):
    return a+b
print(type(fonk))
print(type(fonk(2,3)))
print(type(fonk("2","3")))
print(type(fonk({2},{3})))