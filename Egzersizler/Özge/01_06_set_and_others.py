kume = set()
print(type(kume))

liste1 = [1,2,3,4,5]
liste2 = 4,5,6,7,8
kume1 = set(liste1)
kume2 = set(liste2)
print(kume1)
print(kume2)

print(kume1.isdisjoint(kume2))  ## ayrık
print(kume1.issubset(kume2))  ## alt küme
print(kume1.issuperset(kume2))  ## kapsam

print(kume1.difference(kume2))  ## {1, 2, 3}
print(kume2.difference(kume1))  ## {8, 6, 7}

print(kume1.symmetric_difference(kume2))  ## {1, 2, 3, 6, 7, 8}

print(kume1.intersection(kume2))  ## {4,5}

print(kume1.union(kume2))  ## {1, 2, 3, 4, 5, 6, 7, 8}

kume1.difference_update(kume2)
print(kume1)  ## {1, 2, 3}

var1 = 9.2
var1.as_integer_ratio()
