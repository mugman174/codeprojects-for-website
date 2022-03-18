import readline, sys, random
from colorama import Back, Style
from spellchecker import SpellChecker # pyspellchecker
RED, GREEN, YELLOW, GRAY, RESET = Back.RED, Back.GREEN, Back.YELLOW, Style.DIM, Style.RESET_ALL

spell = SpellChecker()

print(f"{GREEN}Worfdolew - The Worfd Game\nEnter your guesses and see if they're correct. {RESET}\n\n")

with open("wordlist.txt") as wordlist:
	words = wordlist.read().strip().splitlines()
word = random.choice(words)
won = False

def handle_guess(guess):
	global words
	already = []
	if spell.correction(guess) != guess:
		return f"{RED}{guess}{RESET}", False
	if guess == word:
		return f"{GREEN}{guess}{RESET}", True
	guess = list(guess[:5])
	for i in range(len(guess)):
		if guess[i] == word[i] and guess[i] not in already:
			already.append(guess[i])
			guess[i] = f"{GREEN} {guess[i]} {RESET}"
		elif guess[i] in word and guess[i] not in already:
			already.append(guess[i])
			guess[i] = f"{YELLOW} {guess[i]} {RESET}"
		else:
			guess[i] = f"{GRAY} {guess[i]} {RESET}"
	return ' '.join(guess), False

for i in range(6):
	guess = input("\r")
	print(f"\033[F", end="")
	x = handle_guess(guess)
	sys.stdout.flush()
	if x[0]: print(x[0])
	if x[1]:
		won = True
		break

if won:
	print("\nYou won!")
else:
	print(f"The word was {word}.")
