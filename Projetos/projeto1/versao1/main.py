#Jogo da forca em Python

import random
from os import system, name

#limpando a tela a cada execução
def limpa_tela():
    if name == 'nt':
        _= system('cls') #para windows
    else:
        _= system('clear') #para mac ou linux

def game():
    limpa_tela()

    print('\nBem-vindo(a) ao jogo da forca')
    print('Adivinhe a palavra abaixo:\n')

    palavras = ['banana', 'abacate', 'morango', 'pitaya', 'laranja', 'kiwi']

    palavra = random.choice(palavras) #escolhe a palavra para o jogo

    palavra_escolhida = ['_' for letra in palavra] #define os tracinhos de acordo com a quantidade de letras da palavra escolhida

    chances = 6

    letras_erradas = [] #lista para armazenar as letras erradas

    while chances > 0:
        print(' '.join(palavra_escolhida))
        print('\nChances restantes: ',chances)
        print('Letras erradas:',' '.join(letras_erradas))

        tentativa = input('Digite uma letra: ').lower()

        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    palavra_escolhida[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        if '_' not in palavra_escolhida:
            print('Você venceu! A palavra era:',palavra)
            break
    
    if '_' in palavra_escolhida:
            print('Você perdeu! A palavra era:',palavra)

if __name__ == "__main__":
    game()
