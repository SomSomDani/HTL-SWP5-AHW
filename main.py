class Knoten:
    def __init__(self, daten):
        self.daten = daten
        self.naechste = None
        return
        
    def besitzt_Wert(self,wert):
        if self.daten == wert:
            return True
        else:
            return False
            
class verketteListe:
    def __init__(self):
        self.Kopf = None
        self.Pfad = None
        return
    
    def hinzufügen_Element_in_Liste(self, item):
        if not isinstance(item, Knoten):
            item = Knoten(item)
        
        if self.Kopf is None:
            self.Kopf = item
        else:
            self.Pfad.naechste = item
        
        self.Pfad = item
        return
    
    def listen_länge(self):
        count = 0
        derzeitiger_Knoten = self.Kopf
        
        while derzeitiger_Knoten is not None:
            count = count +1
            derzeitiger_Knoten = derzeitiger_Knoten.naechste
        return count
        
    def ausgabe_liste(self):
        derzeitiger_Knoten = self.Kopf
        ausgabe = []
        while derzeitiger_Knoten is not None:
            ausgabe.append(derzeitiger_Knoten.daten)
            derzeitiger_Knoten = derzeitiger_Knoten.naechste
        print(ausgabe)

    def ungeordnete_Suche(self, value):
        derzeitiger_Knoten = self.Kopf
        Knoten_Id = 1
        ergebnis = []
        
        while derzeitiger_Knoten is not None:
            if derzeitiger_Knoten.besitzt_Wert(value):
                ergebnis.append(Knoten_Id)
            derzeitiger_Knoten = derzeitiger_Knoten.naechste
            Knoten_Id = Knoten_Id +1
        
        return ergebnis
    
    def entfernen_Element(self, item_id):
        derzeitige_id = 1
        derzeitiger_Knoten = self.Kopf
        Knoten_davor = None

        while derzeitiger_Knoten is not None:
            if derzeitige_id == item_id:
                if Knoten_davor is not None:
                    Knoten_davor.naechste = derzeitiger_Knoten.naechste
                else:
                    self.head = derzeitiger_Knoten.naechste
                    return

            Knoten_davor = derzeitiger_Knoten
            derzeitiger_Knoten = derzeitiger_Knoten.naechste
            derzeitige_id = derzeitige_id + 1

        return
        
    def hinzufügen_random(self):
        import random
        laenge = int(input("Länge?: "))
        for i in range(laenge):
            Knoten_input = random.randint(0,100)
            list.hinzufügen_Element_in_Liste(Knoten_input)
    
    def ausgabe(self):
        print("Länge : %i" % list.listen_länge())
        list.ausgabe_liste()
    
    def loeschen(self):
        item_id = int(input("Welches Element sollte gelöscht werden?: "))
        list.entfernen_Element(item_id)
        self.ausgabe()
    
    def suche(self):
        item_value = int(input("Welches Element sollte gesucht werden?: "))
        print(list.ungeordnete_Suche(item_value))
        
    def menü(self):
        repeat = True
        answer = None
        while(repeat):
            answer = input("Löschen [l] - Suche [s] - Beenden [any]").lower()
            if answer == "l":
                self.loeschen()
            elif answer == "s":
                self.suche()
            else:
                repeat = False
                print("Verlassen")
                

if __name__ == '__main__':
    list = verketteListe()
    list.hinzufügen_random()
    list.ausgabe()
    
    list.menü()
