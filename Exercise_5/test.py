# Testing the Linked List
if __name__ == "__main__":
    llist = ()

    # Inserting at least 5 values
    llist.insert_at_end(10)
    llist.insert_at_end(20)
    llist.insert_at_beginning(5)
    llist.insert_at_end(30)
    llist.insert_at_beginning(1)

    print("Linked List after insertions:")
    llist.display_list()          # Output: 1 -> 5 -> 10 -> 20 -> 30

    # Deleting one node (e.g., 20)
    llist.delete_node(20)
    print("Linked List after deleting 20:")
    llist.display_list()          # Output: 1 -> 5 -> 10 -> 30