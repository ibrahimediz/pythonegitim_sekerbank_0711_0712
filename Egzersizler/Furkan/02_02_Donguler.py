cevap = ""
max_ = 100
min_ = 0
while True:
  tahmin = (max_+min_)//2
  cevap = input(f"Tuttuğunuz sayı {tahmin} ise '3', yukarı ise '1', aşağı ise '2' tuşuna basınız.")
  if cevap:
    if cevap == "3":
      print(f"Tuttuğunuz sayı {tahmin}...")
      break   
    elif cevap == "1":
      min_ = tahmin
    elif cevap == "2":
      max_ = tahmin
    tahmin = (tahmin + min_)//2
  else:
    print("Uygun bir değer giriniz.")
