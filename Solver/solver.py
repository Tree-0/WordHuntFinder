import sys
import os

# Add the parent directory of Solver and Trie to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Trie.trie import Trie

class Solver:

    def __init__(self, letters:str, mode:str, board_size:int):
        self.board = None
        self.board_size = board_size
        letters = letters.upper()

        if mode == 'wordhunt':
            # square matrix
            self.board = [['']*board_size for i in range(board_size)] 
            if not len(letters) == board_size ** 2:
                raise ValueError('invalid amount of letters given. Must fill square board exactly.')
            
            row = 0
            col = 0
            # fill out board with given letters
            for l in letters:
                self.board[row][col] = l
                col += 1
                if col == board_size: # wrap to next row
                    row += 1
                    col = 0  

        elif mode == 'anagrams':
            # don't need board, just letters
            self.board = None
            if not len(letters) == board_size:
                raise ValueError('invalid amount of letters given. Must match board size.')
            
        else:
            raise ValueError('mode must be \'anagrams\' or \'wordhunt\'.')
        
    def solve_word_hunt(self, valid_words:Trie) -> set:
        ''' 
        Solve the wordhunt board given to the solver. 
        Takes a trie of accepted words to compare to.
        Valid words must be at least length 3.
        '''

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
                nonlocal found_words
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
                print('starting from letter: ', self.board[i][j])
                find_words(i,j,'',depth=1)
        
        return found_words
