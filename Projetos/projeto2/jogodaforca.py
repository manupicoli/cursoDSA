# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
from os import system, name

def limpa_tela():
    if name == 'nt':
        _= system('cls')
    else:
        _= system('clear')

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

# Classe
class Hangman:
    def __init__(self, palavra): #espera uma palavra ao inicializar
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_escolhidas = []

    def adivinha_letra(self, letra): #guess
        #verifica se a letra está na palavra e separa de acordo nas listas inicializadas
        if letra in self.palavra and letra not in self.letras_escolhidas: 
            self.letras_escolhidas.append(letra)
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        else:
            return False
        return True
    
    def verifica_derrota(self): #hagman_over
        return self.verifica_vitoria() or (len(self.letras_erradas) == 6)
		
    def verifica_vitoria(self): #hangman_won
        if '_' not in self.verifica_letra(): #se nã tem mais '_' significa que todas as letras foram adivinhadas
            return True
        return False
		
    def verifica_letra(self ): #hide_palavra
        espaco = ''

        for letra in self.palavra:
            if letra not in self.letras_escolhidas:
                espaco += '_'
            else:
                espaco += letra

        return espaco
		
    def verifica_status(self): #print_game_status   
        print(board[len(self.letras_erradas)])
        print('\nPalavra: ' + self.verifica_letra())
        print('\nLetras erradas: ',)

        for letra in self.letras_erradas:
            print(letra,)

        print()

        print('Letras corretas: ')

        for letra in self.letras_escolhidas:
            print(letra,)

        print()

def escolhe_palavra():
    palavras = ['abacate', 'laranja', 'kiwi', 'morango', 'abacaxi', 'nectarina']

    palavra = random.choice(palavras)

    return palavra

def main():
    limpa_tela()

    game = Hangman(escolhe_palavra())

    while not game.verifica_derrota():
        game.verifica_status()

        user_input = input('\nDigite uma letra: ')

        game.adivinha_letra(user_input)
    
    game.verifica_status()

    if game.verifica_vitoria():
        print('Parabéns! Você venceu.')

    else:
        print('Game over! Você perdeu.')
        print('A palavra era: ' + game.palavra)

    print('Obrigada!')

if __name__ == "__main__":
    main()