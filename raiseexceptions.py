### Raise exceptions only if it is really neede. This is a costly thing to do (Even in C#)


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less")
    return 10/age


try:
    calculate_xfactor(0)
except ValueError as error:
    print(error)
