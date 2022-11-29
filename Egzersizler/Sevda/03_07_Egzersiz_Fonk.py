"""
Kurallar:
* 11 hanelidir.
* Her hanesi rakamsal değer içerir.
* İlk hane 0 olamaz.
* 1. 3. 5. 7. ve 9. hanelerin toplamının 7 katından, 2. 4. 6. ve 8. hanelerin toplamı çıkartıldığında, elde edilen sonucun 10'a bölümünden kalan, yani Mod10'u bize 10. haneyi verir.
* 1. 2. 3. 4. 5. 6. 7. 8. 9. ve 10. hanelerin toplamından elde edilen sonucun 10'a bölümünden kalan, yani Mod10'u bize 11. haneyi verir.
"""

def tckn_kontrol(tckn):
  tckn=list(map(int,tckn))
  tek=cift=t10=0
  for i in range(0,10):
    if i<9: #9 =10.hane
      if i%2==0:
        tek+=tckn[i] #1-3-5-7-9 haneler 0-2-4-6-8
      else:
        cift+=tckn[i] #2-4-6-8 haneler 1-3-5-7
        
    t10+=tckn[i]
  if (tek*7-cift)%10==tckn[9] and t10%10==tckn[10]:
    return 1
  else: return 0

inpTCKN=input("TCKN Giriniz:")
if inpTCKN.isdigit() and len(inpTCKN)==11:
  print(tckn_kontrol(inpTCKN))
else: print("Tamamı rakamlardan oluşan 13 haneli bir TCKN giriniz.")

