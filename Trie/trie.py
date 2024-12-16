from node import Node
import pickle
import json

class Trie:
    
    def __init__(self):
        self.head = Node()
        self.letter_count = 0
        self.word_count = 0
    

    def add_word(self, word:str) -> bool:
        '''
            Add the given word to the trie. True if successful,
            False if the word already existed.
        '''
        if not self.head or not word:
            return False

        # go through trie
        def traverse(i, node):
            let = word[i]   
            #print("letter:", let, i)

            # if letter not in trie, add it
            if let not in node.children:
                new_node = Node(value=let, parent=node)
                node.add_child(let, new_node)
                self.letter_count += 1
            
            # traverse to new node    
            next_node = node.children[let]

            # at last letter, check if already added
            if i == len(word)-1:
                # word already existed
                if next_node.end_of_word: 
                    return False

                # word was added
                next_node.end_of_word = True
                self.word_count += 1
                return True

            # finish adding rest of word
            return traverse(i+1, next_node)
        
        return traverse(0, self.head)
        

    def contains_word(self, word:str) -> bool:
        '''
            Check if the trie contains the given word.
        '''
        if not self.head or not word:
            return False

        # go through trie
        def traverse(i, node):
            let = word[i]
            #print("letter:", let, i)

            # if letter not in trie, return false
            if let not in node.children: return False
            
            # next letter exists
            next_node = node.children[let]

            # if end of word is reached, check end_of_word
            if i == len(word)-1:
                return next_node.end_of_word

            # traverse to next letter node
            return traverse(i+1, next_node)
        
        return traverse(0, self.head)


    def contains_any_word(self, node=None) -> bool:
        '''
            Check if any word is stored in the
            given node or its children. By default, checks 
            the whole tree.
        '''

        if node is None:
            node = self.head
        
        def traverse(node):
            if node is None: return False
            if node.end_of_word: return True

            for child in node.children.values():
                if traverse(child): return True
            
            return False

        return traverse(node)


    def count_nodes(self, node=None) -> int:
        '''
            count the number of nodes in a subtree.
            Probably inefficient to use this helper function, 
            but it's a stand-in for now.
        '''
        if node is None:
            node=self.head

        count = 0
        def traverse(node):
            nonlocal count
            if node is not None:
                count += 1
                for child in node.children.values():
                    traverse(node)
        
        traverse(node)
        return count


    def remove_word(self, word:str) -> bool:
        if not self.head or not word:
            return False

        def traverse_and_cleanup(i, node):

            if i == len(word):
                # end of word reached, check if exists 
                if node.end_of_word:
                    node.end_of_word = False # remove word
                    self.word_count -= 1
                else:
                    return False # word does not exist
                
                # if no children (this was the longest word),
                # see if we can shorten this branch of the trie
                if not node.children:
                    while node.parent and not node.children and not node.end_of_word:
                        # sever node
                        del node.parent.children[node.value]
                        self.letter_count -= 1
                        node = node.parent
                return True
            
            # not at end of word, try and traverse
            let = word[i]
            if let not in node.children:
                return False # word does not exist
            
            next_node = node.children[let]
            return traverse_and_cleanup(i+1, next_node)

        return traverse_and_cleanup(0, self.head)
            

    def print_tree(self, level=0) -> None:
        def traverse(node, level):
            if node.end_of_word:
                print(level, '   '*level, f'[{node.value}]')
            else:
                print(level, '   '*level, f' {node.value} ')
            for child in node.children.values():
                traverse(child, level + 1)

        traverse(self.head, level)
    
    # just so I can call print_tree with either name
    def print_trie(self, level=0) -> None:
        self.print_tree(self, level)


    def clear(self) -> None:
        self.head = Node()
        self.letter_count = 0
        self.word_count = 0


    def serialize_to_file(self, filepath, format='pickle'):
        if format == 'pickle':
            with open(filepath, 'wb') as f:
                pickle.dump(self.head, f)
        elif format == 'json':
            with open(filepath, 'w') as f:
                json.dump(self._to_dict(self.head), f)
        else:
            raise ValueError("Unsupported format. Use 'pickle' or 'json'.")

    def deserialize_from_file(self, filepath, format='pickle'):
        if format == 'pickle':
            with open(filepath, 'rb') as f:
                self.head = pickle.load(f)
        elif format == 'json':
            with open(filepath, 'r') as f:
                self.head = self._from_dict(json.load(f))
        else:
            raise ValueError("Unsupported format. Use 'pickle' or 'json'.")    
        
    def _to_dict(self, node):
        return {
            'value': node.value,
            'end_of_word': node.end_of_word,
            'children': {k: self._to_dict(v) for k, v in node.children.items()},
        }

    def _from_dict(self, data):
        node = Node(data['value'], data['end_of_word'])
        node.children = {k: self._from_dict(v) for k, v in data['children'].items()}
        return node