class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head == None:
            node = Node(data, None)
            self.head = node
            return

        else:
            itr = self.head

            while itr.next:
                itr = itr.next
            itr.next = Node(data, None)

    def insert_values(self, dataList):
        self.head = None
        for data in dataList:
            self.insert_at_end(data)

    def get_length(self):
        itr = self.head
        counter = 0
        while itr:
            counter += 1
            itr = itr.next

        return counter

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('This is not a valid index')

        if index == 0:
            self.head = self.head.next
            return

        counter = 0
        itr = self.head

        while itr:
            if counter == index - 1:
                itr.next = itr.next.next
            itr = itr.next
            counter += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception('This is not a valid index')

        if index == 0:
            self.insert_at_begining(data)
            return

        counter = 0
        itr = self.head

        while itr:
            if counter == index - 1:
                new_node = Node(data, itr.next)
                itr.next = new_node
                return

            itr = itr.next
            counter += 1

    def printll(self):
        if self.head is None:
            print('The linked list is empty')
            return

        itr = self.head
        llString = ''
        while itr:
            llString += str(itr.data) + '-->'
            itr = itr.next

        print(f'{llString}')


if __name__ == '__main__':
    ll = LinkedList()

    ll.insert_at_begining('A')
    ll.insert_at_begining('G')
    ll.insert_at_end('B')
    ll.insert_values(['a', 'b', 'c'])
    print(f'The length is {ll.get_length()}')
    ll.remove_at(2)
    ll.insert_at(1, 'd')
    ll.insert_at(1, 'e')
    ll.printll()
