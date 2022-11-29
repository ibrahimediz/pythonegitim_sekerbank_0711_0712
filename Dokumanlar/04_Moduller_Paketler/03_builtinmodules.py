# import os
# print(os.path.join("Egzersizler","Ediz","str.py"))
# import sys
# # print(*sys.path,sep="\n")
# sys.path.append("Dokumanlar/03_Fonksiyonlar")
# print(*sys.path,sep="\n")

# import time
# import multiprocessing
# def sleeping(s):
#     print(f"{s} sn uyuyor ")
#     time.sleep(s)
#     print("Uyandı")
# zaman1 = time.time()
# sleeping(1)
# sleeping(1)
# zaman2 = time.time()
# print(zaman2-zaman1," sn zaman geçti")

# process1 = multiprocessing.Process(target=sleeping,args=(1,))
# process2 = multiprocessing.Process(target=sleeping,args=(1,))
# zaman1 = time.time()
# process1.start()
# process2.start()
# process1.join()
# process2.join()
# zaman2 = time.time()
# print(zaman2-zaman1," sn zaman geçti")


import hashlib
var1 = hashlib.sha256()
var1.update(b"Sekerbank!")
print(var1.digest())
b'Z\xe1\xfa\x99$9HM\xe2\xca\x97@\xa0\xef\xb8\x8a\xa5\xde\x8d@\x1e$\xa5\x0f%\xfc\xd2j\x91\xa9\xf9P'


metin= "Tripanazomigambiyetsiz"
import collections
print(collections.Counter(metin))