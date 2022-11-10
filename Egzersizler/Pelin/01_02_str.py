ad=input("isminizi 5 karakterden uzun olacak şekilde giriniz:")
print(ad,type(ad))
print(ad[0:3])
print(ad[4])
print(ad[::-1])

#str veri tipi
#1.tanımlama
var1='Ankara'
print(var1,type(var1))
var1="Ankara'da"
print(var1,type(var1))
var1="""Neler "yapıyorsun" Ankara'da"""
print(var1,type(var1))
var1='Ankara\'da'
print(var1,type(var1))
var1='Ankara\nİstanbul'#\n alt satıra geçer
print(var1,type(var1))
var1='Ankara\bİstanbul'#\b kendisinden önce gelen 1 karakteri siler
print(var1,type(var1))
var1='Ankara\tİstanbul'#\t  kendisinden sonra boşluk yerleştirir.
print(var1,type(var1))

#\ özel bir anlam ifade ediyorsa \\ olarak kullanılır.
var1='C:\\talat\\nalan\\buket.html'
print(var1)
var1=r'C:\talat\nalan\buket.html' #raw string
print(var1)

#2.erişim
var1 = "Şekerbank"
#       01235678
print((var1[0],var1[8]))
var1 = "Şekerbank"
#    -9-8-7-6-5-4-3-2-1
print(var1[0],var1[-9]) #aynı sonucu verir Ş

### Slicing-Bölümleme
var1 = "Şekerbank"
print(var1[0:5]) #5 gelmez Şeker
print(var1[5:9]) #bank
print(var1[5:]) #bank
print(var1[:5])#Şeker
print(var1[0:-4],var1[:-4]) #Şeker Şeker
print(var1[::3]) #şea
print(var1[::-1])#tersinden yazdırır. knabrekeŞ

#YARDIMCI FONKSİYONLAR
var1="Ankara"
var1.index("a") # en düşük index numarasını verir
var1.rindex("a") # sondan başlayarak gelen ilk index
var1.find("a") #olmayan bir değer olunca -1 döner, index hata verir
var1.rfind("a")
var1.replace("a", "e") # anlık değiştirir, sürekli değişmesine sebp olmaz
var1=var1.replace("a", "e") # sürekli değişime sebep
var1.replace("a", "e",2).replace("k", "t")

var1 = "Teşekkürler Süperman" #Teşekkürler Süpırmın
print(var1[::-1].replace("e", "ı",2)[::-1])

# Split ve Strip
var1= "12000 3 4 30000 1"
var1.split() # -> liste veri tipinde () içine verilen şeyi ayraç kullanır bişey vermezsen boşluk kullanır
var1.split("",maxsplit=2)
var1 = "        Şekerbank        "
var1.strip() # Trim boşlukları
var1 = "..........Şekerbank......."
var1.strip(".") # Trim noktaları
var1 = "....a.....Şekerbank..._2.."
var1.strip(".a_2") # Trim içerdeki karakterleri baştan ve sondan başlayarak temizler
var1.rstrip()#right
var1.lstrip()#left
#JOIN
liste = ["Ali","Veli","Ankara","a.@gmail","123456"]
print(",".join((liste))) # , ve liste içindekileri joinliyor

#FORMAT FONKSİYONU

var1 ="""
Sayın {} {},
Doğum gününüz kutlu olsun
"""
isim = "Ali"
soyisim = "Veli"
print(var1.format(isim,soyisim)) #değer vermeyince sırasıyla yerleştiri

var1 ="""
Sayın {1} {0},
Doğum gününüz kutlu olsun
"""
isim = "Ali"
soyisim = "Veli"
print(var1.format(isim,soyisim)) #değer vermeyince sırasıyla yerleştiri
















