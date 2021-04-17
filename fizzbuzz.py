# FizzBuzz problem
# Input divisible by 3 Fizz
#       divisible by 5 Buzz
#       divisible by both FizzBuzz
# Else return input

def fizz_buzz(input):

    if (input % 3 == 0) and (input % 5 == 0):
        return 'Fizz Buzz'
    if input % 3 == 0:
        return 'Fizz'
    if input % 5 == 0:
        return 'Buzz'
    return input


print(fizz_buzz(5))  # Expected Output: Buzz
print(fizz_buzz(3))  # Expected Output: Fizz
print(fizz_buzz(15))  # Expected Output: FizzBuzz
print(fizz_buzz(7))  # Expected Output: 7
