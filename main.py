"""
Tento kód by šel dát do funkcí, ale účelem je si spíš vyzkoušet logiku.
"""

import random
# tady by mohla být funkce na získání slova z textového souboru
words = ["autobaterie", "monitor", "křeslo", "guláš", "beruška"]
chosen_word = random.choice(words).upper()
hidden_word = "-" * len(chosen_word)
attempts = len(chosen_word)
input_letter = ""
guessed_letters = []
print("Hádané slovo má {0} písmen.\n{1}".format(len(chosen_word), hidden_word))

while attempts > 0:
    # ošetření vstupu uživatele
    wrong = True
    while wrong:
        input_letter = input("Zvol písmeno: ").upper()
        if (input_letter.isalpha()) and (len(input_letter) == 1):
            wrong = False
        else:
            print("Špatně! Nevíš, co je to písmeno? Zkus to znovu.")
            wrong = True

    if input_letter in guessed_letters:
        print("Toto písmeno už jsi zkoušel.")
        attempts -= 1
    elif input_letter in chosen_word:
        hidden_word = chosen_word
        guessed_letters.append(input_letter)
        for i in chosen_word:
            if i not in guessed_letters: hidden_word = hidden_word.replace(i, "-")
    else:
        guessed_letters.append(input_letter)
        attempts -= 1
    
    if hidden_word == chosen_word:
        print("{}\nGratuluji, uhádl jsi slovo!".format(chosen_word))
        break

    print(hidden_word)
    print("\nZbývající pokusy: {}".format(attempts))
    print("Zvolená písmena: {}".format(guessed_letters))

if attempts <= 0: print("\nBohužel. Došly Ti pokusy a prohrál jsi.")
