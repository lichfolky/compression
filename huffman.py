from utils import contaFrequenze, Tree, genera_codifica_huffman

testo = "hello world"
"""
testo = "In informatica, un albero o struttura ad albero (tree in inglese) è la struttura dati che si riconduce al concetto di albero con radice presente nella teoria dei grafi. Un albero si compone di due tipi di sottostrutture fondamentali: il nodo, che in genere contiene informazioni, e l'arco, che stabilisce un collegamento gerarchico fra due nodi: si parla allora di un nodo padre dal quale esce un arco orientato che lo collega a un nodo figlio. Si chiede inoltre che ogni nodo possa avere al massimo un unico arco entrante, mentre dai diversi nodi possono uscire diversi numeri di archi uscenti. Si chiede infine che l'albero possegga un unico nodo privo di arco entrante: questo nodo viene detto radice (root) dell'albero. Ogni nodo che non presenta archi uscenti è detto foglia (leaf node) e in ogni albero finito, cioè con un numero finito di nodi, si trova almeno un nodo foglia. Ovviamente, un nodo può essere contemporaneamente padre (se ha archi uscenti) e figlio (se ha un arco entrante, ovvero se è diverso dalla radice). Solitamente ogni nodo porta con sé delle informazioni e molto spesso anche una chiave con cui è possibile identificarlo univocamente all'interno dell'albero. L'altezza o profondità dell'albero è il massimo delle lunghezze dei suoi cammini massimali, cammini che vanno dalla radice alle sue foglie."
"""
freq_dizionario = contaFrequenze(testo)
forest = []
for simbolo, freq in freq_dizionario.items():
    forest.append(Tree(freq, None, None, simbolo))
print(forest)

# Ordina i simboli da codificare in una lista, in base alla loro frequenza
forest.sort(key=lambda x: x.freq, reverse=True)
print(forest)

# Ripeti i seguenti passi finché la lista non contiene un singolo elemento:
while len(forest) > 1:
    # Prendi dalla lista i due simboli con la frequenza di conteggio minore.
    # (gli ultimi 2 dato che sono ordinati)
    elemento1 = forest.pop()
    elemento2 = forest.pop()
    print("prendo ", elemento1, elemento2)
    # Crea un albero che ha come "figli" questi due elementi, e crea un nodo genitore che ha come dato la somma delle loro frequenze
    nuovo_albero = Tree(elemento1.freq + elemento2.freq, elemento1, elemento2, None)
    print("inserisco ", nuovo_albero)

    forest.append(nuovo_albero)
    forest.sort(key=lambda x: x.freq, reverse=True)
    print("---", forest)

radice = forest.pop()
codifica = genera_codifica_huffman(radice)
print(codifica)


code = ""
for simbolo in testo:
    code += codifica[simbolo]
print(len(testo) * 8)
print(len(code))
print(f"{len(code) / (len(testo) * 8):.0%} di compressione")
