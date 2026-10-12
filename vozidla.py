import random

class vozidlo:
    def __init__(self, znacka:str, rok_vyroby:int, stav_nadrze:int = 100):
        self.znacka = znacka
        self.rok_vyroby = rok_vyroby
        self.stav_nadrze = stav_nadrze
        pass

    def zvuk_motoru(self):
        return "????"
    
    def info(self):
        return f"značka: {self.znacka} // rok výroby: {self.rok_vyroby} "
    
    def startuj_se(self):
        if(random.randint(0,1) > 0):
            return f"nastartováno {self.zvuk_motoru}"
        else:
            return "došla šťáva bouráku"

class Auto(vozidlo):
    def __init__(self, znacka,typ_prevodovky:str , rok_vyroby, stav_nadrze = 100):
        super().__init__(znacka, rok_vyroby, stav_nadrze)
        self.typ_prevodovky = typ_prevodovky

    def zvuk_motoru(self):
        return f"{super().zvuk_motoru()} vrum! vrum!"
    
    def zatrub(self):
        return "trub! trub!"
    

class moped(vozidlo):
    def __init__(self, znacka, rok_vyroby,ma_slapadla:bool ,  stav_nadrze = 100):
        super().__init__(znacka, rok_vyroby, stav_nadrze)
        self.ma_slapadla = ma_slapadla 

    def ma_slapadlo(self):
        if self.ma_slapadla:
           typ = "má šlapadla"
        else:
            typ = "nemá šlapdla"

        return f"{self.znacka} ... {typ} "

    def zvuk_motoru(self, slapej:str):
        self.slapej = slapej 
        return f"{super().zvuk_motoru()} Trrrrrrrrr! a {slapej}"
    
Volvo = vozidlo("volvo","2001")
print(Volvo.zvuk_motoru())
print(Volvo.info())
print(Volvo.startuj_se())


print("---" * 20)

Skoda = Auto("Skoda", "Manuální", "2015")
print(Skoda.info())
print(Skoda.zvuk_motoru())
print(Skoda.zatrub())

print("---" * 20)

Babetta = moped("Jawa", 1985, True)
print(Babetta.info())
print(Babetta.zvuk_motoru("Slapej"))
print(Babetta.ma_slapadlo())





garaz = [Volvo, Skoda, Babetta]

for auto in garaz:
    print(auto.info())