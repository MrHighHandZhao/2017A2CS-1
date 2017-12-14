"""
S3C2 Harr Xue
Linked List, Queue and Stack
"""

class List():  
    def __init__(self):  
        self.head = None  
  
    def getHead(self):  
        return self.head  
  
    def isEmpty(self):  
        return self.head is None  
  
    def add(self, item):  
        node = ListNode(item)  
        node.next = self.head  
        self.head = node     
  
    def size(self):  
        currentNode = self.head  
        count = 0  
        while currentNode is not None:  
            count += 1  
            currentNode = currentNode.getNext()  
  
        return count  
  
    def search(self, item):  
        currentNode = self.head                                                                                                                                                                                                                                     
        found = False  
        while currentNode is not None and not found:  
            if currentNode.getData() == item:  
                found = True  
            else:  
                currentNode = currentNode.getNext()  
        return found  
  
    def append(self, item):  
        node = ListNode(item)  
        if self.isEmpty():  
            self.head = node  
        else:  
            currentNode = self.head  
            while currentNode.getNext() is not None:  
                currentNode = currentNode.getNext()  
            currentNode.setNext(node)  
  
    def remove(self, item):  
        currentNode = self.head  
        previous = None  
        found = False  
        while not found:  
            if currentNode.getData() == item:  
                found = True  
            else:  
                previous = currentNode 
                currentNode = currentNode.getNext()  
  
        if previous is None:  
            self.head = currentNode.getNext()  
        else:  
            previous.setNext(currentNode.getNext())


class QueueNode():  
    def __init__(self, value):  
        self.value = value  
        self.next = None  
  
  
class Queue():  
    def __init__(self):  
        self.front = None  
        self.rear = None  
  
    def is_empty(self):  
        return self.front is None and self.rear is None  
  
    def enqueue(self, num):  
        node = QueueNode(num)  
        if self.is_empty():  
            self.front = node  
            self.rear = node  
        else:  
            self.rear.next = node  
            self.rear = node  
  
    def dequeue(self):  
        if self.front is self.rear:  
            node = self.front  
            self.front = None  
            self.rear = None  
            return node.value  
        else:  
            node = self.front  
            self.front = node.next  
            return node.value

        

class StackNode():    
    def __init__(self, value):  
        self.value = value  
        self.next = None  
  
  

class Stack():  
    def __init__(self, top=None):  
        self.top = top  
      
    def get_top(self):  
        return self.top  
  
    def is_empty(self):  
        return self.top is None  
  
    def pushItem(self, item):  
        if self.is_empty():  
            self.top = StackNode(item)  
            return  
        else:  
            node = StackNode(item)  
            node.next = self.top.next  
            self.top = node  
            return  
  
    def popItem(self):  
        if self.is_empty():  
            print("Empty Stack!\n")  
            return  
        node = self.top  
        self.top = self.top.next  
        return node



