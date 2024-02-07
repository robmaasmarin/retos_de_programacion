myDict = {"A": "a", "B": "b", "C": "c", "D": "d", "E":"e", "F": "f", "G": "g", "H": "h", "I": "i", "J": "j", "K": "k", "L": "l", "M": "m", "N": "n", "Ñ": "ñ", "O": "o", "P": "p", "Q": "q", "R": "r", "S": "s", "T": "t", "U": "u", "V": "v", "W": "w", "X": "x", "Y": "y", "Z": "z"}

#print("a" in myDict.values())

def primeraMayuscula(palabra):
    miPalabra = list(palabra)
    palabraFinal = ""

    if miPalabra[0] not in myDict.values():
        print("Nothing to modify: " + palabra)
    else:

        for key, value in myDict.items():
            if miPalabra[0] == value:
                miPalabra[0] = key
                print("Word after modification: " + "".join(miPalabra))
            continue
        

primeraMayuscula("hola")
primeraMayuscula("cola")
primeraMayuscula("Cola")
primeraMayuscula("YIOJOJOIJIJHHIOGOG")
primeraMayuscula("fdhaifhdpasofhaiohfd")