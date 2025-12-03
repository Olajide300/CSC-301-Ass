# Function to calculate the total sum of elements in an array
def total_sum(arr):
    total = 0
    for i in arr:
        total += i
    return total



# ACtivity2: Code for Insertion at Head (for reference)
def insert_at_head(head, value):
    new_node = (value)
    new_node.next = head
    return new_node  # new head