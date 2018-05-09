import scrabble
#import sys

#search = sys.argv[1]

letters = "abcdefghijklmnopqrstuvwxyz"

def has_double(letter):
    for word in scrabble.wordlist:
        if letter + letter in word:
            return True
    return False


def has_all_the_vowels(word):
    vowels = "aeiou"

    for vowel in vowels:
        if vowel not in word:
            return False

    return True

def score_of(word):
    score = 0

    for letter in word:
        score += scrabble.scores[letter]

    return score


# Summarise word lengths and scores

summ = {}

for word in scrabble.wordlist:
    score = score_of(word)
    length = len(word)

    if score not in summ:
        summ[score] = {}
    if length not in summ[score]:
        summ[score][length] = []

    summ[score][length].append(word)

for score in sorted(summ):
    print("Words with score "+str(score)+" : ")
    for length in sorted(summ[score]):
        if length < 10:
            print("\tLength "+str(length)+"\t: "+str(summ[score][length]))



'''
# for letter in letters:
    # print("Check for double "+letter +" ...")

    # if not has_double(letter):
        # print ("Nope. "+letter+" has no double")


total = 0
all_vowels = 0
shortest = 99
longest = 0

for word in scrabble.wordlist:
    total += 1
    if has_all_the_vowels(word):
        #print ("Look! "+word+" has all the vowels")
        all_vowels += 1
        if len(word) < shortest:
            shortest = len(word)
            print ("New shortest word is " + word )
            print ("and it has a score of " + str(score_of(word)))
        elif len(word) > longest:
            longest = len(word)
            print ("New longest word is " + word )
            print ("and it has a score of " + str(score_of(word)))

print("Total " + str(total) + ", all vowels " + str(all_vowels) +
        " and the shortest has " + str(shortest) + " letters.")
'''
