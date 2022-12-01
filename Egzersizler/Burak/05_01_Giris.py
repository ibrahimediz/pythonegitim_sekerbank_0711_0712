class Cokgen:
    def __init__(self,kenarsayisi,isim):
        self.kenarsayisi = kenarsayisi
        self.isim = isim

        def icacitoplami(self):
            print(f"{self.isim} Kenar Sayısı : {self.kenarsayisi} İç açı toplamı:",(self.kenarsayisi-2)*180)

ucgen = Cokgen(3,"Üçgen")
kare = Cokgen(4, "Dörtgen")