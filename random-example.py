import random
import string


print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4, 6, 7]))
print(random.choices(range(1, 100), k=2))
print("".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=4)))
print(string.digits)
print(string.ascii_letters)
print("".join(random.choices(string.ascii_lowercase+string.digits, k=8)))

# shuffling array
numbers = list(range(1, 20))
random.shuffle(numbers)
print(numbers)
