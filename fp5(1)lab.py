def arithmetic_sequence(term, difference):
    current_term = term
    while True:
        yield current_term
        current_term += difference

term = int(input("Enter the initial term of the arithmetic sequence: "))
difference = int(input("Enter the common difference of the arithmetic sequence: "))
generator = arithmetic_sequence(term, difference)

for i in range(4):
    print(next(generator))

