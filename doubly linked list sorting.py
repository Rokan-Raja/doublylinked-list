class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class linkedlist:
    def __init__(self):
        self.head=None
    def push(self,data):
        temp = node(data)
        temp.next=self.head
        if self.head is not None:
            self.head.prev=temp
        self.head=temp
    def sorting(self):
        temp=self.head
        index=None
        if self.head is None:
            return
        if self.head is not None:
            while temp is not None:
                index=temp.next
                while index is not None:
                    if temp.data > index.data:
                        sort=index.data
                        index.data=temp.data
                        temp.data=sort
                    index=index.next
                temp=temp.next
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data,end=",")
            temp=temp.next
llist=linkedlist()
llist.push(5)
llist.push(8)
llist.push(3)
llist.push(4)
print("\nBefore Sorting")
llist.printlist()
print("\nAfter Sorting")
llist.sorting()
llist.printlist()