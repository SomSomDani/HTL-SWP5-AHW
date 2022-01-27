class Knoten:
    def __init__(self, daten):
        self.vorher = None
        self.daten = daten
        self.nächste = None


class verketteListe:
    def __init__(self):
        self.Kopf = None

    def __init__(self):
        self.Kopf = None

    def einfügen(self, neuer_Knoten):
        if self.Kopf:
            letzte_Knoten = self.Kopf
            while letzte_Knoten.nächste != None:
                letzte_Knoten = letzte_Knoten.nächste
            neuer_Knoten.vorher = letzte_Knoten
            letzte_Knoten.nächste = neuer_Knoten
        else:
            self.Kopf = neuer_Knoten

    def ausgabe(self):
        print("Normal Sortiert:", end="")
        temp_Knoten = self.Kopf
        while temp_Knoten != None:
            print(temp_Knoten.daten, end='-')
            temp_Knoten = temp_Knoten.nächste
        print()

        print("Ungedreht Sortiert:", end="")
        letzte_Knoten = self.Kopf
        while letzte_Knoten.nächste != None:
            letzte_Knoten = letzte_Knoten.nächste
        temp_Knoten = letzte_Knoten
        while temp_Knoten != None:
            print(temp_Knoten.daten, end="|")
            temp_Knoten = temp_Knoten.vorher
        print()


if __name__ == '__main__':
    vlist = verketteListe()
    vlist.einfügen(Knoten(1))
    vlist.einfügen(Knoten(3))
    vlist.einfügen(Knoten(7))
    vlist.einfügen(Knoten(2))
    vlist.einfügen(Knoten(5))
    vlist.einfügen(Knoten(9))
    vlist.einfügen(Knoten(6))
    vlist.ausgabe()
