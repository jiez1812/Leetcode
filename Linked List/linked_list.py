class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class SingleLinkedList:
    def __init__(self):
        self.head = None

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
        node = ListNode(data)
        pointer = self.head
        position -= 1;
        while position != 1:
            pointer = pointer.next
            position -= 1
        node.next = pointer.next
        pointer.next = node

    def append(self, data):
        node = ListNode(data)
        if self.head == None:
            self.head = node
        else:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            
            pointer.next = node
    
    def push(self, data):
        node = ListNode(data)
        if self.head:
            node.next = self.head
        
        self.head = node

if __name__ == '__main__':
    linked_list = SingleLinkedList()
    linked_list.append(45)
    linked_list.append(98)
    linked_list.append(3)
    linked_list.append(67)
    linked_list.print_data()
    
    linked_list.push(53) 
    linked_list.print_data()

    linked_list.insert(76, 3)
    linked_list.print_data()