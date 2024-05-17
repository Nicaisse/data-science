import string,random,re
# 1-kreye yon fonksyon ki ap pran yon paramèt yon mo, epi li retounen envès la.
def reversemo(mo):
    return mo[::-1]
# print(reversemo("Ayiti"))

# 2-kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alfabetik.
def generekod(n):
    lettres = string.ascii_letters
    return ''.join(random.choices(lettres,k=n))

# print(generekod(5))

# 3-kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alfabetik, san repetisyon.
def nodoubkod(n):
    lettres = string.ascii_letters
    tab=set()
    while len(tab)<n:
        tab.add(random.choice(lettres))
    return ''.join(tab)

# print(nodoubkod(5))

# 4-kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alafanimerik, san repetisyon.
def generekof_An(n):
    lettres = string.ascii_letters+string.digits
    tab=set()
    while len(tab)<n:
        tab.add(random.choice(lettres))
    return ''.join(tab)
# print(generekof_An(5))

# 5-Ou gen yon lis chenn. Jenere yon SLUG apati chenn nan. Nan yon SLUG, tout karaktè ki akseptab yo se: alfanimerik ak "-"
def chenn_vers_slug(chenn):
    slug = re.sub(r'[^\w\-]+', '-', chenn.lower()).strip('-')
    return slug
# print(chenn_vers_slug("Yon chenn ki gen karaktè espesyal!?"))

# 6-Kreye yon fonksyon ki ap separe chak lèt nan yon mo ak yon vigil
def separe_vigil(mo):
    return mo.replace('',',')
# print(separe_vigil("AyitiKapabAvanse"))
# 7-Kreye yon fonksyon ki ap kripte yon mo, avèk endèks li nan alfabè a. Chak karaktè dwe separe ak yon tirè
def criptage(mot):
    alfabet=string.ascii_letters
    tab=[]
    for i,caractere in enumerate(mot.lower()):
        carac=caractere
        for j,element2 in enumerate(alfabet):
            if carac==element2:
                index=str(j)
        tab.append(index)
    chaine="-".join(tab)
    print(chaine)

# criptage('ALO')

# #8 Kreye yon fonksyon ki ap dekripte yon mo ki fèt ak endèks chak lèt nan alfabè a, separe ak yon tirè.
def decryptage(chaine):
    alfabet=string.ascii_letters
    tab=[]
    chainesplit=chaine.split('-')
    for num in chainesplit:
        for j,element2 in enumerate(alfabet):
            if int(num)==j:
                tab.append(element2)
    mot="".join(tab)
    print(mot)


# decryptage('0-11-14')

# 9-Kreye yon fonksyon ki ap pran 2 paramèt, epi ki pèmite valè yo. Answit li retounen tou 2 valè yo sou fòm Tuple.
def pemitasyon(val1,val2):
    temp=val1
    val1=val2
    val2=temp
    tipl=(val1,val2)
    print (tipl)
# pemitasyon(5,7)


# 10-Kreye yon fonksyon ki ap pran yon non an paramèt, epi ki retounen inisyal yo. Atansyon ak non konpoze ak tirè yo.
def inisyal(nom):
    while not isinstance(nom,str):
        nom=input('entre un nom sans aucun element numeric')
    inis=re.split(r'[-\s]',nom)
    inisyal_maj=''.join(element[0].upper() for element in inis)
    print (inisyal_maj)
inisyal("Jean-Baptiste Jean")