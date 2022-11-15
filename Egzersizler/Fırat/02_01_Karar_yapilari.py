yas = input('Yasinizi giriniz')
if yas.isdigit():
    if int(yas) in range(18,31):
        print("Z Kuşağı")
    # for a in range(18,31):
    #     if int(yas)==a:
    #        print('Z kusagı')
    #        break         
else:
    print('girdiginiz deger numeric degildir')


