from functools import reduce
numbers = [1, 2, 3, 4, 5]
odd_numbers = filter(lambda x: x % 2 != 0, numbers )
squared_odd_numbers = map(lambda x: x**2, odd_numbers)
result = odd_numbers,squared_odd_numbers,reduce(lambda x, y: x + y, squared_odd_numbers, 0)
print(numbers)
print(squared_odd_numbers)
print(result)

