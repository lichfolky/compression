stringa = "hello world"
codifica = ""
for simbolo in stringa:
    simbAscii = ord(simbolo)
    if simbAscii < 97 or simbAscii > 122:
        simbAscii = 123
    codifica += f"{(simbAscii - 97):05b}"
print(codifica)
print(len(codifica), "bit")
