class motorka:
    def __init__(self, znacka:str, kat:str, stav_nadrze:int, stav_stojanku:str):
        self.znacka = znacka
        self.kat = kat
        self.stav_nadrze = stav_nadrze
        self.stav_stojanku = stav_stojanku

        pass


    def zatoc_plyn(self):
        return "Vruuuuuum"
    
    def popis_moto(self):
        return f"Značka: {self.znacka} // Kategorie: {self.kat} // Stav nádrže: {self.stav_nadrze} "
    
    def stav_stojanu(self):
        return f"Stojánek je {self.stav_stojanku}"
    
    def novy_stav_stoj(self, novy_stav_stojanu:str):
        self.stav_stojanku = novy_stav_stojanu
        return f"nový stav stojanu je {novy_stav_stojanu}"
    
    def popojed(self, uber_pal:int):
        self.stav_nadrze -= uber_pal

        return f"Popojel jsem 15km a ubralo se mi {uber_pal}litrů"
    
    def novy_stav_nadrz(self, nstav_nad):
        self.stav_nadrze = nstav_nad
        return f"nový stav nádrže je {nstav_nad}"
    
    
        

moto = motorka("suzuki", "naháč", 100, "Vyklopen")

print(moto.zatoc_plyn())

print(moto.popis_moto())

print(moto.stav_stojanu())
    
print(moto.novy_stav_stoj("zaklopen"))

print(moto.popojed(5))