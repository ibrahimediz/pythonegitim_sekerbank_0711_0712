var222 = "Şekerbank"
#       012345678
#ilk üç harf
var_ilk_uc = "Şekerbank"
print("var ilk üc harf : " ,var_ilk_uc[:3])

#beşinci
var_besinci = "Şekerbank"
print("var besinci : ", var_besinci[4])

# tersinden yazdır,
var_tersten = "Şekerbank"
print("tersten yazımı : ",var_tersten[::-1]) # tersinden yazdır

## YARDIMCI FONK

var1= "Ankara"
var1.index("a")

var1= "Teşekkürler Süpermen"
var_replace = var1.replace("e", "ı").replace("ü", "1")
print (var_replace)

var_spr= "Teşekkürler Süpermen" #Teşekkürler Supırmın
var_replace = var1.replace("e", "ı").replace("ü", "1")
print (var_replace)

print(var_spr[::-1].replace("e","ı",2)[::-1])
print(var_spr[::-1].replace("e","ı",1)[::-1])

var1_spl="11531,4,213,4"
print(var1_spl.split(","))
print((type(var1_spl.split(","))))
var1_spl_pr= var1_spl.split(",",maxsplit=2)

var_select = " 1_  s __  a1a  ss1s 1__ "

print(var_select)
print("strip",var_select.strip(' _1'))
print("rstrip",var_select.rstrip(' _1'))
print("lstrip",var_select.lstrip(' _1'))
