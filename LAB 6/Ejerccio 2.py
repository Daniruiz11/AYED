####Binary Search Tree : Lowest Common Ancestor


class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
  while root:
      if root.info < v1 and root.info < v2: # Si el valor del nodo actual es menor que v1 y v2, el LCA debe estar en el subárbol derecho.
      root = root.right
      elif root.info > v1 and root.info > v2:# Si el valor del nodo actual es mayor que v1 y v2, el LCA debe estar en el subárbol izquierdo.
      root = root.left
      else: # Si el valor del nodo actual está entre v1 y v2, el nodo actual es el LCA.
      return root
  return None # Si el bucle termina y el nodo actual es None, no se ha encontrado el LCA.



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)

##By:DaniRuiz11_
