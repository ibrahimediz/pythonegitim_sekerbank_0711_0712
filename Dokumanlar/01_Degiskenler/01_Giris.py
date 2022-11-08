var1 = 2
#degisken = değer
# değişkenleri tanımlarken atama operatörü kullanılır. '=' assignment operator
var1 = var2 = 2


# --------------------------------------------------------
"""
Etkinlik 01:
kullanıcıdan yaş bilgisini alıp ekrana yazdıran python kodunu yazınız.
deg1 adında bir değişken tanımlayıp bu değişkeni ekrana yazdıran python kodunu ekrana yazınız.
kodları 01_01_Giris.py dosyasına yazabiliriz.
"""
# yas = input("Yaşınızı Giriniz:")
# print("Yaşı:",yas)
# deg1 = 99
# print("deg1 içerisindeki değer:",deg1)
# --------------------------------------------------------
var1 = var2 = 2
var1,var2 = 2,3
print(var1,var2) # => 2 3
# a = b = 1
# print(a,b) # 1 1
# a,b = b,a+b
# print(a,b) # 1 2
# a,b = b,a+b
# print(a,b) # 2 3
# a,b = b,a+b
# print(a,b) # 3 5
# a,b = b,a+b
# print(a,b) # 5 8
""" 
Değişken tanımalama kuralları
1. Değişken ismi sayı ile başlayamaz
2. Değişken isminde `_` dışında herhangi bir noktalama işareti ve boşluk kullanılmaz
3. rezerver kelimelerin değişken ismi olarak kullanılması önerilmez
```
import keywords
print(keywords.kwlist)
```
"""

import keyword
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 
'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 
'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']