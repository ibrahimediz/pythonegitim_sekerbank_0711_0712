ad=input("isminizi 5 karakterden uzun olacak şekilde giriniz:")
print(ad[0,3])


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
print(var1[0,5]) #5 gelmez Şeker
print(var1[5,9]) #bank
print(var1[5:]) #bank
print(var1[:5])#Şeker
print(var1[0:-4],var1[:-4]) #Şeker Şeker
print(var1[::3]) #şea
print(var1[::-1])#tersinden yazdırır. knabrekeŞ









