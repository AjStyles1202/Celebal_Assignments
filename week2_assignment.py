class Node:
    def __init__(self,value):
        self.value =value
        self.next = None


class IndexErrorException(Exception):
    def __init__(self, k, msg="k is greater than the length of LinkedList."):
        self.k = k
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.k} -> {self.msg}'
    
class EmptyListException(Exception):
    def __init__(self, msg="List is empty"):
        
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.msg}'    
   
class LinkedList:
    head = None

    def printLinkedList(self):
        temp = self.head
        while temp!= None:
            print(temp, end="->")
            temp = temp.next
        print(" ")

    def insertionAtTail(self,value):
        if self.head == None:
            self.head = Node(value)
            return self.head 
                   
        temp = self.head
        while temp.next!= None:
            temp = temp.next

        temp.next = Node(value)

    def DeleteNode(self, k):
        if self.head is None:
            raise EmptyListException()

        if k == 1:
            self.head = self.head.next
            return

        count = 2
        temp = self.head

        while count < k and temp.next is not None:
            temp = temp.next
            count += 1

        if temp.next is None:
            raise IndexErrorException(k)

        temp.next = temp.next.next

if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.insertionAtTail(1)
    linkedList.insertionAtTail(2)
    linkedList.insertionAtTail(8)
    linkedList.insertionAtTail(6)
    linkedList.insertionAtTail(10)

    linkedList.printLinkedList()

    linkedList.DeleteNode(3)

    linkedList.printLinkedList()
