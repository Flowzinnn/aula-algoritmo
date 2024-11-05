for i in range(2, 11, 2): #primeiro numero serve para indicar o começo, o segundo sera o termino, e o terceiro sera de x em x ou seja, pulando as casas de x em x
    if i % 2 == 0:
        print(i)
        
        
palavra = 'python'

numeros = [1, 2, 34, 3, 4, 5, 6, 'wolf', True, 3.14]

print(numeros[7])

print(palavra.upper())
print(palavra.lower())

for letra in palavra:
    print(letra)

for n in numeros:
    print(n)

for i in range(len(numeros)):
    print(numeros[i])

print(numeros[7][2])