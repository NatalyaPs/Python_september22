# задача 4. напиш.прогр, к-я будет на вход принимать число N 
# и выводить числа от -N до N

#n = int(input())
#i = -n
#while i <= n:
 #   print(i)
  #  i+=1

n = int(input())
for i in range(-n, n+1, 1):
    print(i)


# или сделать красивый вывод в строке

n = int(input())
mass = []
for i in range(-n, n+1, 1):
    mass.append(i)
print(mass)


# или
n = int(input())
mass = []
for i in range(-n, n+1, 1):
    print(i,end=" ")