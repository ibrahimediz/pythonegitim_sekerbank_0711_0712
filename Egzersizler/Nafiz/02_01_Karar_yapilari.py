## Kullanıcıdan , yaş bilgisi alınsın. Numeric input olduğu kontrol edilsin.
## Z kuşağı grubu olup olmadığı bilgisi + Uyarı

yas = input("Lütfen Yaşınızı Giriniz .. :") 
if yas:
    if yas.isdigit():
        yas = int(yas)
        if (yas >18 and yas <30):
            print("Z Kuşağı Yaş Grubundsınız")
        else:
            print("Z Kuşağı Yaş Grubunda değilsiniz")
    else:
        print("Nümerik bir değer girmediniz")
else:
    print("Değer Girmediniz")