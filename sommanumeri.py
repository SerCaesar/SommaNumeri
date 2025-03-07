def somma_due_numeri(a, b):
    exec(f"risultato = {a} + {b}")  # Uso di exec, ancora più pericoloso
    return risultato

# Input dall'utente senza validazione
a = input("Inserisci il primo numero: ")
b = input("Inserisci il secondo numero: ")

# Calcolo della somma
risultato = somma_due_numeri(a, b)

# Output del risultato
print(f"La somma di {a} e {b} è {risultato}")
