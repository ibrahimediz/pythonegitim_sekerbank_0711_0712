#operatörler
var1=2
#aritmetik o. + - / * // % **
var1=2
var2=3
print("+",var1+var2)
print("-",var1-var2)
print("*",var1*var2)
print("/",var1/var2)
print("//",var1//var2)
print("%",var1%var2)
print("**",var1**var2)

#unary : +=, -=
var1 = 5
var1= var1 + 7
var1+=7
print(var1)

#karşılaştırma <, > <=, >= !=
a=4
b=2
print("a<b", a<b) #false

#mantıkssal : and or not
a=True
b=False
print("a and b", a and b)

#üyelik o. in, not in
liste=[1,2,3,4,5]
print(1 in liste) # true
#kimlik : is, is not
var1 = 1.0
var2= 1
print(var1 is var2) # false çünkü id leri farklı
print(var1==var2)
print(id(var1))
print(id(var2))
#unpack : *
liste= [1,2,3,4,5]
print(*liste)
print(*liste,sep=";")
#bitwise : &,|,<<,>>,^,~
a=10        # => 1010
b=4         # => 0100
print(a&b)  # => 0000 :0
print(a|b)  # => 1110 :14
print(a^b)  # => 1110 :14
print(~a)  # => -0101
print(b<<2)  # => 
print(b>>2)  # => 


