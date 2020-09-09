import random
print('H A N G M A N\n')
words = ('python', 'java', 'kotlin', 'javascript')
word = list(random.choice(words))
answer = list(len(word) * '-')
#print(answer)
chances = 8
guess = ''
guessed = set()
#hint = word[:3] + (len(word)-3) * '-'
#print("You survived!" if input(f"Guess the word: {hint}") == word else "You are hanged!")
while chances > 0:
    print(f"\n{''.join(answer)}")
    guess = input('Input a letter: ')
    if len(guess) != 1:
        print("You should input a single letter")
        continue
    elif guess not in 'abcdefghijklmnopqrstuvwxyz':
        print("It is not an ASCII lowercase letter")
        continue
    elif answer.count(guess) != 0 or guess in guessed:
        print("You already typed this letter")
        continue
    elif guess in set(word):
        while guess in set(word):
            answer[word.index(guess)] = guess
            word[word.index(guess)] = '-'
    else:
        print('No such letter in the word')
        chances -= 1
    if word.count('-') == len(word):
        print("You guessed the word!\nYou survived!")
        break
    guessed.add(guess)
if "-" in answer:
    print("You are hanged!")
    

#print("\nThanks for playing!\nWe'll see how well you did in the next stage")