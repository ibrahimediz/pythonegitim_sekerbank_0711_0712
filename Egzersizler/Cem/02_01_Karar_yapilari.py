
while True:
    try:
        yas = int(input("Plese enter a age: "))
        print("veri tipi basarili",yas)
        if int(yas)>= 18 and int(yas)<=30:
            print("z kusağısınız yasınız: ",yas)
        elif int(yas)>30:
            print("30'dan büyük")
        else:
            print("18'den büyük")
        break
    except ValueError:
        print("Please enter a valid integer")