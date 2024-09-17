from os import system, name
import random
from  hangman_words import word_list
from hangman_art import stages, logo
def clear():

    if name == 'nt':
        _ = system('cls')

print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

display = []
for _ in range(word_length):
    display += "_"

end_of_game = False
print(f"{' '.join(display)}")

while end_of_game == False:
    guess = input("Rate einen Buchstaben: ").lower()
    clear()

    if guess in display:
        print(f"Du hast den Buchstaben {guess} bereits geraten.  ")

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"Du hast den Buchstaben {guess} eingegeben, Der Buchstabe ist nicht im Wort enthalten. Du verlierst ein Leben")
        lives = lives -1

        if lives == 0:
            end_of_game = True
            print("Alle Leben verbraucht!\nGAME OVER!")
            print(f"das gesuchte Wort war: {chosen_word}")

    print(stages[lives])
    if "_" not in display:
        end_of_game = True
        print("Gewonnen!")
