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
        self = self.sort_array(self)
            

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

       # Return -1 as index if the value doesnt exist in the list
       if value not in self:
           found = True
           index = -1
           
       # binary search for the item
       while low <= high and not found:
           counter += 1 # Register an iteration
           middle = (low + high) //    # Get the midpoint
           if self[middle] == value:
               found = True
               index = middle
           else:
               if value < self[middle]:
                   high = middle - 1
               else:
                   low = middle + 1
                   
       return {'count': counter, 'index': index}
        

    def sort_array(self, array):
        """ Sorts and returns the list passed to it """

        for i in range(len(array)-1, 0, -1):
            maxpos = 0
            for position in range(1, i+1):
                if array[position] > array[maxpos]:
                    maxpos = position

            array[i], array[maxpos] = array[maxpos], array[i]

        return array

b = BinarySearch(20, 2)
#print(b[16])
print(b.search(40))
#print(b)
