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








