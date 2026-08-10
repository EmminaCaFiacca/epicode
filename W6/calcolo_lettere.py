def calcolo_lettere(A):
    return [len(parola) for parola in A]

if __name__ == "__main__":
    n = int(input("Quante parole vuoi inserire? "))
    A = []
    for i in range(n):
        parola = input(f"Inserisci la parola {i + 1}: ")
        A.append(parola)

    B = calcolo_lettere(A)
    print("\nLista A:", A)
    print("Lista B:", B)