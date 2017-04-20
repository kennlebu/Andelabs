class BinarySearch(list):
    def __init__(self, a, b):
        self.list_length = a
        self.step = b
        self.array_item = b
        self.count = 0
        for counter in range(self.list_length):
            self.append(self.array_item)
            self.array_item += self.step

        self.length = len(self)
            

    def search(self, value):
       low = 0
       high = len(self) - 1
       index = 0
       found = False
       counter = 0
       
       if value == self[low]:
           found = True
           index = low
       elif value == self[high]:
           found = True
           index = high

       # Return index -1 if the value is not on the list
       if value not in self:
           found = True
           index = -1

       # binary search
       while low <= high and not found:
           counter += 1
           middle = (low + high) // 2    # Get the midpoint
           if self[middle] == value:
               found = True
               index = middle
           else:
               if value < self[middle]:
                   high = middle - 1
               else:
                   low = middle + 1
                   
       return {'count': counter, 'index': index}
