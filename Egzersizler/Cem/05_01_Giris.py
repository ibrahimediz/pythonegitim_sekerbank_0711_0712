class Sinif:
    sinifOzelligi = "Sınıf Özelliği" # sınıf özelliği
     
    def __init__(self,a): # yapıcı fonksiyon
        self.ornekozellik = a # örnek özellik

    
    @classmethod
    def sinifmetodu(cls): # sınıf metodu
        print(cls.sinifOzelliği)

    def ornekmetod(self): # örnek metodu
        print(self.ornekozellik)

    
    def __del__(self): # yıkıcı fonksiyon
        print(self.ornekozellik,"Silindi")
        print(self.ornekozellik,"Silindi")


a = Sinif(3)
b = Sinif(5)
a>b