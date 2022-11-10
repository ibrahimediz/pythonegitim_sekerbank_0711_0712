liste = [[1,2,3,4],[5,6,7,8]]
#           0.         1
#         

print(type(liste[0]))

liste = [1,2,3,4]
#        0 1 2 3
liste.insert(2,100)
print(liste)

liste.append(100)
print(liste)

liste.pop()
print("pop",liste)

liste.remove(1)
print("remove",liste)

liste.delete("2")
print(liste)
