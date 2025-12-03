# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node =  (data)
        new_node.next = self.head
        self.head = new_node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = (data)
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Delete a node by key (data value)
    def delete_node(self, key):
        temp = self.head

        # If head node itself holds the key
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        # Search for the key to be deleted
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # If key was not present
        if temp is None:
            print(f"Key {key} not found in the list.")
            return

        # Unlink the node from linked list
        prev.next = temp.next
        temp = None

    # Traverse and display the list
    def display_list(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> " if temp.next else "\n")
            temp = temp.next