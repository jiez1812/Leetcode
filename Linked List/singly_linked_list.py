class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class SingleLinkedList:
    def __init__(self, head=None):
        self.head = head

    def count(self):
        count = 0
        if self.head == None:
            return count
        else:
            pointer = self.head
            while pointer:
                count += 1
                pointer = pointer.next
            return count

    def print_data(self):
        if self.head == None:
            print("No Data")
        else:
            print('--- Start Print Nodes ---')
            pointer = self.head
            while pointer:
                print(pointer.val)
                pointer = pointer.next
            print('--- Print Nodes End  ---')
    
    def insert(self, data, position):
        node = Node(data)
        pointer = self.head
        position -= 1;
        while position != 1:
            pointer = pointer.next
            position -= 1
        node.next = pointer.next
        pointer.next = node

    def append(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            
            pointer.next = node
    
    def push(self, data):
        node = Node(data)
        if self.head:
            node.next = self.head
        
        self.head = node

    def pop(self):
        if self.head:
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None
        else:
            print('Linked List is empty.')

    def remove_last(self):
        if self.head:
            pointer = self.head
            while pointer.next.next:
                pointer = pointer.next
            pointer.next = None
        
        else:
            print("Linked List is empty.")

    def find_value(self, value):
        index = 1
        if self.head:
            pointer = self.head
            while pointer:
                if pointer.val == value:
                    return index
                else:
                    pointer = pointer.next
                    index += 1
            return 0
        else:
            return -1
    
    def reset(self):
        self.__init__()

if __name__ == '__main__':
    print('Create Single Link')
    linked_list = SingleLinkedList()

    print('\nAppend digits : 45, 98, 3, 67')
    linked_list.append(45)
    linked_list.append(98)
    linked_list.append(3)
    linked_list.append(67)
    linked_list.print_data()
    
    print('\nPush 53 at the head')
    linked_list.push(53) 
    linked_list.print_data()

    print('\nInsert 76 at position 3')
    linked_list.insert(76, 3)
    linked_list.print_data()

    print('\nPop the first node')
    linked_list.pop()
    linked_list.print_data()

    print('\nRemove the last node')
    linked_list.remove_last()
    linked_list.print_data()

    print('\nFind value 76')
    find_result = linked_list.find_value(76)
    if find_result > 1:
        print('The index is {0}'.format(find_result))
    elif find_result == 0:
        print('Value not found')
    else:
        print('This linked list is empty')

    print('\nFind value 55')
    find_result = linked_list.find_value(55)
    if find_result > 1:
        print('The index is {0}'.format(find_result))
    elif find_result == 0:
        print('Value not found')
    else:
        print('This linked list is empty')

    print('\nReset Linked List')
    linked_list.reset()
    linked_list.print_data()