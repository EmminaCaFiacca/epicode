import math
def calcola_quadrato(lato=None):
    if lato is None:
        lato = float(input("Inserisci il lato del quadrato: "))
    perimetro = lato * 4
    area = lato ** 2
    return perimetro, area
 
def calcola_rettangolo(base=None, altezza=None):
    if base is None:
        base = float(input("Inserisci la base del rettangolo: "))
    if altezza is None:
        altezza = float(input("Inserisci l'altezza del rettangolo: "))
    perimetro = base * 2 + altezza * 2
    area = base * altezza
    return perimetro, area
 
def calcola_cerchio(raggio=None):
    if raggio is None:
        raggio = float(input("Inserisci il raggio del cerchio: "))
    perimetro = 2 * math.pi * raggio
    area = math.pi * raggio ** 2
    return perimetro, area

def calcolo():
    print("❒ Ciao! questo programma calcola il perimetro e l'area di una figura geometrica ❒")
   
    figure_disponibili = ["Quadrato", "Rettangolo", "Cerchio"]
    valore = float(input("\nInserisci il valore iniziale (lato/raggio): "))

    while figure_disponibili:
        print("\nFigure disponibili:")
        for i, figura in enumerate(figure_disponibili):
            print(f"{i + 1}: {figura}")

        scelta = int(input("Scegli una figura (inserisci il numero): "))
        if scelta < 1 or scelta > len(figure_disponibili):
            print("Scelta non valida.")
            continue

        figura = figure_disponibili.pop(scelta - 1)

        if figura == "Quadrato":
            perimetro, area = calcola_quadrato(lato=valore)
        elif figura == "Rettangolo":
            perimetro, area = calcola_rettangolo(base=valore, altezza=valore / 2)
        elif figura == "Cerchio":
            perimetro, area = calcola_cerchio(raggio=valore)

        print(f"Perimetro del {figura}: {perimetro}")
        print(f"Area del {figura}: {area}")

      
        valore = area

        if not figure_disponibili:
            print("\nNon ci sono più figure disponibili. Il programma termina.")
            break

        continua = input("Vuoi continuare? (s/n): ")
        if continua.lower() != "s":
            break

calcolo()

