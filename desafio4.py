#jogo da forca
#implementar quantidade de chances para acertar a palavra
#implementar morse code sla como

palavra_secreta = 'banana'
lista_secreta = ['_', '_', '_', '_', '_', '_']
enforcou = acertou = False

nome = input('Digite seu nome: ')
print(f'Bem vindo {nome}, eu sou o computador, tente advinhar o número que eu pensei!!!')
nd = int(input('Digite 1 para fácil // Digite 2 para médio // Digite 3 para díficil. : ')) # ND = NUMERO DA DIFICULDADE

if nd == 1:
    nt = 5 # NT = NUMERO DE TENTATIVAS

elif nd == 2:
    nt = 4    

else:
    nt = 3
    
    while not enforcou and not acertou:
        print(f'Tentativas restantes: {nt}')
        print(lista_secreta)
        chute = input('Digite uma letra: ').lower()
                   
        for i, letra in enumerate(palavra_secreta):
            if chute == letra:
                lista_secreta[i] = chute
            else:
                print(f'Você errou a letra, tentativas restantes:{nt}')
                nt-=1
        if  lista_secreta == list(palavra_secreta):
            print(f'Você acertou, a palavra era {palavra_secreta}')
            acertou = True
            or nt == 0:   
            print(f'Suas tentativas acabaram, o jogo acabou!')
            enforcou = True