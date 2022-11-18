cevap = ""
max = 100
min = 0
while True:
  tahmin = round((max+min)/2)
  cevap = input(f"Tuttuğunuz sayı {tahmin} ise 'd', {tahmin}'den büyük ise 'e', {tahmin}'den küçük ise 'h' tuşuna basınız.")
  if cevap:
    if cevap == "d":
      print(f"Tuttuğunuz sayı {tahmin}...")
      break   
    elif cevap == "e":
      min = tahmin
      tahmin = (tahmin + max)/2
    elif cevap == "h":
      max = tahmin
      tahmin = (tahmin + min)/2
  else:
    print("Uygun bir değer giriniz.")
