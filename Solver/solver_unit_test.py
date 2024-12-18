from solver import Solver
from Trie.trie import Trie
import time
import pytest
from contextlib import redirect_stdout

def test_init():
    letters = 'abcdefghijklmnop'
    solver = Solver(letters, 'wordhunt', 4)
    
    small_solver = Solver('cateptrsa', 'wordhunt', 3)

    assert solver.board == [
        ['A', 'B', 'C', 'D'],
        ['E', 'F', 'G', 'H'],
        ['I', 'J', 'K', 'L'],
        ['M', 'N', 'O', 'P']
    ]

    assert small_solver.board == [
        ['C', 'A', 'T'],
        ['E', 'P', 'T'],
        ['R', 'S', 'A']
    ]

    with pytest.raises(ValueError):
        # letter -- board_size mismatch
        anagram_solver = Solver(letters, 'anagrams', 5)

        # invalid gamemode
        bad_solver = Solver(letters, 'bleep blorp', 4)

def test_word_hunt_small_board():
    small_solver = Solver('cateptrsa', 'wordhunt', 3)

    now = time.time()

    valid_words = Trie()
    valid_words.deserialize_from_file('trie_data.json', format='json')
    
    then = time.time()

    print(f'deserialization took {int(then-now)} seconds.')
    print(f'dictionary size: {valid_words.word_count} words, {valid_words.letter_count} letters.')

    now = time.time()
    with open('wordhunt_small.txt', 'w') as file:
        with redirect_stdout(file):
            found_words = small_solver.solve_word_hunt(valid_words)

    then = time.time()

    print(f'solving board took {int(then-now)} seconds.')

    assert len(found_words) > 0
    print(f'{len(found_words)} words found.')

def test_word_hunt_medium_board():
    solver = Solver('neseyxtrtebaiddn', 'wordhunt', 4)

    now = time.time()

    valid_words = Trie()
    valid_words.deserialize_from_file('trie_data.pickle', format='pickle')
    
    then = time.time()

    print(f'deserialization took {int(then-now)} seconds.')
    print(f'dictionary size: {valid_words.word_count} words, {valid_words.letter_count} letters.')

    now = time.time()
    with open('wordhunt_medium.txt', 'w') as file:
        with redirect_stdout(file):
            found_words = solver.solve_word_hunt(valid_words)

    then = time.time()

    print(f'solving board took {int(then-now)} seconds.')

    assert len(found_words) > 0
    print(f'{len(found_words)} words found.')

def test_word_hunt_large_board():
    large_solver = Solver('crxteeabdsetnaydrbwtstbud', 'wordhunt', 5)
    
    now = time.time()

    valid_words = Trie()
    valid_words.deserialize_from_file('trie_data.pickle', format='pickle')

    then = time.time()
    print(f'deserialization took {int(then-now)} seconds.')
    now = time.time()

    with open('wordhunt_large.txt', 'w') as file:
        with redirect_stdout(file):
            found_words = large_solver.solve_word_hunt(valid_words)

    then = time.time()

    print(f'solving board took {int(then-now)} seconds.')

    assert len(found_words) > 0
    print(f'{len(found_words)} words found.')

    sorted_words = sorted(list(found_words), key=lambda x: len(x), reverse=True)

    print(f'10 longest words: {sorted_words[:10]}')

def test_anagrams_small():
    small_solver = Solver('seats', 'anagrams', 5)
    
    now = time.time()

    valid_words = Trie()
    valid_words.deserialize_from_file('trie_data.pickle', format='pickle')

    then = time.time()
    print(f'deserialization took {int(then-now)} seconds.')
    now = time.time()

    with open('anagrams_small.txt', 'w') as file:
        with redirect_stdout(file):
            found_words = small_solver.solve_anagrams(valid_words)

    then = time.time()

    print(f'solving anagrams took {int(then-now)} seconds.')

    assert len(found_words) > 0
    print(f'{len(found_words)} words found.')

def test_anagrams_medium():
    medium_solver = Solver('seated', 'anagrams', 6)

    valid_words = Trie()
    valid_words.deserialize_from_file('trie_data.json', format='json')

    with open('anagrams_medium.txt', 'w') as file:
        with redirect_stdout(file):
            found_words = medium_solver.solve_anagrams(valid_words)

    assert len(found_words) > 0
    print(f'{len(found_words)} words found.')