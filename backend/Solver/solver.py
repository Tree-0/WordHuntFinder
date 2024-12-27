import sys
import os
from collections import Counter
import math

# Add the parent directory of Solver and Trie to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Trie.trie import Trie

class Solver:

    def __init__(self, letters:str, mode:str):
        self.board = None
        self.board_size = 0
        self.letters = letters.upper()
        self.mode = mode

        if mode == 'wordhunt':
            # check for square matrix
            board_dim = math.sqrt(len(self.letters))
            if board_dim - int(board_dim) != 0:
                raise ValueError('invalid amount of letters given. Must fill square board exactly.')
            
            self.board_size = int(board_dim)

            self.board = [['']*self.board_size for i in range(self.board_size)] 
                
            row = 0
            col = 0
            # fill out board with given letters
            for l in self.letters:
                self.board[row][col] = l
                col += 1
                if col == self.board_size: # wrap to next row
                    row += 1
                    col = 0  

        elif mode == 'anagrams':
            # don't need board, just letters
            self.board = None
            self.board_size == len(letters)
            
        else:
            raise ValueError('mode must be \'anagrams\' or \'wordhunt\'.')
        
    def solve_word_hunt(self, valid_words:Trie) -> set:
        ''' 
        Solve the wordhunt board given to the solver. 
        Takes a trie of accepted words to compare to.
        Valid words must be at least length 3.
        '''

        assert self.mode == 'wordhunt'

        visited = set() # the letters used so far in a word
        found_words = set() # valid words found in board
        
        def find_words(x,y, curr_word, depth):
            if x < 0 or y < 0 or x >= len(self.board) or y >= len(self.board[0]):
                return # out of bounds
            if (x,y) in visited: 
                return # tile already used
            if (depth > self.board_size ** 2):
                return # word is too long to fit on board
            

            if not valid_words.contains_prefix(curr_word):
                # print(f"Invalid prefix: {curr_word}")
                return # there is no word that starts with these letters
            
            # use new tile
            curr_word += self.board[x][y]
            visited.add((x,y))

            #print('string: ', curr_word, 'depth: ', depth)
            if depth >= 3 and valid_words.contains_word(curr_word):
                #print('checking string', curr_word)
                print('valid word:', curr_word)
                found_words.add(curr_word)
    
            find_words(x+1,y, curr_word, depth+1) # down
            find_words(x-1,y, curr_word, depth+1) # up
            find_words(x,y+1, curr_word, depth+1) # right
            find_words(x,y-1, curr_word, depth+1) # left

            find_words(x-1,y-1, curr_word, depth+1) # up-left
            find_words(x+1,y-1, curr_word, depth+1) # down-left
            find_words(x-1,y+1, curr_word, depth+1) # up-right
            find_words(x+1,y+1, curr_word, depth+1) # down-right

            visited.remove((x,y)) # don't want this word to interfere with other recursion

        # permute through every letter in the board
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                visited.clear()
                print(f'({i},{j}) - starting from letter: ', self.board[i][j])
                find_words(i,j,'',depth=1)
        
        return found_words

    def solve_anagrams(self, valid_words:Trie) -> set:
        ''' 
        Solve the anagrams given to the solver. 
        Takes a trie of accepted words to compare to.
        Valid words must be at least length 3.
        '''

        assert self.mode == 'anagrams'

        unused = Counter(self.letters) # the letters to be used in a word
        found_words = set() # valid words found in board

        def permute(curr_word:str, depth:int):
            # print(curr_word)  
            
            if not valid_words.contains_prefix(curr_word):
                # print(f'no valid prefix: ', curr_word)
                return # no possible word could be made

            #print('string: ', curr_word, 'depth: ', depth)
            if depth >= 3 and valid_words.contains_word(curr_word):
                print('valid word:', curr_word)
                found_words.add(curr_word)

            for let in list(unused.keys()):
                # check if any instances of this letter can be used
                if unused[let] > 0:
                    unused[let] -= 1 # use one letter

                    #print(f'removed {let}. Remaining: {unused}')
                    permute(curr_word+let, depth+1)
                    
                    unused[let] += 1 # restore letter for other recursive branches
                    #print(f'added {let}. Remaining: {unused}')

        permute('', 0)
        return found_words

            





