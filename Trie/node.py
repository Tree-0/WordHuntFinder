class Node:
            
    def __init__(self, value:str=None, end_of_word:bool=False, children:dict[str, 'Node']=None, parent=None):
        self.value = value # letter stored
        self.end_of_word = end_of_word # indicates end of a stored word
        self.children = children if children is not None else {} # navigate to children by value of node
        self.parent = parent

    def __str__(self):
        return f'val: {self.value}, children: {self.children.keys()}'
    
    def __repr__(self):
        return f"Node(value={self.value}, end_of_word={self.end_of_word}, children={list(self.children.keys())})"
    
    def add_child(self, char: str, node: 'Node'):
        self.children[char] = node
        node.parent = self

    def remove_child(self, char: str):
        if char in self.children:
            del self.children[char]

