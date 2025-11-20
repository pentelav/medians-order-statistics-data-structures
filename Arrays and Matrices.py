# Declares an array class that is used to provide the option of insertion, deletion, and access.
# A nested list is used to illustrate simple row-and-column access of matrix.

# Defining an array class with basic operations
class Array:
    def __init__(self):
        self.data = []  # Initializing an empty array

    # Inserting element at the end of the array
    def insert(self, value):
        self.data.append(value)  # Appending element to the array

    # Deleting element by value
    def delete(self, value):
        if value in self.data:
            self.data.remove(value)  # Removing first occurrence of value

    # Accessing element by index
    def access(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]  # Returning element at given index
        return None

# Example usage
arr = Array()
arr.insert(10)  # Adding element
arr.insert(20)
arr.insert(30)
print("Access index 1:", arr.access(1))  # Accessing second element
arr.delete(20)  # Deleting element 20
print("Array after deletion:", arr.data)  # Displaying array

# Matrix implemented as a nested list
matrix = [[1,2,3],[4,5,6],[7,8,9]]  # Initializing 3x3 matrix
print("Matrix element [1][2]:", matrix[1][2])  # Accessing element at row 1, column 2
