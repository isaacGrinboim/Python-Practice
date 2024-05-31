import random
import os
import time
import requests

def get_words_from_subject(subject):
    url = f"https://api.datamuse.com/words?ml={subject}" # words related to subject
    # url = f"https://api.datamuse.com/words?rel_jjb={subject}" #other ways to describe subject
    response = requests.get(url)
    if response.status_code == 200:
        word_nodes = response.json()
        return [word_node['word'] for word_node in word_nodes]
    else:
        print("Failed to fetch words")
        return []


over = False
letters_found = 0
letters_used = []
strikes = 0
max_strikes = 8
guess = ''
pic = [
"""
      
      
      
_____|
"""
,

"""
      
      
     |
_____|
"""
,

"""
      
     |
     |
_____|
"""
,

"""
     |
     |
     |
_____|
"""
,

"""
  []-|
     |
     |
_____|
"""
,

"""
  []-|
   | |
     |
_____|
"""

,

"""
  []-|
   | |
   | |
_____|
"""
,

"""
  []-|
  /| |
   | |
_____|
""",

"""
  []-|
  /| |
  /| |
_____|
"""

]
os.system('cls')
print("Welcome to hangman game")
words = []
while words == []:
    print("-Enter a subject-")
    words = get_words_from_subject(input())
word = words[random.randint(0,len(words))]
word_to_show = ["_" for letter in word]
os.system('cls')
print(pic[strikes].splitlines()[1] , word_to_show)
while(not over):
    found = False
    print(pic[strikes].splitlines()[2] , "letters guessed by now: ", letters_used)
    print(pic[strikes].splitlines()[3] , "strikes you made: ", strikes)
    print(pic[strikes].splitlines()[4] , "guess a letter")

    while True:
        guess = input().lower()
        if guess not in letters_used:
            break
        print("you already used that letter")


    for index,letter in enumerate(word):
        if (guess in letter.lower() or guess in letter.upper()) and word_to_show[index] == "_":
            letters_found+=1
            found = True
            word_to_show[index] = letter
    if not found:
        strikes += 1
    letters_used.append(guess)
    if strikes != max_strikes:
        os.system('cls')
        print(pic[strikes].splitlines()[1] , word_to_show)
    if letters_found == len(word) or strikes == max_strikes:
        over = True

if strikes == max_strikes:
    os.system('cls')
    for line in pic[strikes].splitlines():
        print(line)
    print("The word was: ", word)
    print("You have lost")
    
else:
    print("You have won")











