def contaFrequenze(testo):
    freq = {}
    for simbolo in testo:
        freq[simbolo] = freq.get(simbolo, 0) + 1
    return freq


class Tree:
    def __init__(self, freq, left, right, simbolo):
        self.left = left
        self.right = right
        self.simbolo = simbolo
        self.freq = freq

    def __repr__(self) -> str:
        if self.simbolo != None:
            return "(" + str(self.simbolo) + ": " + str(self.freq) + ")"
        else:
            return "{" + str(self.freq) + "}"


# codice_corrente accumula il codice corrente
# codici accumula tutti i codici trovati
def genera_codifica_huffman(nodo, codice_corrente="", codici={}):
    if nodo is None:
        return

    if nodo.simbolo is not None:
        codici[nodo.simbolo] = codice_corrente

    # Ricorsione per i rami sinistra e destra
    genera_codifica_huffman(nodo.left, codice_corrente + "0", codici)
    genera_codifica_huffman(nodo.right, codice_corrente + "1", codici)

    return codici
