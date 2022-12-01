class Cokgen:
    sinifOzelligi = "Çokgen"
    def __init__(self,kenarsayisi,isim):
        self.kenarsayisi = kenarsayisi
        self.isim = isim
        self.icacitoplami()
        print(Cokgen.sinifOzelligi)

    def icacitoplami(self):
        print(f"{self.isim} Kenar Sayısı: {self.kenarsayisi}  İç açı toplamı:",(self.kenarsayisi-2)*180)

ucgen = Cokgen(3, "Üçgen")
kare = Cokgen(4, "Kare")
