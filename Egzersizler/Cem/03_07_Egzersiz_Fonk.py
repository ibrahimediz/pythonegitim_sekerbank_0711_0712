#tckno=input("tck girin")
tckno = 12345685325
tckno_str = str(tckno)

print("str",tckno_str)
print(isinstance(tckno, int))
print(str(tckno)[0])

if 1==1 and len(tckno_str) == 11 and tckno_str[0] != 0:
    print("doğru")
else:
    print("nope")

print(tckno)


 #isinstance(tckno, int) 
#     if 1==1 and len(tckno) == 11 and tckno[0] != 0:
