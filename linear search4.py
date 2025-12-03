# Linear Search 

values = [2, 5, 7, 10, 14, 20]
target = 10

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i   # Return index where target is found
    return -1          # Return -1 if not found

# Perform the search
index = linear_search(values, target)

# Output results
if index != -1:
    print(f"Target {target} found at index {index}.")
else:
    print("Target not found.")
    
    # Output: Target 10 found at index 3.
    

