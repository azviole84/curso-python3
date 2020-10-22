#lista=[[1,2,3],[4,50,6],[7,'Juan',9]]
#print(lista)

lista=[]
r=int(input('dame renglones:'))
c=int(input('dame colunmas:'))

for i in range(0,r):
    lista.append([])
    for j in range(0,c):
         lista[i].append(int(input('Dame un numero:')))


   

for i in lista:
    for j in i:
      #print(j,end=' ') #imprima como una matris 
      #print("%5d"%j,end=' ')
      print("{0:>5}".format(j), end='')
    print()

"""
#range

for i in range(0,len(lista)):
    for j in range(0,len(lista[i])):
         print(lista[i][j],end=' ')
    print()
"""
13=[[[1,2,3],[4,5,6],[7,8,9]],[[1,1],[2,2],[3,3]]]
print(13[0][1][0]])

