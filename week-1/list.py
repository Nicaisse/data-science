# 1-Kreye yon lis eleman ki divizib pa 2, nan entèval [0-n] enklizif
def pair(n):
    return [i for i in range(n) if i%2==0]
# print(pair(15))


# 2-Ou gen yon lis antye, konvèti l an yon lis chenn.
listchenn=[str(i) for i in [1,2,3,4,5,6,7,8,9]]
# print(listchenn)


#3-Ou gen yon lis chenn ki an miniskil, konvèti an yon lis chenn majiskil
listmajiskil=[i.upper() for i in ["ayibobo", "ayiti"]]
# print(listmajiskil)

# 4-Ou gen yon lis, kreye yon nouvo lis ki fèt ak eleman ki nan endèks ki divizib pa 3 yo sèlman
liste_nombres = [10, 20, 30, 40, 50, 60, 70, 80, 90]
listdiv3=[i for i in liste_nombres if i%3==0]
# print(listdiv3)

# 5-Ou gen lis eleman, kreye yon nouvo lis ki gen chak 3 eleman yo gwoupe anndan yon tipl. Ekzanp:
egznp=[1,2,3,4,5,6,7,8,9]
newlist=[]
for i in range(0,len(egznp),3):
    if i+2<len(egznp):
        newlist.append((egznp[i],egznp[i+1],egznp[i+2]))
# print(newlist)



# 6-Ou gen yon lis, ki gen yon pakèt eleman ki repete. Konvèti l an yon lis, ki pa gen okenn doublon. 
noboub=list(set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 5, 6, 7, 8]))
# print(noboub)

# 7-Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman komen ant 2 lis yo.
list_A = [1, 2, 3, 4, 5, 6, 7, 8]
list_B = [1, 2, 3, 4]
list_C=[i for i in list_A if i in list_B]
# print(list_C)

# 8-Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman distenge ant 2 lis yo.
listdistenge=[i for i in list_A if i not in list_B]
# print(listdistenge)

# 9-Ou gen yon diksyonè. Kreye yon nouvo lis ak kle yo sèlman, epi yon lòt ak valè yo sèlman.
entreprises = {
    "non": "Jean",
    "sirname": "Baptiste",
    "age": 30,
    "vil": "Pòtoprens",
    "plis": [1, 2, 3],
    
}
key_list=[key for key in entreprises.keys()]
value_list=[value for value in entreprises.values()]
# print(key_list)
# print(value_list)



# 10-Reyini 3 lis ansanm, san okenn doublon.
list3=list(set(list_A+list_B+list_C))
# print(list3)

