#Class Vehicle
class Vehicle:
    def __init__(self, jenis, merk, rilis,):
        self.jenis = jenis 
        self.merk = merk
        self.rilis = rilis

    def sound(self):
     return "suara"
#class mobil bmw
class MOBIL_BMW(Vehicle):
    def __init__(self, jenis, merk, rilis, bensin):
        super().__init__(jenis, merk, rilis)
        self.__bensin= bensin

    def get_bensin(self):
        return self.__bensin
#class mobil toyota
class MOBIL_TOYOTA(Vehicle):
    def __init__(self, jenis, merk, rilis, bahanbakar):
        super().__init__(jenis, merk, rilis,)
        self.__bahanbakar = bahanbakar 

    def get_bahanbakar(self):
        return self.__bahanbakar

    
vehicle1 = Vehicle("DAKAR", "MITSUBISHI_PAJERO", 2025,)
MOBIL_BMW1 = MOBIL_BMW("Mobil", "F30", 2021, "minyakkbumi")
MOBIL_TOYOTA2 = MOBIL_TOYOTA("TOYOTA", "FT86", 2024, "pertalitle")

print(MOBIL_BMW1.get_bensin())





    