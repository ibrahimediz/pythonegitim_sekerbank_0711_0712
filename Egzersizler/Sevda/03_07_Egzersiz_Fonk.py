tckn=input("TCKN Giriniz:")
if tckn.isdigit() and len(tckn)==11:
  ttek=sum(int(i) for i in tckn[0:10:2])
  tcift=sum(int(i) for i in tckn[1:9:2])
  t=sum(int(i) for i in tckn[0:10])
  print(t,ttek,tcift)
  if (ttek*7-ttek)%10 == tckn[9] and t==tckn[10]:
    print(1)
  else: print(0)
else: print(0)
