liste = [4]
def asalBul(sayilar):
    sonuc = []
    for item in sayilar:
        for i in range(2,item): # 2,3,4,5,6,7,8,9,10
            if item % i == 0: # => item = 11 =>  i ise değişiyor yukarıdaki sayılar
                break
        else:
            sonuc.append(item)
    return sonuc
print(asalBul(liste))