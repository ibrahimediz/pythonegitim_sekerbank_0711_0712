yas = input("Yaşınızı Giriniz:")
if yas:
    if yas.isdigit():
        yas = int(yas)
        print(f"")
    else:
        print("Nümerik bir değer girmediniz")
else:
    print("Değer Girmediniz")