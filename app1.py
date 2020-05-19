import json
import difflib

def printDefinition(word, data):    
    if word == None:
        getUserWord(data)
    elif word in data:
        word = word.lower() 
        for definition in data[word]:
            print(definition)
    else:
        print('This word was not found in the database')

def checkIfValidWord(word, data):
    if word in data:
        return word
    else:
        possibleWord = difflib.get_close_matches(word, data.keys(), 1)
        if len(possibleWord) > 0:
            response = input('Did you mean %s \n Y/y - yes / N/n - no ' % possibleWord[0])
            if response.lower() == 'y':
                return possibleWord[0]
            elif response.lower() == 'n':
                return None
            else:
                print('Invalid response')
                return checkIfValidWord(word, data)
        else:
            return word

def getUserWord(data):
    user_word = input('Enter a word: ')
    printDefinition(checkIfValidWord(user_word, data), data)

with open('data.json') as file:
    data = dict(json.load(file))

for i in range(10):
    print(i)
    getUserWord(data)




