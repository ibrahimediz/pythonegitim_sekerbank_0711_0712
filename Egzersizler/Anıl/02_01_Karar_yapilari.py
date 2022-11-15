yas=input("Yaşiniz: ")
if yas:
  if yas.isdigit():
      yas=int(yas)
      if 17<yas<31:
        print("Z kuşağisiniz")
      else:
        print("Başka bir kuşaksiniz")
  else: 
    print("Nümerik bir değer girmediniz")
else: print("Değer girmediniz")
