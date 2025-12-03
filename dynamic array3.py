# Here is a simple Python implementation of a dynamic array
class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.array = [None] * self.capacity

    def resize(self):
        # Double the capacity
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity
        
        # Copy old values
        for i in range(self.size):
            new_array[i] = self.array[i]
        
        self.array = new_array
        self.capacity = new_capacity

    def insert(self, value):
        # If array is full, resize
        if self.size == self.capacity:
            self.resize()
        
        # Insert new value
        self.array[self.size] = value
        self.size += 1

    def __str__(self):
        return str(self.array[:self.size])


# ----- USE THE DYNAMIC ARRAY -----

dyn = DynamicArray()

values = [10, 20, 30, 40, 50]

for v in values:
    dyn.insert(v)
    print(f"Inserted {v} → Array: {dyn.array}, size={dyn.size}, capacity={dyn.capacity}")

print("\nFinal Array:", dyn)
