# readFile
# Takes argument of fileName in string
# Returns dictionary of all words in file, with each word as a key
# each value as the number of times key word is present in the text so far

def readFile(fileName):
  #print(fileName)
  file = open(fileName, 'r') # open file 

  index = {}
  for line in file:
    line = file.readline() #save line into string line
    words = line.split() #split line into list of words

    for word in words:
      if (word != '\n') and (word!= ""):
        if word in index:
          index[word] += 1 #increment
          num = index[word]
        else:
          index[word] = 1
  file.close()
  return index
  
  
# readFileCapitals
# Takes argument of fileName in string
# Returns dictionary of all CAPITAL words in file, with each word as a key
# each value as the number of times key word is present in the text so far

def readFileCapitals(fileName):
  #print(fileName)
  file = open(fileName, 'r') # open file 

  index = {}
  for line in file:
    line = file.readline() #save line into string line
    words = line.split() #split line into list of words

    for word in words:
      if (word != '\n') and (word!= "") and word[0].isupper():
        if word in index:
          index[word] += 1 #increment
          num = index[word]
        else:
          index[word] = 1
  file.close()
  return index
  
# sortWords
# Takes argument of a dictionary where words are keys and # of times they appear are values
# Returns a list of words sorted by 
def sortWords(dictionary):
  wordList = sorted(dictionary, key=dictionary.get, reverse=True)
  return wordList
  
  
# printWords
# takes in a wordList with words sorted in order of how common they are
# and dictionary with values
# No return value; prints words and # of times they appear in descending order

def printWords(wordList, dictionary):
  i = 0
  for word in wordList:
    print(i, ".) ", word, " appears: ", dictionary[word], " times", "\n")
    i += 1
    
    # Uncomment this code to create a top 50 list (or change to any number)
    # if not limited, the number of words makes it difficult to read
    if i == 150:
      break
      
      
# Run program here - prints list of all words in descending order

indexDecline = readFile("declineandfall-gut.txt")
indexWealth = readFile("wealthofnations-gut.txt")

print("Decline and Fall of the Roman Empire words: \n")
wordsDecline = sortWords(indexDecline)
printWords(wordsDecline, indexDecline)

print("Wealth of Nation words: \n")
wordsWealth = sortWords(indexWealth)
printWords(wordsWealth, indexWealth)
