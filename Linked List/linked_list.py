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

    def main(self):
        self.head = ListNode(45)
        self.current = ListNode(98)
        self.head.next = self.current

        self.current = ListNode(3)
        self.head.next.next = self.current

if __name__ == '__main__':
    linked_list = SingleLinkedList()
    linked_list.main()
    # print(linked_list.count())
    linked_list.print_data()