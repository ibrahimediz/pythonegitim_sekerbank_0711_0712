class cokgen:

    def __init__(self,kenar,isim): # yapıcı fonksiyon
        self.kenari = kenar # örnek özellik
        self.ismi = isim # örnek özellik
        self.icacilartoplami=0

    
    @classmethod
    def ornekmetod(self): # örnek metodu
        self.icacilartoplami= (self.kenari-2)*180
        print(self.isim," iç açılar toplamı:" ,self.icacilartoplami)

    
    def __del__(self): # yıkıcı fonksiyon
        print(self,"Silindi")

ucgen=cokgen(3, "Ucgen")
ucgen.ornekmetod()