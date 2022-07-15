# Module pwalgorithms
import time

# get words from password dictionary file
def get_dictionary():
  words = []
  dictionary_file = open("dictionary.txt")
  for line in dictionary_file:
    # store word, omitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
  return words

# analyze a one-word password
def one_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    guesses += 1
    if (w == password):
      return True, guesses
  return False, guesses

def combine_words(password):
  #password = input("What is your passphrase? ")
  words = get_dictionary()
  two_words = []
  guesses = 0
  for w in words:
    for x in words:
      textfile = open("two_words.txt", "w")
      guesses += 1
      passphrase = w + x
      two_words.append(passphrase)
      for element in two_words:
        textfile.write(element + "\n")
      print(two_words)

      if passphrase == password:
        return True, guesses
    return False, guesses





  

