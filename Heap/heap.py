class Heap:
    def __init__(self):
        self.heap = list()
        self.size = 0

    def extract_max(self):
        extract_num = self.heap.pop(0)
        self.heap[0] = self.heap.pop(-1)
        self.size -= 1
        self.max_heapify(0)
        return extract_num
    
    def parent_index(self, child_idx:int):
        if child_idx > 0:
            return (child_idx - 1)//2
        return None

    def left_child_index(self, parent_idx:int):
        left_child_idx = parent_idx * 2 + 1
        if left_child_idx < self.size:
            return left_child_idx
        return None

    def right_child_index(self, parent_idx:int):
        right_child_idx = parent_idx * 2 + 2
        if right_child_idx < self.size:
            return right_child_idx
        return None
    
    def max_heapify(self, index):
        if index < self.size:
            violation = index
            left_child = self.left_child_index(index)
            right_child = self.right_child_index(index)

            if left_child != None and self.heap[left_child] > self.heap[violation]:
                self.heap[violation], self.heap[left_child] = self.heap[left_child], self.heap[violation]
            if right_child != None and self.heap[right_child] > self.heap[violation]:
                self.heap[violation], self.heap[right_child] = self.heap[right_child], self.heap[violation]
            
            if violation != index:
                self.heap[violation], self.heap[index] = self.heap[index], self.heap[violation]
                self.max_heapify(violation)
    
    def build_max_heap(self, numbers:list):
        self.heap = numbers
        self.size = len(self.heap)
        if self.size > 1:
            for i in range(self.size//2 - 1, -1, -1):
                self.max_heapify(i)

if __name__ == '__main__':
    hp = Heap()
    hp.build_max_heap([4,6,2,7,9,17,15,13])
    print(hp.heap)
    hp.extract_max()
    print(hp.heap)
