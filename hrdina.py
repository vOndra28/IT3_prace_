class Hrdina:
    def __init__ (self, jmeno:str, LEVEL:int, lokace:str = "Tajemný hrad v Karpatech"):
            self.jmeno = jmeno
            self.LEVEL = LEVEL
            self.lokace = lokace


            pass

    def zvuk(self):
        return "Garhhhhh..."

    def predstav_se(self):
        return "To jsem já..."

    def kde_jsi(self):
        return f"Kde jsi? Jsem v{self.lokace}"

    def presun_se(self, nlokace:str ):
        self.lokace = nlokace
        return f"presunul jsem se na {nlokace}. {self.kde_jsi()}"


Hrdina1 = Hrdina("Jiří z Poděbrad", 18)

print(Hrdina1.jmeno)
print(Hrdina1.LEVEL)
print(Hrdina1.lokace)
print(Hrdina1.zvuk())
print(Hrdina1.predstav_se())
print(Hrdina1.kde_jsi())
print(Hrdina1.presun_se("Babylon"))
print(Hrdina1.kde_jsi())
