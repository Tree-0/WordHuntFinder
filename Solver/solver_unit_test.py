from solver import Solver
import pytest

def test_init():
    letters = 'abcdefghijklmnop'
    solver = Solver(letters, 'wordhunt', 4)

    assert solver.board == [
        ['a', 'b', 'c', 'd'],
        ['e', 'f', 'g', 'h'],
        ['i', 'j', 'k', 'l'],
        ['m', 'n', 'o', 'p']
    ]

    with pytest.raises(ValueError):
        # letter -- board_size mismatch
        anagram_solver = Solver(letters, 'anagrams', 5)

        # invalid gamemode
        bad_solver = Solver(letters, 'bleep blorp', 4)