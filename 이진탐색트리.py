class Node:
    def __init__(self,item,left_child=None, right_child=None):
        self.key=item
        self.left=left_child
        self.right=right_child
    def get_key(self): return self.key
    def get_left(self): return self.left
    def get_right(self): return self.right
    def set_key(self,new_item):
        self.key=new_item
    def set_left(self,new_left_child):
        self.left=new_left_child
    def set_right(self,new_right_child):
        self.right=new_right_child

class BST:
    def __init__(self):
        self.root=None
    def search(self,k):
        #finding value k in the tree
        return _search(self.root,k)
    def _search(self,n,k):
        if n==None or n.get_key()==k:
            return n!=None
        elif n.get_key()>k:
            return self._search(n.get_left(),k)
        else:
            '''Finish code'''
            return self._search(n.get_right(),k)
            pass
    def insert(self,key):
        #inserting node with the key 'key' in the tree
        self.root=self._insert(self.root,key)
    def _insert(self,n,key):
        if n==None:
            return Node(key)
        if n.get_key()>key:
            n.set_left(self._insert(n.get_left(),key))
        elif n.get_key()<key:
            '''Finish code'''
            n.set_right(self._insert(n.get_right(),key))
            pass
        return n
    def find_min(self):
        #finding the minimum value of the tree
        if self.root==None:
            return None
        return self._find_min(self.root)
    def _find_min(self,n):
        if n.get_left()==None:
            return n
        return self._find_min(n.get_left())
    def delete_min(self):
        #deleting the minimum value of the tree
        if self.root==None:
            print("Tree is empty")
        self.root=self._delete_min(self.root)
    def _delete_min(self,n):
        if n.get_left()==None:
            return n.get_right()
        n.set_left(self._delete_min(n.get_left()))
        return n
    def delete(self,key):
        #deleting node with key value 'key' in the tree
        self.root=self._delete(self.root,key)
    def _delete(self,n,key):
        #search first. if item found, then delete
        if n==None:
            return None
        if n.get_key()>key:
            n.set_left(self._delete(n.get_left(),key))
        elif n.get_key()<key:
            n.set_right(self._delete(n.get_right(),key))
        else:
            #item found, implement deleting process
            #case 0.
            if n.get_left()==None and n.get_right()==None:
                return None
            #case 1.
            if n.get_left()==None or n.get_right()==None:
                if n.get_left()==None:
                    return n.get_right()
                else:
                    '''Finish code'''
                    return n.get_left()
                    pass
            #case 2.
            target=n #node that needs to be deleted. set as 'target'
            '''Finish code'''
            lf=target.get_left()
            rt=target.get_right()
            if target.get_key()==self.root.get_key():
                self.root.set_key(rt.get_key())
                self.root.set_right(rt.get_right())
            else:
                target.set_key(rt.get_key())
                target.set_right(rt.get_right())
            pass
        return n
    def inorderPrint(self,n):
        #print elements in graph, using 중위순회.
        #중위순회: 왼쪽 자식-루트 노드-오른쪽 자식 순으로 순회하는 것을 의미
        if n!=None:
            if n.get_left():
                self.inorderPrint(n.get_left())
            print(str(n.get_key()),' ',end='')
            if n.get_right():
                self.inorderPrint(n.get_right())


tree=BST()
tree.insert(40)
tree.insert(35)
tree.insert(50)
tree.insert(60)
tree.insert(90)
tree.insert(55)
print(tree.inorderPrint(tree.root))
tree.delete(40)
print(tree.inorderPrint(tree.root))
