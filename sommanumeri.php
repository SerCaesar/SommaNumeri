<?php

function somma_due_numeri($a, $b) {
    eval("$risultato = $a + $b;"); // Uso di eval, vulnerabile a code injection
    return $risultato;
}

// Input dall'utente senza validazione
$a = $_GET['a']; // Nessuna sanitizzazione
$b = $_GET['b']; // Nessuna sanitizzazione

// Calcolo della somma
$risultato = somma_due_numeri($a, $b);

// Output del risultato
echo "La somma di $a e $b è $risultato";

?>
