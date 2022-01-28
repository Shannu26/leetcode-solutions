######################################################

#   Solved on Thursday, 29 - 07 - 2021.

######################################################


######################################################

#   Runtime: 128ms   -   98.03%
#   Memory: 21.3MB  -   100.00%

######################################################

import re

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Creating an empty dictionary. The dictionary will have len of words as key
        # and list of words having length = key as value
        # Ex:  { 2 : ['ab', 'bc'], 3 : ['abc', 'acd'] }
        self.words = {}
        

    def addWord(self, word: str) -> None:
        # If len(word) key is not present in the dictionary, we create a new list with
        # that len(word) as key
        if len(word) not in self.words:
            self.words[len(word)] = list()

        # Adding the given word to that len(word) key set
        self.words[len(word)].append(word)

    def search(self, word: str) -> bool:
        # If len(word) key is not present in dictionary, there is no word with that
        # length. So given word also doesn't present. so return False
        if len(word) not in self.words: return False
        
        # If there is no "." in the given word, it is a normal word and so there is 
        # no need to match the words in our dictionary using regular expression 
        # matching. We just need to look whether that word is present in that len(key)
        # list.
        if "." not in word:
            return word in self.words[len(word)]
        
        # If the given word is an regular expression type with "." in it, we loop 
        # through the words in len(word) key and check if that word matches the given
        # regular expression. If yes we return True
        for w in self.words[len(word)]:
            if re.match(word, w): return True
        
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)