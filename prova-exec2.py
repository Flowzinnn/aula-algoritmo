

# #def lista_crescente(lista):
#  #   for i in lista:
         

# def criar_lista():
#     lista2 = []
#     while True:
#         lista1 = input('Digite varios números, para parar digite "fim" vamos criar uma lista deles: ')
#         lista2.append(lista1)
        

         
        
        
               
# criar_lista()
# #lista_crescente(lista1)


lista = [1, 3, 5, 7, 4, 2, 9, 12, 3, 15, 10, 20, 25, 22, 30]
lista_ordenada = []
x = 0
for i in lista:
    x += 1
    if i > i + 1 :
        print(f'O valor {i} segue a ordem da lista.')   
        lista_ordenada.append(i)
    else:
        print(f'O valor {i} quebra a ordem da lista.')

set(lista_ordenada)
print('A sequência da lista é: ', lista_ordenada)
