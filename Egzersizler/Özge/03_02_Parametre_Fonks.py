def dortgen(a,b):
    print(f"Çevre: {2*(a+b)}")
    print(f"Alan: {a*b}")
dortgen(int(input("ilk kenar: ")),int(input("ikinci kenar: ")))

def fonk(a,b,*args,**kwargs):
    print(a,b)
    print(args)
    print(kwargs)
fonk(1, 2,3,4,5,param1="sdfsdfs")