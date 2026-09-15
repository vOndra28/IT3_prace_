class Zvire:
    def __init__(self, jmeno:str, vek:int, misto:str = "bouda"):
        self.jmeno = jmeno
        self.vek = vek
        self.misto = misto
       
        
        pass
    def zvuk(self):
        return "???"
    def predstav_se(self):
        return f"Jmenuji se{self.jmeno}, je mi {self.vek} let."
    def kde_jsi(self):
        return f"Kde jsi? Jsem v{self.misto}"
    def jdi_na(self, nmisto:str):
        self.misto = nmisto
        return f"presunul jsem se na {nmisto}. {self.kde_jsi()}"


zvire = Zvire("Luděk", 22,)
print(zvire.jmeno)
print(zvire.vek)
print(zvire.misto)
print(zvire.zvuk())
print(zvire.predstav_se())
print(zvire.kde_jsi())
print(zvire.jdi_na())
print(zvire.kde_jsi())




zvire2 = Zvire("Amlka", 5, "Zahrada")
print(zvire2.jmeno)
print(zvire2.vek)
print(zvire2.misto)
print(zvire2.zvuk())
