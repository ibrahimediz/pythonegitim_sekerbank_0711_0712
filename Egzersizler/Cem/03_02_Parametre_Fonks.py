def topla(a,b):
        print(f"{a}+{b}={a+b}")
        print("çevre: ",(a+b) *2 ,"cm'dir")
        print("alan: ",a*b ,"cm2'dir")
topla(2,3)

def topla(*args):
    sonuc = 0
    for item in args:
        if isinstance(item,float) or isinstance(item,int):
            sonuc += item
    print(sonuc)
topla()
topla(2,3)
topla(1,2,3,2,2,2,"a",1,1,2.3)