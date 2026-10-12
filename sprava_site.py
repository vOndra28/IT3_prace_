import random

class Sitove_zar:
    def __init__(self, nazev:str, ip_adreda:str, online:bool = False):
        self.nazev = nazev
        self.ip_adresa = ip_adreda
        self.online = online
        pass

    def diagnostika(self):
        if (random.randint(0,1) > 0):
            self.online=True
        return f"momentální stav {self.online}"
        


class router(Sitove_zar):
    def __init__(self, nazev, ip_adreda,pocet_portu:int ,online = False):
        super().__init__(nazev, ip_adreda, online)
        self.pocet_portu = pocet_portu

    def diagnostika(self):
        return f"{super().diagnostika()} Kontroluji Lan porty"
    
    def restart_wifi(self):
        return f"probíhá restart"
    

class server(Sitove_zar):
    def __init__(self, nazev, ip_adreda,os:str = "Ubuntu" , online = False):
        super().__init__(nazev, ip_adreda, online)

    def diagnostika(self):
        return f"{super().diagnostika()} Kontroluji vytížení CPU a stav disků"

print("---" * 20)

router1 =  router("PissFree", 4844848648, 48)
print(router1.diagnostika())
print(router1.restart_wifi())

print("---" * 20)


server1 = server("PissServer", 468448686836)
print(server1.diagnostika())

print("---" * 20)

sit = [router1, server1]

for site in sit:
    print(site.diagnostika())
    


print("---" * 20)