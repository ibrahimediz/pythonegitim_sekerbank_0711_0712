# yas = input("Yaşınızı Giriniz:")
    if yas.isdigit():
        if int(yas)>= 18 and int(yas)<=30:
            print("Z Kuşağı")
        else: 
            print("Çıkar Telefonunu")
    else:
        print("Nümerik bir değer girmediniz")
else:
    print("Değer Girmediniz")


açılar1 = input("Birinci Açıyı giriniz")
açılar2 = input("İkinci Açıyı giriniz")
açılar1 = int(açılar1) if açılar1 and açılar1.isdigit() else -1
açılar2 = int(açılar2) if açılar2 and açılar2.isdigit() else -1
açılar3 = 180-(açılar1+açılar2)
if açılar1 == açılar2 and açılar3 == açılar1:
    print("Eşkenar Üçgen")
elif açılar1 or açılar2 ==90:
    print("Dik Üçgen")
elif açılar1 == açılar2 and açılar3 == açılar1:
    print("İkizkenar Üçgen")
elif açılar1 != açılar2 and açılar3 !=açılar2:
    print("Çeşitkenar Üçgen")
else:
    print("Nice Try")




