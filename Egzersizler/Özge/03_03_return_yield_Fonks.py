def fonk(a,b):
    return a+b
print(fonk(2,3))

def fonk(a,b):
    return a,b,a+b
sonuc = fonk(2, 3)
print(f"{sonuc[0]}+{sonuc[1]}={sonuc[2]}")
