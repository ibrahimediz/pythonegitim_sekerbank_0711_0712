yas = input("Yaşınızı Giriniz:")
if yas:
    if yas.isdigit():
        if int(yas)>= 18 and int(yas)<=30:
            print("Z Kuşağı")
        else: 
            print("Çıkar Telefonunu")
    else:
        print("Nümerik bir değer girmediniz")
else:
    print("Değer Girmediniz")

        