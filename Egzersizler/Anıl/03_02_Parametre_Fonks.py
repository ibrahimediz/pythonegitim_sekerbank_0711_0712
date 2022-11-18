def dortgen(a,b):
    print(f"Çevre: {2*(a+b)}")
    print(f"Alan: {a*b}")
dortgen(int(input("uzun kenar: ")),int(input("kısa kenar: ")))

def fonk(a,b):
    print(f"Çevre: {2*(a+b)}")
    print(f"alan: {a*b}")
fonk(int(input("uzun kenar: ")), int(input("kısa kenar: ")))

def fonk(a,b,*args,**kwargs):
    print(args)
    print(kwargs)
fonk(1,2,3,4,5,6,param="Anıl")

   


 