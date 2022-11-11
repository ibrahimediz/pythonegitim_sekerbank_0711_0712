#LİST VERİ TİPİ
#1.tanımlama
liste= [1,2,3,1.3,1.5,1.6+4j,"Ankara",[1,2,3]]
#       0 1 2 3    4   5       6         7
#       -8-7-6-5  -4  -3       -2        -1
print(liste[0],liste[-1])

liste = [[1,2,3,4],[5,6,7,8]]
print(liste[0][1]) #2
liste=["Ali","Veli",1,2,3,4]
print(liste[0].upper())# listenin 0. elemanı str olduğu için elemana eriştikten hemen sonra str fonksiyonu kullanabildik

#ekleme, silme, güncelleme
#ekleme : insert, append,extend
liste = [1,2,3,4]
liste.insert(0, 100)# [100,0,1,2,3,4]
print(liste)
liste = [1,2,3,4]
liste.append(100)  #[0,1,2,3,4,100]
print(liste)
liste = [1,2,3,4]
liste.extend([5,6,7,8])  #[0,1,2,3,4,5,6,7,8]
print(liste)
liste = [1,2,3,4]
liste2= [5,6,7,8]
print(liste+liste2)

#Silme:pop,remove,del
liste=[1,2,3,4]
liste.pop(2) #2. indisteki 3 elemanını siler
print(liste)
liste=[1,2,3,4]
liste.pop() # son elemanı siler
print(liste)
del liste[0]#1.elemanı siler
del liste[3:6]#4. , 5., 6. elemanları siler

#Yardımcı Fonksiyonlar
liste= [1,2,3]
liste2 = liste.copy()
liste=["Ali","Veli","Ayşe"]
liste.index("Veli") # 1 döndürür 1. index
liste = [1,2,3,4,5]
liste.clear() #listenin elemanlarını döndürür
liste=[11,57,42,69,23,2,11]
liste.sort() #sıralar küçükten büyüğe
liste=[11,57,42,69,23,2,11]
liste.sort(reverse=True) #sıralar büyükten küçüğe
liste.reverse()#listeyi tersten yazar
liste.count(1) #listede kaç tane 1 değeri olduğunu döndürür









