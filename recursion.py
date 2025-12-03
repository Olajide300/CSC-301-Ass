# Here’s how to get the sum of the first ten natural numbers (1–10) using recursion.
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)

print(sum(10))
# Output: 55
