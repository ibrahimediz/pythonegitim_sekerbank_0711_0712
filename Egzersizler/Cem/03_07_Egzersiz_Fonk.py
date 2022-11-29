inpTCKN = "10000000146" 
# inpTCKN=input("TCKN Giriniz:")
def TCKimlikKontrol(inpTCKN):
    dogrulama = False
    if inpTCKN.isdigit() and len(inpTCKN)==11:
        if inpTCKN[0] != "0":
            liste = list(map(int,inpTCKN))
            if (sum(liste[0:9:2])*7 - sum(liste[1:8:2])) % 10 == liste[9]:
                if sum(liste[0:10]) % 10 == liste[10]:
                    dogrulama = True
    return dogrulama

TCKimlikKontrol(inpTCKN)