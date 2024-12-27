''' 
Create the trie of all ~200k valid words from the Collins_Scrabble_Words.txt file
and serialize it for future use.

Post: ~1 second to read file, ~8 seconds to serialize both methods
'''
 
from .trie import Trie
from .node import Node
import time

all_words = Trie()

now = time.time()

with open('Collins_Scrabble_Words.txt', 'r') as file:
    for line in file:
        all_words.add_word(line.strip())

then = time.time()
seconds = int(then - now)
print(f'trie created from file in {seconds} seconds.')

now = time.time()
all_words.serialize_to_file('trie_data.pickle', format='pickle')
all_words.serialize_to_file('trie_data.json', format='json')
then = time.time()
seconds = int(then - now)
print(f'trie serialized to pickle and json in {seconds} seconds.')
