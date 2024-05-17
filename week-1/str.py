# 1-Nan yon chenn karaktè, mete tout karaktè yo an miniskil.
karakte="AYITI"
karakte=karakte.lower()
# print(karakte)

# 2-Nan yon chenn karaktè, koupe chenn nan tout kote ki gen espas. Epi afiche yon lis ki gen chak eleman yo. Ekzanp:
chen="Ayibobo Ayiti"
# print(chen.split(' '))

# 3-Nan yon chenn karaktè, mete tout premye lèt chak mo an majiskil.
chenkarakte="endeks premye karaktè"
a=chenkarakte.title()
print(a)

# 4- Nan yon chenn karaktè, rekipere premye lèt chak mo. Epi afiche yon nouvo chenn ak tout inisyal sa yo.
mot=''.join([mot[0] for mot in chenkarakte.split(' ')])
print(mot)

# 5-Ranplase tout karaktè "a" ki nan yon chenn pa "@"
replace=karakte.replace('a','@')
print(replace)

# 6-Mete yon chenn karaktè devan dèyè, answit mete l an majiskil. 
inves=karakte[::-1].upper()
print(inves)

# 7-Afiche endeks premye karaktè "a" ki nan yon chenn. :
endeks1=None
for i,karak in enumerate(chen):
    if karak=='a':
        endeks1=i
        # print(endeks1)
        break
if endeks1==None:
    print('nan chenn nan pa gen a ')

# 8-Afiche total tout endeks karaktè "a" ki nan yon chenn (Kit se a majiskil oubyen miniskil). Ekzanp:
total=0
result = sum([i for i,karak in enumerate("Ayiti kapab avanse") if karak.lower() == 'a'])
# print(result)

# 9-Kreye yon lis ki gen endeks tout karaktè "a" ki nan yon chenn (Sèlman a miniskil). Ekzanp:
listendeks=[i for i,karak in enumerate("Ayiti kapab avanse") if karak=='a']
print(listendeks)

# 10-Retire tout espas ki nan yon chenn, epi kole chenn sa ak kantite karaktè li genyen (Pa kontwole espas yo).
nouvochenn=''.join("Ayiti kapab avanse".replace(' ','') + str(len("Ayiti kapab avanse".replace(' ',''))))
# print(nouvochenn)

