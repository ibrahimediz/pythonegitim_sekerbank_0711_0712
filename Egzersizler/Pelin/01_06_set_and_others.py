#set veri tipi
kume={}
print(type(kume))
kume={1,2,3,4}
print(type(kume))
liste1=[1,2,3,4]
liste2=4,5,6,7,8
kume1=set(liste1)
kume2=set(liste2)
print(kume1)
print(kume2)
print(kume1.difference(kume2))
print(kume2.difference(kume1))
print(kume1.symmetric_difference(kume2))
print(kume1.intersection(kume2))
print(kume1.union(kume2))
#union hariç hepsinin update'i de vardır.
liste=[1,2,3,4,1,1,1,1,1,1,1,1,2,2,2,3,3,3,4,5,6,6,6,6,7,7,7,8,8,8]
print(set(liste))
liste1=[1,2,3,4]
liste2=4,5,6,7,8
kume1=set(liste1)
kume2=set(liste2)
print("update olmadan önce:",kume1)
print("kümelerin farkı:",kume1.difference(kume2))
kume1.difference_update(kume2)#burada farkı elde edip kümeyi güncelledik
print("kümelerin farkının güncellenmiş hali:",kume1)

#issubset,isdisjoint,issuperset
kume1={1,2,3}
kume2={1,2,3,4,5,6,7}
kume3={10,20,30}
print(kume1.isdisjoint(kume3))#ayrık
print(kume1.issubset(kume2))#altküme
print(kume2.issuperset(kume1))#kapsar

##the others
#int veri tipi
#float
#complex
var1=255
var1=4.5


