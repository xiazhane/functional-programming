def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    def decrement():
        nonlocal count
        count -= 1
        return count
    return increment, decrement


# Example usage:
increment, decrement = make_counter()

print("Initial Count:", increment())  # Output: 1
print("Incremented Count:", increment())  # Output: 2
print("Decremented Count:", decrement())  # Output: 1
