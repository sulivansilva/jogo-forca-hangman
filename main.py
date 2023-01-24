# Importando lista de palavras e imagens. 

import random
from replit import clear
from words import lista_palavras
from hangman_art import stages
from hangman_art import logo

print("Bem vindo ao jogo da forca!\n")
print(logo)
print("\n")


# O jogo escolhe uma palavra aleatória de lista_palavras e armazena na variável palavra_secreta.

palavra_secreta = random.choice(lista_palavras)
#print(palavra_secreta)

# Variáveis

display = []
len_palavra = len(palavra_secreta)
fim_do_jogo = False
vidas = 6

# Preenchendo a variável 'display'. 

for letra in range (len_palavra):
    display.append("_") 
print(display)
print("\n")

# Loop que verifica se a letra que o joagdor escolheu é igual a alguma letra da palavra secreta.

while fim_do_jogo == False:
    palpite = input("Escolha uma letra: ").lower()

    clear()

    if palpite in display:
        print("Você já usou essa letra, escolha outra letra.")
        
    print("\n")
    
    for posicao in range(len_palavra):
        letra = palavra_secreta[posicao]
        if letra == palpite:            
            display[posicao] = letra            
    print(display)
    print("\n")

    if palpite not in palavra_secreta:
        print(f"A letra '{palpite}' não existe nessa palavra, você perdeu uma vida.")
        print(stages[vidas])
        vidas -= 1 
        if vidas < 0:
            print(f"Fim de jogo, você perdeu! A palavra secreta era '{palavra_secreta}'")
            fim_do_jogo = True

    if "_" not in display:
        print(f"Parabéns! A palavra secreta era '{palavra_secreta}'!")
        fim_do_jogo = True