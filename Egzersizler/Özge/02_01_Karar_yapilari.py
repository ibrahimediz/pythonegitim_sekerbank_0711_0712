yas = input("Yaşınızı giriniz:")
if yas:
    if yas.isdigit():
         yas = int(yas)
         if yas>=18 and yas<=30:
            print("Z kuşağı")
         else:
            print("Z kuşağı değilsiniz.")
    else:
        print("Nümerik değer girmediniz.")
else:
    print("Değer girmediniz.") 
    