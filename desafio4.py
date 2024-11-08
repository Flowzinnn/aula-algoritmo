#jogo da forca
#implementar quantidade de chances para acertar a palavra
#implementar morse code sla como
from random import choice
score = 0

lf = ['banana', 'laranja', 'uva', 'melancia', 'abacaxi']
palavra_secreta = choice(lf)


lista_secreta = ['_'] * len(palavra_secreta)
letras_chutadas = []
enforcou = acertou = False
nome = input('Digite seu nome: ')

print(f'Bem vindo {nome}, eu sou o computador, tente advinhar o número que eu pensei!!!')
nd = int(input('Digite 1 para fácil // Digite 2 para médio // Digite 3 para díficil. : ')) # ND = NUMERO DA DIFICULDADE

if nd == 1:
    score_m = 1
    nt = 5 # NT = NUMERO DE TENTATIVAS
    
elif nd == 2:
    nt = 4    
    score_m = 1.5
else:
    nt = 3
    score_m = 2
    
while not enforcou and not acertou:
    print(f'Tentativas restantes: {nt}')
    print(lista_secreta)
    chute = input('Digite uma letra: ').lower()
    
    if chute in letras_chutadas:
        print('Você já tentou essa letra, tente outra.')
        continue
        
    letras_chutadas.append(chute)
       
    if chute in palavra_secreta:
        for i, letra in enumerate(palavra_secreta):
            if chute == letra:
               lista_secreta[i] = chute
               score += 100            
    else:
        score -= 50
        nt-=1
        print(f'Você errou a letra, tentativas restantes:{nt}')
            
    if  lista_secreta == list(palavra_secreta):
        score = score * score_m
        print(f'Você acertou, a palavra era {palavra_secreta}')
        print(f'Parabéns, seu score foi de: {int(score)}')
        acertou = True
        
        
    elif nt == 0:   
        score = score * score_m
        print(f'Suas tentativas acabaram, o jogo acabou!')
        print(f'Seu score foi de: {int(score)}, tente denovo!!!')
        enforcou = True
        