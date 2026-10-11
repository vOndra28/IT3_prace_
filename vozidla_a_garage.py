import random

class Vozidlo:
    def __init__(self, znacka:str, rok_vyroby:int, stav_nadrze:int = 100):
        self.znacka = znacka
        self.rok_vyroby = rok_vyroby
        self.stav_nadrze = stav_nadrze
        pass

    def zvuk_motoru(self):
        return "????"

    def info(self):
        return f"vozidlo {self.znacka} // rok výroby {self.rok_vyroby}"

    def startuj(self):
        if(random.randint(0,1) > 0):
            return " nastartovalo!!!"
        else:
            return "bohužel došla šťáva!!!"

class Auto(Vozidlo):
    def __init__(self, znacka, rok_vyroby,typ_prevodovky:str , stav_nadrze = 100):
          super().__init__(znacka, rok_vyroby, stav_nadrze)
          self.typ_prevodovky = typ_prevodovky


    def zvuk_motoru(self):
         return "vrum!" 
    def zatrub(self):
         return "trub! trub!"
    def info(self):
        return f"{super().info()} a {self.typ_prevodovky} "
    


class Moped(Vozidlo):
    def __init__(self, znacka, rok_vyroby, ma_slapadla:bool, stav_nadrze = 100):
        super().__init__(znacka, rok_vyroby, stav_nadrze)
        self._ma_slapadla = ma_slapadla

    def zvuk_motoru(self):
         return "trrrrrr!" 

    def slapej(self):
         return "slapa!!!!"

    def ma_slapadla(self):
        if self.ma_slapadla:
            return "má šlapadla"
        else: 
          return "nemá šlapadla"
        

Skoda = Auto ("Skoda", 2016, "manuál")
print(Skoda.zvuk_motoru())
print(Skoda.zatrub())
print(Skoda.info())
print(Skoda.startuj())

print("--" *20)

Babetta = Moped("Babetta", 1983, True)
print(Babetta.info())
print(Babetta.zvuk_motoru())
print(Babetta.ma_slapadla())
print(Babetta.slapej())
print(Babetta.startuj())

print("--" *20)


garage = [Skoda, Babetta]

for auto in garage:
    print(auto.info())
    print(auto.startuj())
