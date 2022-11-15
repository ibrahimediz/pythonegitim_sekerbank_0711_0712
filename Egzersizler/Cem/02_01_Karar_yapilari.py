
yas = (input("Yaşınızı Giriniz:")) 
if yas:
    if yas.isdigit():
        yas=int(yas)
        if int(yas)>= 18 and int(yas)<=30:
            print("z kusağısınız yasınız: ",yas)
        else: print("z kusağı değilsiniz, yasınız : ",yas)
    else:
        print("Değer Girmediniz")

