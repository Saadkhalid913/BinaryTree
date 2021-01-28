class Node(object):
   
   def __init__(self, Data=None):
        self.data = Data
        self.greater = None
        self.lesser = None 

    
class Tree(object):
    
    def __init__(self):
        self.root = None
        self.height =0 

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(data, self.root) 

    def _insert(self, data, current):
        
        if data > current.data:
            if current.greater == None:
                current.greater = Node(data)
            else:
                self._insert(data, current.greater)
        
        elif data < current.data:
            if current.lesser == None:
                current.lesser = Node(data)
            else:
                self._insert(data, current.lesser)
        
        else:
            pass

        
    def search(self,data):
        
        if self.root.data == data:
            return True
        else:
            return self._search(data, self.root)

    def _search(self, data, current):

        if data > current.data and current.greater !=None:
            return self._search(data, current.greater)

        elif data < current.data and current.lesser !=None:
            return self._search(data, current.lesser)

        elif data == current.data:
            return True 

        elif current.greater == None and current.lesser == None:
            return False


    def post_order_traverse(self, root):
        print(root.data)

        if root.lesser !=None:
            self.post_order_traverse(root.lesser)
        
        if root.greater != None:
            self.post_order_traverse(root.greater)
    
    def _tree_height(self, cur):
        if cur is None:
            return 0
        else:
            height = max(self._tree_height(cur.lesser), self._tree_height(cur.greater) ) +1
        return height 

    def GetHeight(self):
        return self._tree_height(self.root) -1
    
    def _GetHeightNode(self, cur):
        if cur is None:
            return 0
        else:
            height = max(self._GetHeightNode(cur.lesser), self._GetHeightNode(cur.greater) ) +1
        return height 
    
    def NodeHeight(self, node):
        return self._GetHeightNode(node) - 1

    def equals(self, node1, node2):
        if node1 == None or node2 == None:
            pass
        elif node1.data != node2.data:
            return False
        elif (node1.data == node2.data):
            self.equals(node1.lesser, node1.greater)
            self.equals(node2.lesser, node2.greater)
        
        return True





tr = Tree()
for item in range(1, 10):
    tr.insert(item)

tr2 = Tree()
for item in range(1, 10):
    tr2.insert(item)


print(tr.equals(tr.root, tr2.root))


            
