#jogo da forca
#implementar quantidade de chances para acertar a palavra
#implementar morse code sla como

palavra_secreta = 'banana'
lista_secreta = ['_', '_', '_', '_', '_', '_']
enforcou = acertou = False

while not enforcou and not acertou:
    print(lista_secreta)
    chute = input('Digite uma letra: ').lower()
    
    
    for i, letra in enumerate(palavra_secreta):
        if chute == letra:
            lista_secreta[i] = chute
    if  lista_secreta == list(palavra_secreta):
        acertou = True