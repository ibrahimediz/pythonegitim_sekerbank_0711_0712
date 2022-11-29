import os # tüm kütüphaneyi alır
print(os.listdir(".")) # os. ile çağırdım
from os import listdir # sadece listdir alınır
print(listdir("."))


import random as rnd # as ile kısaltma yapılabilir
print(rnd.randint(1,49))
from random import randint as rint
print(rint(1,49))