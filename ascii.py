stringa = "hello world"
asci = ""
for simbolo in stringa:
    # ord è l'opposto di chr()
    # f-string serve a convertire in byte
    asci += f"{ord(simbolo):08b}"

print(asci)
print(len(asci), "bit")
