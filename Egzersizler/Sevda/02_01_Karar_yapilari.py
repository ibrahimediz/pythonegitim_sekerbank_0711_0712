i=2
if i%2==0:
    print(i)

    yas= input("yasiniz:")
    if yas:
        if yas.isdigit():
            yas=int(yas)
            if yas<30 and yas>18:
                print("Z kuşağındasınız :)")
            else: 
                print("Z kusagi degilsiniz ")
        else:
            print("Numerik deger girilmeli.")
    else:    
        print("Değer girmediniz")




