def fonk(isim,soyisim):
    print("Merhabalar",isim,soyisim)
fonk(soyisim="Ankara",isim="Çankaya")

def topla(a,b):
    print(a+b)
topla(2,3)

def topla(a,b,c=0):
    print(f"{a}+{b}+{c}={a+b+c}")
topla(2,3)
topla(2,3,5)