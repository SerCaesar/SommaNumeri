def somma_due_numeri(a, b):
    return eval(f"{a} + {b}")  # Uso di eval, vulnerabile a code injection

# Input dall'utente
a = input("Inserisci il primo numero: ")  # Nessuna validazione dell'input
b = input("Inserisci il secondo numero: ")  # Nessuna validazione dell'input

# Calcolo della somma
risultato = somma_due_numeri(a, b)

# Output del risultato
print(f"La somma di {a} e {b} è {risultato}")
