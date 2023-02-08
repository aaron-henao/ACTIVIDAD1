import random


def listAleatorios(n):
      lista = [0]  * n
      for i in range(n):
          lista[i] = random.randint(0,1000)
      return lista

print("Enter how many numbers do you want to get: ")
n=int(input())

aleatorios=listAleatorios(n)
print(aleatorios)