yas = input("Yaşınızı Giriniz:") # str veri tipinde giriş 
if yas:
    if yas.isdigit():
        yas = int(yas)
        if yas>=18 and yas<30:
            print(f"Z Kuşağı")
        else:
            print (f"Z Kuşağı değilsiniz")
    else:
        print("Girdiğiniz Değer Nümerik Değildir")
else:
    print("Lütfen Değer Giriniz")