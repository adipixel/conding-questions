"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
        1001011
"""        

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root , s):
    code = s
    c = 0
    node = root
    result = ""
    while c < len(code):
        
        if code[c] == '0':
            node = node.left
        else:
            node = node.right
        
        if node.data == '\0':
            pass
        else:
            result += node.data
            node = root
        
        c += 1
    
    print result
