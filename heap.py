
class Heap:
    def __init__(self, comparison_function, init_array):
        self.arr = init_array
        self.comparison_function = comparison_function
        n = len(init_array)
        for i in range((n-1)//2, 0, -1):
            self.heapify(self.arr, i, n)
    
        
    def insert(self, value):
        if len(self.arr) == 0:
            self.arr.append(value)
            return 

        self.arr.append(value)
        n = len(self.arr)
        index = n - 1
        
        while index > 0:
            parent = (index - 1)//2
            if self.comparison_function(self.arr[index], self.arr[parent]):
                self.arr[index], self.arr[parent] = self.arr[parent], self.arr[index]
                index = parent
            else:
                return
        pass

    def extract(self):
        n = len(self.arr)
        if n <= 0:
            return
        
        self.arr[n-1], self.arr[0] =  self.arr[0] , self.arr[n-1]
        ans = self.arr.pop()
        self.heapify(self.arr, 0, len(self.arr))
        return ans
        pass
    
    def top(self):
        if self.arr:
            return self.arr[0]
        pass

    def heapify(self, arr, i, size):
        if size == 0 or size == 1:
            return
        largest = i
        left = i*2 + 1
        right = i*2 + 2
        if left < size and self.comparison_function(arr[left], arr[largest]):
            largest = left
        if right < size and self.comparison_function(arr[right], arr[largest]):
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, largest, size)
    def empty(self):
        return len(self.arr) == 0