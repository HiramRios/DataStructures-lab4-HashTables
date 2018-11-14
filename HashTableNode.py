'''
Created on Nov 12, 2018

@author: hiramrios
'''

#this node class will be used in the method to creak link lists in the array 
class HashTableNode: 
    def __init__(self, item, embedding, next=None):
        self.item = item
        self.embedding = embedding
        self.next = next