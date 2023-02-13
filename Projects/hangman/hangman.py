#Malik Eddy
#Fall 2018
#Cis 6
#Final Project

#import random module
import random

#txt file with 55,909 words
WORDSLIST_FILENAME = "words.txt"

#hangman ascii art depending on chances left
def display_screen(chances):
	if chances == 10:
		print("\n-----\n|   |\n|\n|\n|\n|\n|\n|\n|\n--------")
	elif chances == 9:
		print("\n-----\n|   |\n|   0\n|\n|\n|\n|\n|\n|\n--------")
	elif chances == 8:
		print("\n-----\n|   |\n|   0\n|  -+-\n|\n|\n|\n|\n|\n--------")
	elif chances == 7:
		print("\n-----\n|   |\n|   0\n| /-+-\n|\n|\n|\n|\n|\n--------")
	elif chances == 6:
		print("\n-----\n|   |\n|   0\n| /-+-\\\n|\n|\n|\n|\n|\n--------")
	elif chances == 5:
		print("\n-----\n|   |\n|   0\n| /-+-\\\n|   |\n|\n|\n|\n|\n--------")
	elif chances == 4:
		print("\n-----\n|   |\n|   0\n| /-+-\\\n|   |\n|   |\n|\n|\n|\n--------")
	elif chances == 3:
		print("\n-----\n|   |\n|   0\n| /-+-\\\n|   |\n|   |\n|  |\n|\n|\n--------")
	elif chances == 2:
		print("\n-----\n|   |\n|   0\n| /-+-\\\n|   |\n|   |\n|  |\n|  |\n|\n--------")
	elif chances == 1:
		print("\n-----\n|   |\n|   0\n| /-+-\\\n|   |\n|   |\n|  | |\n|  |\n|\n--------")

#opens a file with 55909 words
#returns an array with 55909 words
def getWords():
	inFile = open(WORDSLIST_FILENAME, 'r')
	line = inFile.readline()
	wordlist = line.split()
	#uncomment to show # of words in file loaded
	#print(len(wordlist), "words loaded")
	return wordlist

#chooses a random secret word from txt file
#prints the secret word
def ran_word(wordsList):
	return random.choice(wordsList)

#take in the secret word and lettersGuessed list and returns
#a string with all letters, all dashes, or a mixture of both
def getGuessedWord(secret_word, lettersGuessed):
	#create an empty string that will later be filled with
	#characters and underscores
	string = ""
	for letter in secret_word:
		#for each letter in secret word if it is in 
		#our lettersGuessed list add letter to our empty string 
		if letter in lettersGuessed:
			string += letter
		#otherwise add underscores to empty string
		else:
			string += "-"

	return string

#prints a running list of available letters
#based on the user's guess input 
def getAvailableLetters(lettersGuessed):
	#create an empty string that will later be filled with
	#available letters
	string = ""
	#preset available letter
	#includes all letters in alphabet
	s = "abcdefghijklmnopqrstuvwxyz"
	
	#for each letter in s if it is in lettersGuessed list
	#do nothing
	for letter in s:
		if letter in lettersGuessed:
			pass
		#otherwise add available letters to empty string
		else:
			string += letter
	#returns string of available letters
	return string

def game_time(secret_word, chances, lettersGuessed):
	try:
		#while not out of chances continue game
		#While / Else hardest part to code :)
		while(chances != 0):
			#displays game board
			display_screen(chances)

			#prints dashes and caracters of secret word
			print("\n", getGuessedWord(secret_word, lettersGuessed))
			
			#if secret word hasn't been guessed display chances and available letters
			#prompt user to enter a letter
			if secret_word != getGuessedWord(secret_word, lettersGuessed):
				print("\nYou have", chances, "chances left\n")
				print("Available letters:", getAvailableLetters(lettersGuessed))
				guess = input("Please guess a letter: ")
					
				if len(guess) > 1:
					print("\nYou can only enter one letter! Try again.\n")
					game_time(secret_word, chances, lettersGuessed)

				elif guess.lower() not in "abcdefghijklmnopqrstuvwxyz":
					print("\nNot a letter! Try again\n")
					game_time(secret_word, chances, lettersGuessed)
				else:
					#change guess to lowercase
					lc_guess = guess.lower()
				
					#if letter has already been guessed tell user
					#don't deduct chance; add nothing to lettersGuessed list
					if lc_guess in lettersGuessed:
						lc_guess =""
						#print(lettersGuessed)
						print("\nOops! You have already guessed that letter.")

					elif lc_guess not in secret_word:
						lettersGuessed.append(lc_guess)
						print("\nNope! That letter is not in my word.")
						chances -= 1
					else:
						lettersGuessed.append(lc_guess)
						print("\nGood Guess! That letter was in my word.")

			elif secret_word == getGuessedWord(secret_word, lettersGuessed):
				print("\nCongratulations! You won!")
				break
		#will break out while statement and only run once chances = 0
		else:
			print("\n-----\n|   |\n|   0\n| /-+-\\\n|   |\n|   |\n|  | |\n|  | |\n|\n--------")
			print("\nYou lose! The word was:", secret_word)
 
	except KeyboardInterrupt:
		print("You cancelled the program.")

#asks user if they want to start the game	
def start_screen():
	try:
		beginning = input("Press s to start game!\n" + 
			"Press x to exit game.\n")
		if beginning[0] == "s":
			chances = 10
			lettersGuessed = []
			#returns array and places it in all_words variable
			all_words = getWords()
			#**secret_word equals a random lowercase word from
			#our all_words list
			secret_word = ran_word(all_words).lower()

			print("\nI am thinking of a word that is", len(secret_word), "long.")
			#win in 10 tries or less
			print("Try to guess the word in 10 tries or less to win!\n")
			#uncomment to show secret word
			#print(secret_word)

			#load secret word and start guessing game
			game_time(secret_word, chances, lettersGuessed)

			#play again?
			play_again()
		
		#if x pressed, exit
		elif beginning.lower() == "x":
			exit()
		else:
			print("Incorrect input. Try again")
			start_screen()
	
	except KeyboardInterrupt:
		print("You cancelled the program.")


def play_again():
	try:
		print("\nPress p to play again.\nPress x to exit.")
		decision = input("\n")
		if decision[0].lower() == "p":
			start_screen()
		elif decision[0].lower() == "x":
			exit()
		else:
			print("Incorrect input. Try again.")
			play_again()
	except:
		print("An error occurred.")

#exits the program
def exit():
	print("Thank you for playing....Exiting now.")

def main():

	name = input("What is your name? ")
	print("\n############################")
	print("Welcome to Hangman," , name)
	print("############################")

	start_screen()

main()