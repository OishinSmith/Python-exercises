import sys
number_less_than = int(sys.argv[1]) + 1

all_numbers = [n for n in range(number_less_than) if n > 0]

multiples = [m for m in all_numbers if m % 3 == 0]
print("Multiples of 3:", multiples)

print("Multiples of 3 squared:", [m * m for m in all_numbers if m % 3 == 0]) 

print("Multiples of 4 doubled:", [m * 2 for m in all_numbers if m % 4 == 0])

print("Multiples of 3 or 4:", [m for m in all_numbers if m % 3 == 0 or m % 4 == 0])

print("Multiples of 3 and 4:", [m for m in all_numbers if m % 12 == 0])

print("Multiples of 3 replaced:", ["X" if m % 3 == 0 else m for m in all_numbers])
