class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self.index = 0

    def __iter__(self):
        return self  # returning an object with __next__ method

    def __next__(self):
        if self.index == 0:
            self.index += 1
            return {'length': self.length}
        elif self.index == 1:
            self.index += 1
            return {'width': self.width}
        else:
            raise StopIteration

# Example usage
rect = Rectangle(10, 50)
for side in rect:
    print(side)
