
def dikdortgen_alan(a,b):
    print("Dikdörtgenin alanı: ",a*b)
def dikdorgen_cevre(a,b):
    print("Dikdörtgenin çevresi: ",2*(a+b))
def kare_alan(a):
    print("Karenin alanı: ",a*a)
def kare_cevre(a):
    print("Karenin çevresi: ",4*a)

kenar1=int(input("Kenar uzunluğu giriniz:"))
kenar2=int(input("Kenar uzunluğu giriniz:"))
if kenar1==kenar2:
    kare_alan(kenar1)
    kare_cevre(kenar1)
else:
    dikdortgen_alan(kenar1, kenar2)
    dikdorgen_cevre(kenar1, kenar2)