#expressões regulares
import re #regular expression

texto = 'Meu email é exemplo@gmail.com e você pode me contatar em outroemail@yahoo.com'

resultado = len(re.findall('@', texto)) #a função vai procurar as ocorrências de @ na variável texto
#a variavel resultado vai guardar o tamanho do resultado retornado pela função

print(f'O caracter @ apareceu {resultado} vezes na frase')

#para encontrar a palavra posterior à desejada
result = re.findall(r'você (\w+)', texto)

print(f'A palavra após você é: {result[0]}')

text = 'O aluno estava incrivelmente perdido, mas encontrou a DSA e rapidamente começou a aprender'
