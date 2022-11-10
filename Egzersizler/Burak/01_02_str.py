var1 = "Şekerbank"
#       012345678
print(var1[:3])
print(var1[4])
print(var1[::-1])


var1 = "Ankara"
print(var1,type(var1))
var1.index("a")
var1.rindex("a")
var1.find("z")


var1="Teşekkürler Süperman"
print(var1.replace("e", "ı"))


var1="Teşekkürler Süpermen"
print(var1[::-1].replace("e","ı",2)[::-1])

var1 = "Teşekkürler Süpermen"
print(var1[::-1].replace("e","ı",2)[::-1])