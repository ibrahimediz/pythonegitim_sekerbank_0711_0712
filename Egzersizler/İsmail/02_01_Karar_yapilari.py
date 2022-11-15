var1 = input("Yaş Giriniz")
if var1:
    if var1.isdigit():
        var1 = int(var1)
        if var1 < 30 and var1 > 18: # 18 <= var1 <= 30 
            print("Z Kuşağı")
    else:
        print("Sayısal bir değer girmediniz!")
else:
    print("Değer Girmelisiniz!")
  
