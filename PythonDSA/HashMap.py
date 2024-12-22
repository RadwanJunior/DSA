# Implement a Node class to be used for linked list implementation for each hashmap key
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    # The  ‘__init__‘ method initializes the hash table with a given capacity. It sets the ‘capacity‘ and ‘size‘ variables and initializes the array to ‘None’.
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity # Output: a list -> [None, None, None, None, None...]
    
    def _hash(self, key):
        # returns where the key should be stored in the list based on the built-in hash value % the capacity of the list (hashmap keys)
        return hash(key) % self.capacity
    

    def insert(self, key, value): 
        # calculates hash value for given key & return index in capacity of list through private function _hash
        index = self._hash(key) 

        # if the table is null at the required index for insertion -> create a new node & insert at index -> increment size by 1 of HashMap
        if self.table[index] is None: 
            self.table[index] = Node(key, value) 
            self.size += 1
        # Otherwise we assume that the key already exists: 1. we need to update the value of an element stored in key linked list 
        # OR 2. we need to add to the end of the linked list at the key
        else: 
            # get head node at the index required
            current = self.table[index] 
            # keep iterating until we get to a Node that has the "key" we are looking for Or until the current node is null, meaning we are done iterating
            while current: 
                # We gave found an existing Node with a key matching the one we want to insert -> becomes an insert operation
                if current.key == key: 
                    current.value = value # update with new value & return
                    return
                current = current.next # keep iterating through "linked list"
            # We couldn't find a key that matches the one we want to insert -> we need to create a new node & insert a new one to the end of the linked list at that index in the table
            new_node = Node(key, value) # new node is created by calling Node class with key and value passed
            new_node.next = self.table[index] # new node is placed at head of linked list -> the next of the new node becomes the old head of the table at index

            # why place new insertions at head of linked list?
                # In a hash table using chaining, new nodes are often added at the head of the linked list for efficiency.
                # Linking the new node's next to the existing chain ensures the rest of the chain is preserved.

            self.table[index] = new_node # assignment of node at index in the table to the new node
            self.size += 1 # increment size of hashMap by 1


    def search(self, key): 
        # find where the key we want should be in the table through the computed hash value
        index = self._hash(key) 

        # returns head node at the index of the key were looking for
        current = self.table[index] 
        # iterates through "linked list" until either we find the key & we return a value associated OR we cant find the key in the place it should be & return an Error handling
        while current: 
            if current.key == key: 
                return current.value 
            current = current.next
            raise KeyError(key)

    def remove(self, key): 
        # find where the key we want should be in the table through the computed hash value
        index = self._hash(key) 
        # This will help keep track of the node preceding the current node during traversal, which is important for re-linking nodes if the key is found.
        previous = None
        # gets head of list at the index we need
        current = self.table[index] 
        
        # iterates through "linked list" until either we find the key & we remove it and adjust accordingly OR we cant find the key in the place it should be & return an Error handling
        while current: 
            # checks if we have reached the key we want to remove -> if true we can start with removal with 2 scenarios: 1. node is head 2. node isnt head
            if current.key == key: 
                # a check to see if the current node is not the first node in the linked list at an index in a hashmap table
                if previous: 
                    # link the previous node to the key we want to remove -> to the node after the node with the key we want to remove
                    previous.next = current.next
                # means the key we want to remove is the head node of the linked list
                else: 
                    # remove by setting head to the next value in linked list rather than current head
                    self.table[index] = current.next
                
                #decrement size of table to reflect the removal of one key-value pair & return.
                self.size -= 1
                return
            # increment through linked list, storing the last visited node at previous
            previous = current 
            current = current.next

        raise KeyError(key)

    # returns a string representation of the hash map with a list of tuples being the keys: values as pairs
    # elements = [("apple", 10), ("banana", 20), ("cherry", 30)] -> example
    def __str__(self): 
        elements = [] 
        for i in range(self.capacity): 
            current = self.table[i] 
            while current: 
                elements.append((current.key, current.value)) 
                current = current.next
        return str(elements) 

    # uses a list of lists containing tuples -> 1 for each index in the hashmap table
    # def __str__(self): 
    #     elements = [[] for _ in range(self.capacity)]  # Initialize a list of empty lists

    #     for i in range(self.capacity):  # Iterate through all indices
    #         current = self.table[i]  # Get the head of the linked list at index i
    #         while current:  # Traverse the linked list
    #             elements[i].append((current.key, current.value))  # Add (key, value) tuple to the sublist
    #             current = current.next  # Move to the next node
        
    #     return str(elements)  # Convert the list of lists to a string and return

# Driver code 
if __name__ == '__main__': 
  
    # Create a hash table with 
    # a capacity of 5 
    hm = HashMap(5) 
  
    # Add some key-value pairs 
    # to the hash table 
    hm.insert("apple", 3) 
    hm.insert("banana", 2) 
    hm.insert("cherry", 5) 
  
    # Check if the hash table 
    # contains a key 
    # print("apple" in hm)  # True 
    # print("durian" in hm)  # False 
  
    # Get the value for a key 
    print(hm.search("banana"))  # 2 
  
    # Update the value for a key 
    hm.insert("banana", 4) 
    print(hm.search("banana"))  # 4 
  
    hm.remove("apple") 
    # Check the size of the hash table 
    # print(len(hm))  # 3 