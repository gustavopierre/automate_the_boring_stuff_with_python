# Este e um jogo de adivinhar o numero
import random

secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Peca para o jogador adivinhar 6 vezes
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # Esta condicao corresponde ao palpite correto10

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope! The number I was thinking of was ' + str(secretNumber))
