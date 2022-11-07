# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:        
    def append(self, val):
        node = ListNode(val)
        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = node
        else:
            self.head = node
    
    def mergeTwoLists(self, list1, list2):
        self.head = None
        while list1 and list2:
            if list1[0] <= list2[0]:
                min_num = list1.pop(0)
            else:
                min_num = list2.pop(0)
            self.append(min_num)
        
        if list1:
            for num in list1:
                self.append(num)
        
        if list2:
            for num in list2:
                self.append(num)
        
        return self.head
    
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

if __name__ == '__main__':
    s = Solution()
    s.mergeTwoLists([1,2,4],[1,3,4])
    s.print_data()