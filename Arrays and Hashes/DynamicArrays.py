class DynamicArray:
    def __init__(self):
        self.capacity = 3
        self.length = 0
        self.arr = [0] * self.capacity
    
    def insert(self, n):
        if self.length == self.capacity:
            self.resize()

        self.arr[self.length] = n
        self.length += 1

    def resize(self):
        self.capacity *= 2
        newArr = [0] * self.capacity

        for i in range(self.length):
            newArr[i] = self.arr[i]
        self.arr = newArr

    def pop(self):
        if self.length > 0:
            self.length -= 1
    
    def get(self, i):
        if i <= self.length:
            print(self.arr[i])

    def insertt(self, i, n):
        if i > self.length:
            return  # Invalid insert
        if self.length == self.capacity:
            self.resize()
        for j in range(self.length, i, -1):
            self.arr[j] = self.arr[j - 1]  # Shift right
        self.arr[i] = n
        self.length += 1

    def print(self):
        for i in range(self.length):
            if i == 0:
                print("[",end='')
            print(f"{self.arr[i]}" +",", end="")
            if i == self.length-1:
                print("]",end="")
        print()


new = DynamicArray()
new.insert(77)
new.insertt(0,55)
new.get(0)
new.print()