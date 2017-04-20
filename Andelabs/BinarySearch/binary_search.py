class BinarySearch(list):
    def __init__(self, a, b):
        self.list_length = a
        self.step = b
        self.array_item = b
        self.array = []
        self.count = 0
        for counter in range(self.list_length):
            self.array.append(self.array_item)
            self.array_item += self.step

        self.length = len(self.array)
        self.array = self.sort_array(self.array)
            

    def search(self, value):
        low = self.array[0]
        high = self.array[-1]
        while low <= high:
            self.count += 1
            middle = (low + high) // 2
            if self.array[middle] > value:
                high = middle -1
            elif self.array[middle] < value:
                low = middle + 1
            else: return {'count':self.count, 'index': self.array.index(value)}
        

    def sort_array(self, array):
        """ Sorts and returns the list passed to it """

        for i in range(len(array)-1, 0, -1):
            maxpos = 0
            for position in range(1, i+1):
                if array[position] > array[maxpos]:
                    maxpos = position

            array[i], array[maxpos] = array[maxpos], array[i]

        return array

b = BinarySearch(20, 1)
#print(b[19])
#print(b.search(5))
