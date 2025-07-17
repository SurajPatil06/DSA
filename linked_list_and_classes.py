# # basic implimentaion of Linked List

# class linkedListNode:
#     def __init__(self, value, nextNode=None):
#         self.value = value
#         self.nextNode = nextNode


# node1 = linkedListNode("3")
# node2 = linkedListNode("7")
# node3 = linkedListNode("8")
# node4 = linkedListNode("9")

# # 8 -> 7 -> 8 -> 9

# node1.nextNode = node2
# node2.nextNode = node3
# node3.nextNode = node4

# currentNode = node1

# while True:
#     print(currentNode.value, "->", end="")
#     if currentNode.nextNode is None:
#         print("None", end='')
#         break
#     currentNode = currentNode.nextNode

#########################################################################################


# Correct method to create Linked List

class linkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def insert(self, value):
        node = linkedListNode(value)
        if self.head is None:
            self.head = node
            return
        
        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                return
            currentNode = currentNode.nextNode

    def length(self):
        result = 1
        currentNode = self.head
        while True:
            if currentNode.nextNode == None:
                return result
            result += 1
            currentNode = currentNode.nextNode
    
    def get_element(self, position):
        i = 0
        currentNode = self.head
        while True:
            if i == position:
                return currentNode.value
            i += 1
            currentNode = currentNode.nextNode

    def printLinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, " -> ", end='')
            currentNode = currentNode.nextNode
        print("None")
    
ll = LinkedList()
ll.insert("78")
ll.insert("98")
ll.insert("45")
ll.insert("09")

print(ll.length())

print(ll.get_element(1))

ll.printLinkedList()

# Reversing the linked List

def reversee(l):
    if l.head is None:
        return
    
    currentNode = l.head
    prevNode = None
    
    while currentNode is not None:
        nextNode = currentNode.nextNode
        currentNode.nextNode = prevNode

        prevNode = currentNode
        currentNode = nextNode
    l.head = prevNode

reversee(ll)
ll.printLinkedList()