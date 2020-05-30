"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
import sys
sys.path.append('../myQueue')
sys.path.append('../stack')
# print(sys.path)
from stack import Stack
from myQueue import Queue

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

     
    def insert(self, value):
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                new_node = BSTNode(value)
                self.right = new_node
        else:
            if self.left:
                self.left.insert(value)
            else:
                new_node = BSTNode(value)
                self.left = new_node

   
    def contains(self, target):
        if self.value == target:
            return True
        
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        
        else:
            return self.left.contains(target) if self.left else False

 
    def get_max(self):
        max = self.value
        if self.right:
            return self.right.get_max()
        else:
            return max


     
    def for_each(self, fn):
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self.left)

        print(node.value)
        
        if self.right:
            self.right.in_order_print(self.right)
            
     
    def bft_print(self, node):
            
        newQueue = Queue()
        newQueue.enqueue(node)

        while newQueue:
            node = newQueue.dequeue()
            print(node.value)
            if node.left:
                newQueue.enqueue(node.left)
            if node.right:
                newQueue.enqueue(node.right)


     
    def dft_print(self, node):
        myStack = Stack()
        myStack.push(node)

        while myStack:
            node = myStack.pop()
            if node.right:
                myStack.push(node.right)
            if node.left:
                myStack.push(node.left)
            print(node.value)

     
    def pre_order_dft(self, node):
        pass

     
    def post_order_dft(self, node):
        pass