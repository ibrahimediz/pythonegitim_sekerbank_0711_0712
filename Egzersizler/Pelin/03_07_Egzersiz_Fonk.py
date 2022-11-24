tc = input("TC kimlik numaranızı giriniz:")
print(tc)
if len(tc) !=11:
    print("TC kimlik numaranızı",len(tc)," karakter girdiniz. 11 karakterli giriniz")
else:
 if list(map(int, tc)) ==False:
        print("Girdiğiniz TC karakter içermektedir")
 else:
    if tc[0]==0:
        print("TC kimlik numaranız 0 ile başlayamaz")
    else:
        