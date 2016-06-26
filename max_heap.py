import math

class MaxHeap:

    def __init__(self):
        self.intern_array = []
        
    def size(self):
        return len(self.intern_array)
        
    def insert(self, tuple):
        self.intern_array.append(tuple)
        current_index = len(self.intern_array) - 1
        while self.has_parent(current_index):
            parent_index = self.get_parent_index(current_index)
            if self.intern_array[current_index][1] > self.intern_array[parent_index][1]:
                self.swap(current_index, parent_index)
                current_index = parent_index
            else:
                break
                
    def insert_list(self, tuple_list):
        for tuple in tuple_list:
            self.insert(tuple)
    
    def extract(self):
        if len(self.intern_array) == 0:
            return None
        
        ret_element = self.intern_array[0]
        self.intern_array[0] = self.intern_array[len(self.intern_array) - 1]
        self.intern_array = self.intern_array[:-1]
        
        current_index = 0
        while self.has_children(current_index):
            child_index = self.get_largest_child_index(current_index)
            if (self.intern_array[child_index][1] > self.intern_array[current_index][1]):
                self.swap(current_index, child_index)
                current_index = child_index
            else:
                break
                
        return ret_element
    
    def has_parent(self, index):
        return index > 0
        
    def get_parent_index(self, index):
        return math.ceil(index / 2) - 1
        
    def swap(self, index1, index2):
        tmp = self.intern_array[index1]
        self.intern_array[index1] = self.intern_array[index2]
        self.intern_array[index2] = tmp
        
    def has_children(self, index):
        return len(self.intern_array) > index * 2 + 1
        
    def get_largest_child_index(self, parent_index):
        first_child_index = parent_index * 2 + 1
        second_child_index = first_child_index + 1
        
        if len(self.intern_array) > second_child_index and self.intern_array[second_child_index][1] > self.intern_array[first_child_index][1]:
            return second_child_index
        else:
            return first_child_index