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
            pointer = self.head
            while pointer:
                print(pointer.val)
                pointer = pointer.next

    def append(self, data):
        node = ListNode(data)
        if self.head == None:
            self.head = node
        else:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            
            pointer.next = node

if __name__ == '__main__':
    linked_list = SingleLinkedList()
    linked_list.append(45)
    linked_list.append(98)
    linked_list.append(3)
    print(linked_list.count())
    linked_list.print_data()