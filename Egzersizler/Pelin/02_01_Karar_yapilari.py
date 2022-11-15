#if
a=2
if a==2:
    print("doğru")
    print("evet")

yas = input("yaş giriniz:")
if yas:
    yas=int(yas)
    print(f"5 yıl sonra : {yas + 5} yaşında olacaksınız")
yas = input("yaş giriniz:")
if yas:
    if yas.isdigit():
     yas=int(yas)
     print(f"5 yıl sonra : {yas + 5} yaşında olacaksınız")
if yas:
    if yas.isdigit():
        yas=int(yas)
        print(f"5 yıl sonra : {yas + 5} yaşında olacaksınız")
    else:
        print("numerik değer girmediniz")        
else:
    print("değer girmediniz")


# egzersiz:
yas = input("yaş giriniz:")
