#sumatoria de 1+2+3+4+5+...+n
#n=3, s=6
#n=5, s=15


i=1
s=0
n=int(input('Dame n:'))
while i<=n:
  s=s+i #acomular
  i+=1 #contador
#FOR
#n=int(input('Dame n:'))
#s=0
#for i in range(1+n+1):  
#    s=s+i
print("la sumatoria es:",s)
