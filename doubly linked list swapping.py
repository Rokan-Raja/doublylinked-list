class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class linkedlist:
    def __init__(self):
        self.head=None
    def push(self,data):
        temp=node(data)
        temp.next=self.head
        if self.head is not None:
            self.head.prev=temp
        self.head=temp
    def swap(self, n1, n2):
        prevNode1 = None
        prevNode2 = None
        node1 = self.head
        node2 = self.head
        if (self.head == None):
            return
        if (n1 == n2):
            return
        while (node1 != None and node1.data != n1):
            prevNode1 = node1
            node1 = node1.next
        while (node2 != None and node2.data != n2):
            prevNode2 = node2
            node2 = node2.next
        if (node1 != None and node2 != None):
            if (prevNode1 != None):
                prevNode1.next = node2
            else:
                self.head = node2
            if (prevNode2 != None):
                prevNode2.next = node1
            else:
                self.head = node1
            temp = node1.next
            node1.next = node2.next
            node2.next = temp
        else:
            print("Swapping is not possible")
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data,end=",")
            temp=temp.next

llist=linkedlist()
llist.push(5)
llist.push(6)
llist.push(3)
llist.push(8)
print("\nBefore Swapping")
llist.printlist()
print("\n After Swapping")
llist.swap(8,6)
llist.printlist()