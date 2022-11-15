yas = input("Yaşınızı Giriniz:") # str veri tipinde giriş 
if yas:
    if yas.isdigit():
        yas = int(yas)
        print(f"5 yıl sonra => {yas + 5} yaşında olacaksınız")
    else:
        print("Nümerik bir değer girmediniz")
else:
    print("Değer Girmediniz")