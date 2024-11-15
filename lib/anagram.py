# your code goes here!

class Anagram: 
  def  __init__(self, word, words=None):
    self._word = word
    self._words = words if words is not None else []

  def get_word(self): 
    return self._word
  
  def match(self, words):
    sorted_word = sorted(self._word)
    matches = [an for an in words if sorted(an) == sorted_word]
    return matches
