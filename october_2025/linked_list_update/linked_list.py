class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data = data, next = self.head)
        self.head = node

    def insert_at_end(self, data):
        node = Node(data = data, next = None)
        if self.head is None:
            self.head = node
            return

        previous_node = self.head
        while previous_node.next != None:
            previous_node = previous_node.next
        previous_node.next = node

    def print_list(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)

    """
    - insert multiple values (overwrite current linkedlist)
    """
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_by_index(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Not valid index")
        
        if index == 0:
            new_head = self.head.next
            self.head.next = None
            self.head = new_head
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_by_index(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Not valid index")
        
        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data = data, itr.next)
                itr.next = node
                break
            
            itr = itr.next
            count += 1



if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(69)
    ll.insert_at_end(100)
    ll.print_list()

    multi = LinkedList()
    multi.insert_values([1,2,3,4,5])
    multi.print_list()
    multi.remove_by_index(1)
    multi.print_list()