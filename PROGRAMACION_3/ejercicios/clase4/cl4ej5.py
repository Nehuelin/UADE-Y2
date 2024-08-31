# Implemente el algoritmo del código de Huffman, no necesariamente con árboles.


# A Huffman Tree Node 
import heapq 
  
  
class node: 
    def __init__(self, freq, symbol, left=None, right=None): 
        # frequency of symbol 
        self.freq = freq 
  
        # symbol name (character) 
        self.symbol = symbol 
  
        # node left of current node 
        self.left = left 
  
        # node right of current node 
        self.right = right 
  
        # tree direction (0/1) 
        self.huff = '' 
  
    def __lt__(self, nxt): 
        return self.freq < nxt.freq 
  
  
# utility function to print huffman 
# codes for all symbols in the newly created Huffman tree 
def printNodes(node, val=''): 
  
    # huffman code for current node 
    new_val = val + str(node.huff) 
  
    if(node.left): 
        printNodes(node.left, new_val) 
    if(node.right): 
        printNodes(node.right, new_val) 
    if(not node.left and not node.right): 
        print(f"{node.symbol} -> {new_val}") 

chars = ['a', 'b', 'c', 'd', 'e', 'f'] 

freq = [5, 9, 12, 13, 16, 45] 

nodes = [] 
   
for x in range(len(chars)): 
    heapq.heappush(nodes, node(freq[x], chars[x])) 
  
while len(nodes) > 1:  
    left = heapq.heappop(nodes) 
    right = heapq.heappop(nodes) 

    left.huff = 0
    right.huff = 1
    
    new_node = node(left.freq+right.freq, left.symbol+right.symbol, left, right) 
    
    heapq.heappush(nodes, new_node) 

printNodes(nodes[0]) 