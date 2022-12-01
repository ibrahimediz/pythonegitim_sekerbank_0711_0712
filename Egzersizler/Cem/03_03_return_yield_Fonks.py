class Cokgen:
    sinifOzelligi = "Çokgen"
    def __init__(self,kenarsayisi,ismi):
        self.kenarsayisi = kenarsayisi
        self.ismi = ismi
        self.icacitoplami()
        print(Cokgen.sinifOzelligi)
    
    def icacitoplami(self):
        print(Cokgen.sinifOzelligi)
        print(f"{self.ismi} Kenar Sayısı: İç açı toplanı:",(self.kenarsayisi-2)*180)
    

ucgen = Cokgen(3,"Üçgen")
kare = Cokgen(4,"Kare")

ucgen.icacitoplami()
kare.icacitoplami()

ucgen = Cokgen(3,"Üçgen2")
kare = Cokgen(4,"Kare2")
