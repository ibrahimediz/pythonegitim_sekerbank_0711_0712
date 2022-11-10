isim1 = "talat"
soyisim1 = "nalan"
var1 = f"Sayın {isim1} {soyisim1},  Doğum Gününüz Kutlu Olsun"
print(var1)


var1 = """
Sayın {} {},
Doğum Gününüz Kutlu Olsun
"""
isim = "Ali"
soyisim = "Veli"
print(var1.format(isim,soyisim))
##        