a1= input("1. açıyı giriniz:")
a1 = int(a1) if a1 and a1.isdigit() else -1
a2= input("2. açıyı giriniz:")
a2 = int(a2) if a2 and a2.isdigit() else -1
a1_2=  int(a1)+ int(a2)
a3=180-a1_2
if a1==a2==a3:
    print("Eşkenar Üçgen")
else:
    if a1==a2 or a1==a3 or a2==a3:
        print("İkizkenar Üçgen")
    else:
        if a1==90 or a2==90 or a3==90:
            print("Dik Üçgen")
        else:
            print("Çeşitkenar Üçgen")



