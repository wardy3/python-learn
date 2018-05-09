import sys
import scrabble

def valid_word(word, rack):
#def valid_word(word, available_letters):
    available_letters = rack[:]
    for letter in word:
        #print("letter "+letter+" word "+word+" avail "+str(available_letters))
        if letter not in available_letters:
            #print ("nup")
            return False
        available_letters.remove(letter)
    return True

def compute_score(word):
    score = 0
    for letter in word:
        score += scrabble.scores[letter]
    return score


if len(sys.argv) < 2:
    print("Usage: scrabble.py [RACK]")
    exit(1)


rack = list(sys.argv[1].lower())
valid_words = []

for word in scrabble.wordlist:
    #print ("Checking word "+word+" can be made from "+str(rack))
    if valid_word(word, rack):
        score = compute_score(word)
        valid_words.append([score, word])

valid_words.sort(reverse=True)
for play in valid_words:
    score = play[0]
    word  = play[1]
    print(word + ": " + str(score))
