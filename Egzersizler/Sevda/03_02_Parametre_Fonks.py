def alan_cevre(a,b):
    cins="Kare" if a==b else "Dikdörtgen"
    print(f"{cins} nin alanı :{a*b}")
    print(f"{cins} nin cevresi :{2*(a+b)}")
kenarlar=list(map(int,input("a,b giriniz:").split(",")))
alan_cevre(int(kenarlar[0]),int(kenarlar[1]))
