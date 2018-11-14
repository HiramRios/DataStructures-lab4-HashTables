'''
Created on Nov 12, 2018

@author: hiramrios

tuesday and thursday 10:30 
the purpose of this lab is to practice hash tables by modifying lab 3
'''


from HashTableNode import HashTableNode
import math
from HashTable import ChainingHashTable





# this method will be used to find the similarities 
def dot(x, y):
    sum = 0
    for i in range(len(x.embeddings)):
        sum += (float(x.embeddings[i]) * float(y.embeddings[i]))
    return sum








# this method will find the magnitude of the word  within the embedding
def Magnitude(n):
    
    sum = 0
    for i in range(len(n.embeddings)):
        sum += (math.pow(float(n.embeddings[i]), 2))
    return math.sqrt(sum)







# this method will find the similarity between the pair of wordds
def similar(x, y):
    if x is None:
        print('x')
        
    if y is None:
        print('y')
        
        
    mg1 = Magnitude(x)
    mg2 = Magnitude(y)
    dot = dot(x, y)
    similar = (dot) / (mg1 * mg2)
    return similar




# this method counts the number of nodes in the hash table
def countNodes (h):
    count =  0
    
    for i in h.table:
        count += len(i)
    return count 



    
# this method gives the number of the longest length of the longest list     
def longestList(h):
    countMax = 0
    
    
    for i in h.table:
        if len(i)> countMax:
            countMax= len(i)
    return countMax




# this method gives the average comparisons 
def comparison(h):
    counter =0
    
    for i in h.table:
        counter += len (i)/2
    return counter  





# this method gives the load factor to the hash table 
def loadFactor(H):
    return countNodes(H)/len(H.table)
  
         






print("Turning tree into a hash table ")




H = ChainingHashTable()
with open("Glove.6b.50d.txt") as textFile:
    for line in textFile:
        array = line.split(' ')
        if array[0][0].isalpha():
            node= HashTableNode(array[0], array[1:])
            H.insert(node)




print("The number of Nodes is " + str(countNodes(H)))
print ("The longest list is " +str(longestList(H)))
print ("The number of average comparisons is " + str(comparison(H)))
print("The Load factor is " + str(loadFactor(H)))





with open("similarities.txt") as textFile:
    for line in textFile:
        words = line.split(' ')
        first= words[0]
        second = words[1].rstrip('\n')
        node1 = H.search(first)
        node2 = H.search(second)
        
    if node1 and node2:
        print(first+ ' ' + second + ' ' + str(similar(node1, node2)))
        










    