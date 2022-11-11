liste = [1,2,3,4]
liste.insert(5,100)
liste2 = [100] + liste  
print(liste)
print(liste2)

#SİLME
#pop
liste=[1,2,3,4]
print(liste.pop(2))
print(liste)
#remove
liste=[1,2,3,2,3,2,1]
print(liste.remove(3))
print(liste)
#del
liste=[1,2,3,4,5,6,7,8,9,10]
del liste[0]
print(liste)
del liste[3:6]
liste=[1,2,3,4,5,6,7,8,9,10]
del liste 
print(liste)
#Mutable ve Immutable

