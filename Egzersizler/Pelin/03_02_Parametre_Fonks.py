#fonksiyonlarda parametreler
#isimli parametre tanım
def fonk():
    print("Merhaba")
fonk()
def fonk(isim):
    print("Merhaba",isim)
fonk("Ankara")
#varsayılan parametre tanımı
def topla(a,b):
    print(a+b)
topla(2,3)
def topla(a,b,c=0):
    print(f"{a}+{b}+{c} = {a+b+c}")
topla(2,3)#c 0 olarak dikkate alınır varsayılan değeri 0
topla(2,3,5)

def fonk(a,b,/,c,d,*,e,f):
    print(a,b,c,d,e)
fonk(1,2,3,4,e=5,f=6)

kenar1=input("kenar uzunluğu giriniz:")
kenar1 = int(kenar1) if kenar1 and kenar1.isdigit() else -1
kenar2=input("kenar uzunluğu giriniz:")
kenar2 = int(kenar2) if kenar2 and kenar2.isdigit() else -1
def alan_kare(a):
    print("karenin alanı:", a*a)
def cevre_kare(a,b):
    print("Çevre:", 4*a)
def alan_dikdortgen(a,b):
    print("dikdörtgenin alanı:", a*b)
if kenar1==kenar2:
    alan_kare(kenar1)
    cevre_kare(kenar1)
else:
    alan_dikdortgen(kenar1, kenar2)
    #cevre(kenar1, kenar2)

    ##*args - tupple
    ##kwarggs - dictionary
    def fonk(**kwargs):
        for key,value in kwargs.items():
            if key == "selam":
                print("selam",value)
            if key == "naber":
                print("naber",value)
     
    



