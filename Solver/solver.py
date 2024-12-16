class Solver:

    def __init__(self, letters:str, mode:str, board_size:int):
        self.board = None

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
        

