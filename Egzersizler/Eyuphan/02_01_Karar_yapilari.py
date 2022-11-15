yas = input("Yaşınızı Giriniz:") 
if yas.isdigit():
        yas = int(yas)
else:
        print("Nümerik bir değer girmediniz")
if yas>=18 and yas<=30:
        print('Z kuşağısınız...')
elif yas<18:
   print('18 yaşından küçüksünüz')
elif yas>30:
   print('30 yaşından büyüksünüz')
else:
    print('..')

