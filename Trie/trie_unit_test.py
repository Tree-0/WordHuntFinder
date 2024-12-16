from trie import Trie

## Test Add
def test_add_word():
    trie = Trie()

    assert trie.add_word("apple")
    
    assert trie.letter_count == 5
    assert trie.word_count == 1

    trie.print_tree()

def test_add_word_overlap():
    trie = Trie()

    assert trie.letter_count == 0
    assert trie.word_count == 0

    assert trie.add_word('banana')
    assert trie.add_word('bat')
    assert trie.add_word('batmobile')
    assert trie.add_word('bandana')

    assert trie.letter_count == 17
    assert trie.word_count == 4

    trie.print_tree()

def test_add_same_word():
    trie = Trie()

    assert trie.add_word('apple')
    assert not trie.add_word('apple')
    assert trie.add_word('at')

    assert trie.letter_count == 6
    assert trie.word_count == 2

    trie.print_tree()

## Test Contains
def test_contains_word():
    trie = Trie()
    
    assert trie.add_word('apple')
    trie.print_tree()

    assert trie.contains_word('apple')
    assert not trie.contains_word('app')
    assert not trie.contains_word('batman')

    assert trie.letter_count == 5
    assert trie.word_count == 1

def test_contains_words():
    trie = Trie()

    assert trie.add_word('app')
    assert trie.add_word('apple')
    assert trie.add_word('applet')
    assert trie.add_word('butter')

    assert trie.contains_word('app')
    assert trie.contains_word('apple')
    assert trie.contains_word('applet')
    assert trie.contains_word('butter')
    
    assert not trie.contains_word('butt')
    assert not trie.contains_word('apt')

def test_contains_any_words():
    trie = Trie()

    assert not trie.contains_any_word()
    assert trie.add_word('app')
    assert trie.contains_word('app')
    assert trie.contains_any_word()

## Test Remove

def test_remove_from_empty():
    trie = Trie()

    trie.add_word('apple')
    assert trie.contains_word('apple')
    assert trie.word_count == 1
    assert trie.letter_count == 5
    trie.print_tree()
    
    assert trie.remove_word('apple')
    assert trie.word_count == 0
    assert trie.letter_count == 0
    trie.print_tree()
    
def test_remove_nonexistent_word():
    """Test removing a word that doesn't exist in the trie."""
    trie = Trie()

    assert not trie.remove_word('ghost')  # Word doesn't exist
    assert trie.word_count == 0
    assert trie.letter_count == 0

def test_remove_partial_word():
    """Test removing a partial word (prefix) that doesn't exist as a full word."""
    trie = Trie()

    trie.add_word('apple')
    assert not trie.remove_word('app')  # 'app' is a prefix, not a word
    assert trie.contains_word('apple')  # 'apple' should still exist
    assert trie.word_count == 1
    assert trie.letter_count == 5

def test_remove_word_with_shared_prefix():
    """Test removing a word that shares a prefix with others."""
    trie = Trie()

    trie.add_word('cat')
    trie.add_word('caterpillar')

    assert trie.remove_word('cat')  # Remove 'cat', but 'caterpillar' should remain
    assert not trie.contains_word('cat')
    assert trie.contains_word('caterpillar')
    assert trie.word_count == 1
    assert trie.letter_count == 11  # Letters of 'caterpillar'

def test_remove_word_causing_cleanup():
    """Test removing a word that causes cleanup of unused nodes."""
    trie = Trie()

    trie.add_word('bat')
    trie.add_word('batmobile')

    assert trie.remove_word('bat')  # 'bat' removal should not affect 'batmobile'
    assert not trie.contains_word('bat')
    assert trie.contains_word('batmobile')
    assert trie.word_count == 1
    assert trie.letter_count == 9  # Only 'batmobile' remains

def test_remove_only_word():
    """Test removing the only word in the trie."""
    trie = Trie()

    trie.add_word('unique')

    assert trie.remove_word('unique')  # Remove the only word
    assert not trie.contains_word('unique')
    assert trie.word_count == 0
    assert trie.letter_count == 0
    assert not trie.contains_any_word()  # Trie should now be empty

def test_remove_longer_word_preserves_shorter():
    """Test removing a longer word while preserving a shorter prefix."""
    trie = Trie()

    trie.add_word('at')
    trie.add_word('atlas')
    trie.print_tree()

    assert trie.remove_word('atlas')  # Remove 'atlas', but keep 'at'
    assert not trie.contains_word('atlas')
    assert trie.contains_word('at')
    assert trie.word_count == 1
    assert trie.letter_count == 2  # Only 'at' remains
    trie.print_tree()

def test_remove_word_with_multiple_paths():
    """Test removing a word that is part of a branching structure."""
    trie = Trie()

    trie.add_word('tree')
    trie.add_word('trie')
    trie.add_word('trick')

    assert trie.remove_word('tree')  # Remove 'tree', but keep others
    assert not trie.contains_word('tree')
    assert trie.contains_word('trie')
    assert trie.contains_word('trick')
    assert trie.word_count == 2
    assert trie.letter_count == 6  # Letters of 'trie' and 'trick'

def test_remove_and_readd():
    """Test removing a word and then adding it back."""
    trie = Trie()

    trie.add_word('cycle')

    assert trie.remove_word('cycle')  # Remove 'cycle'
    assert not trie.contains_word('cycle')

    trie.add_word('cycle')  # Add it back
    assert trie.contains_word('cycle')
    assert trie.word_count == 1
    assert trie.letter_count == 5
