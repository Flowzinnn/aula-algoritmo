#implementar quantidade de chances para acertar a palavra
#implementar morse code sla como
from random import choice
#jogo da forca

lf = ['banana', 'laranja', 'uva', 'melancia', 'abacaxi']
palavra_secreta = choice(lf)


lista_secreta = ['_'] * len(palavra_secreta)
letras_chutadas = []
enforcou = acertou = False
score = 0
nome = input('Digite seu nome: ')

print(f'Bem vindo {nome}, eu sou o computador, tente advinhar o número que eu pensei!!!')
nd = int(input('Digite 1 para fácil // Digite 2 para médio // Digite 3 para díficil. : ')) # ND = NUMERO DA DIFICULDADE

if nd == 1:
    nt = 5 # NT = NUMERO DE TENTATIVAS
    score_m = 1 # Multiplicador do score
    
elif nd == 2:
    nt = 4    
    score_m = 1.5
else:
    nt = 3
    score_m = 2
    
while not enforcou and not acertou: #loop do jogo
    
    print(f'Tentativas restantes: {nt}')
    print(lista_secreta)
    chute = input('Digite uma letra: ').lower()
    
    if chute in letras_chutadas:
        print('Você já tentou essa letra, tente outra.')
        continue
        
    letras_chutadas.append(chute) # adiciona as letras que já foram chutadas
       
    if chute in palavra_secreta: # detecta se a letra selecionada esta dentro da palavra
        for i, letra in enumerate(palavra_secreta):
            if chute == letra:
               lista_secreta[i] = chute
               score += 100            
    else:    # se a letra nao for detectada na palavra, retorna -1 no numero de tentativas
        score -= 50
        nt-=1
        print(f'Você errou a letra, tentativas restantes:{nt}')
            
    if  lista_secreta == list(palavra_secreta): # se ele acertar todas as letras, o if ativa e ele ganha o jogo
        score = score * score_m  # aqui o multiplicador do score entra em ação para determinar a pontuação do jogador
        print(f'Você acertou, a palavra era {palavra_secreta}')
        print(f'Parabéns, seu score foi de: {int(score)}')
        acertou = True
        
        
    elif nt == 0:    # caso o numero de tentativas chegar a 0 o codigo encerra
        score = score * score_m
        print(f'Suas tentativas acabaram, o jogo acabou!')
        print(f'Seu score foi de: {int(score)}, tente denovo!!!')
        enforcou = True
        