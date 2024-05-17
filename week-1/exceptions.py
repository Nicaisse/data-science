# 1-Mande itilizatè a tape yon chif, epi ajoute +5. Kapte eksepsyon ki ka rive si itilizatè a pa tape yon dijit.
try:
    chif = int(input("Tape yon chif: "))
    rezilta = chif + 5
    print("Rezilta a se:", rezilta)
except ValueError:
    print("Ou pa tape yon chif kòrèkman.")
    

# 2-Anndan yon lis. Endekse yon valè nan lis la. Kapte eksepsyon ki ka fèt si endeks la depase longè lis la, epi afiche yon mesaj.
liste = [1, 2, 3, 4, 5]

try:
    endeks = int(input("Tape yon endeks: "))
    valè = liste[endeks]
    print("Valè a nan pozisyon", endeks, "se:", valè)
except IndexError:
    print("Endeks la depase longè lis la.")
except ValueError:
    print("Ou pa tape yon endeks kòrèkteman.")

# 3-Anndan yon diskyonè. Kapte eksepsyon ki ka rive si kle a pa nan diksyonè a. Si li pa ladan, ajoute kle sa ak valè None.
diksyonè = {"kle1": 1, "kle2": 2, "kle3": 3}

try:
    kle = input("Tape yon kle: ")
    valè = diksyonè[kle]
    print("Valè a pou kle", kle, "se:", valè)
except KeyError:
    print("Kle sa pa nan diksyonè a.")
    diksyonè[kle] = None
    print("Kle a ajoute nan diksyonè a ak valè None.")
    print(diksyonè)

# 4-Kreye yon enstans apati yon klas ou te kreye. Kapte eksepsyon ki ka fèt si gen yon atribi ki pa ekziste nan klas la. Epi ajoute atribi sa.
class klassatribi:
    def __init__(self, atribi1, atribi2):
        self.atribi1 = atribi1
        self.atribi2 = atribi2

    def afiche_atribi(self):
        print("Atribi 1:", self.atribi1)
        print("Atribi 2:", self.atribi2)

mwen_enstans = klassatribi("valè1", "valè2")
try:
    print("Atribi 3:", mwen_enstans.atribi3)
except AttributeError:
    print("Klas la pa gen atribi sa.")
    mwen_enstans.atribi3 = "nouvo valè"
    print("Atribi sa ajoute nan klas la.")
    print("Atribi 3:", mwen_enstans.atribi3)
    
# 5-Kreye yon enstans apati yon klas ou te kreye. Kapte eksepsyon ki ka fèt si yon moun rele yon atribi sou fòm fonksyon, epi afiche yon mesaj ki di li pa yon fonksyon.
class klasstest:
    def __init__(self, atribi):
        self.atribi = atribi

    def afiche_atribi(self):
        print("Atribi mwen se:", self.atribi)

enstans = klasstest("valè atribi")

try:
    rezilta = enstans.atribi()
except TypeError:
    print("Atribi a pa yon fonksyon.")

# 6-Jenere pwòp erè pa w, si itilizatè a pa tape yon chenn (miniskil oubyen majiskil) ki fè pati chif women yo. "IVXLCDM"
karakter_asepte = "IVXLCDM"

def verifye_chèn(chèn):
    for ch in chèn:
        if ch not in karakter_asepte:
            return False
    return True

try:
    chèn = input("Tape yon chèn ki gen chif women yo: ")
    if not verifye_chèn(chèn.upper()):
        raise ValueError("Ou pa tape yon chèn ki gen chif women yo.")
except ValueError as err:
    print(err)
