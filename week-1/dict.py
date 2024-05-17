# 1-Ou gen yon diksyonè. Rekipere tout valè yo, gras ak kle yo epi retounen yon lis valè.
entreprises = {
    "non": "Jean",
    "sirname": "Baptiste",
    "age": 30,
    "vil": "Pòtoprens",
    "plis": [1, 2, 3],
    
}
key_list=[key for key in entreprises.keys()]
# print(key_list)


# 2-Mande itilizatè a, tape yon valè... epi verifye si l gen akolad devan ak dèyè.
# user=input('type something: ')
# if user[0]=='{' and user[-1]=='}':
#     print('li gen akolad devan ak dèyè')
# else:
    # print('li pa gen akolad devan ak dèyè')

# 3-Pakouri yon diksyonè, epi afiche tout kle yo.
# for i in entreprises.keys():
#     print(i)

# 4-Pakouri yon diksyonè, epi afiche tout valè yo.
# for i in entreprises.values():
#     print(i)
    


# 5-Pakouri yon diksyonè, pou w kapab kreye yon kopi(nouvo) sou disksyonè sa.
copydict=entreprises.copy()
# print(copydict)

# 6-Anndan yon diksyonè ki gen kle ak valè(valè yo ka nenpòt tip done). Ajoute yon underscore devan ak dèyè tout valè ki se chenn yo. Ekzanp:
for eleman in entreprises:
    if isinstance(entreprises[eleman], str):
        entreprises[eleman]="_"+ entreprises[eleman] + "_"
        
# print(entreprises)

# 7-Nan yon diksyonè ki gen valè ki se chenn sèlman. Kreye yon nouvo diksyonè ki gen tout eleman ki gen valè ki dijit yo sèlman. Ekzanp:
dict_digits={eleman:entreprises[eleman] for eleman in entreprises if isinstance(entreprises[eleman], int)}

# print(dict_digits)


# 8-Pakouri yon disksyonè, pou w mete l sou fòm lis, kote chak eleman nan disksyonè sa, vin sou fòm tipl(kle, valè) anndan lis la. Ekzanp:
listegzanp={"non": "12", "b": "abc", "c": "12r", "d":"90"}
listtip=[]
for eleman in listegzanp:
    # tipl=(eleman, listegzanp[eleman])
    listtip.append((eleman, listegzanp[eleman]))

# print(listtip)

# 9-Pakouri yon lis tipl, pou w mete l sou fòm diksyonè. Ekzanp:
listdict=dict(listtip)

# print(listdict)
# 10-Kole 2 diksyonè ansanm pou fè youn, kote si gen eleman ki gen menm kle ap konkatene valè, swivan kondisyon sa yo:
diksyone1 = {
    "non": "Jean",
    "sirname": "Baptiste",
    "age": 30,
    "vil": "Pòtoprens",
    "plis": [1, 2, 3],
    'pow': 'pow',
    
}

diksyone2 = {
    "non": "Marie",
    "sirname": "Lorel",
    "age": 25,
    "vil": "Gonaïves",
    "plis": {4, 5, 6},
    'paw': 'paw',
    
}
adisyondict = {}
for key, value in diksyone1.items():
    if key in diksyone2:
        if isinstance(value, int) and isinstance(diksyone2[key], int):
            adisyondict.update({key: diksyone2[key]+ value})
        else:
            adisyondict.update({key: str(diksyone2[key])+' '+ str(value)})
print(adisyondict)
