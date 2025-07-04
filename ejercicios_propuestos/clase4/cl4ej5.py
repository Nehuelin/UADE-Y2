# Implemente el algoritmo del código de Huffman, no necesariamente con árboles.


# A Huffman Tree Node 
import heapq 
  
  
class node: 
    def __init__(self, freq, symbol, left=None, right=None):          
        self.freq = freq 
        self.symbol = symbol
        self.left = left 
        self.right = right  
        self.huff = '' 
  
    def __lt__(self, nxt): 
        return self.freq < nxt.freq 

def printNodes(node, val=''): 
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