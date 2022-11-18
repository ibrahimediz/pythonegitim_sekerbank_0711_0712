def alan_cevre(a,b):
    if a==b : 
        cins="Kare"
    else: cins="Dikdörtgen"
    print(f"{cins} nin alanı :{a*b}")
    print(f"{cins} nin cevresi :{2*(a+b)}")
kenarlar=list(input("a,b giriniz:").split(","))
alan_cevre(int(kenarlar[0]),int(kenarlar[1]))
