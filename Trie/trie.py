from node import Node

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
    
        def traverse(i, node):
            let = word[i]
            #print("letter:", let, i)

            # word can't be in tree
            if let not in node.children: return False

            next_node = node.children[let]
            
            # check end of the word we are trying to remove
            if i == len(word)-1:
                if next_node.end_of_word: 
                    # remove the word
                    next_node.end_of_word = False 
                    self.word_count -= 1

                    # if there is still a word stored within this subtree, we're done
                    if self.contains_any_word(next_node):
                        return True
                    
                    # otherwise, no words need this tree
                    else:
                        # traverse up the parents to remove as many letters as possible
                        while next_node and next_node.parent:

                            # if this node is not the end of a word, or used for a longer word
                            if not (self.contains_any_word(next_node) or next_node.end_of_word):
                                # sever this node
                                next_node.parent.remove_child(next_node.value)
                                
                                # how big is the subtree we are severing?
                                self.letter_count -= self.count_nodes(next_node)

                                next_node = next_node.parent
                            else: break
                        
                        # success
                        return True
                else:
                    # word did not exist, failed removal
                    return False
                
            return traverse(i+1, next_node)
        
        return traverse(0, self.head)

    # visualize that thang
    def print_tree(self, level=0) -> None:
        def traverse(node, level):
            if node.end_of_word:
                print(level, '   '*level, f'[{node.value}]')
            else:
                print(level, '   '*level, f' {node.value} ')
            for child in node.children.values():
                traverse(child, level + 1)

        traverse(self.head, level)
    
    # idk I just wanted to be able to call it by both names
    def print_trie(self, level=0) -> None:
        self.print_tree(self, level)


    def clear(self):
        self.head = Node()
        self.letter_count = 0
        self.word_count = 0