from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less")
    return 10/age


try:
    calculate_xfactor(0)
except ValueError as error:
    pass
"""


code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10/age



xfactor=    calculate_xfactor(0)
if xfactor==None:
    pass

"""
print("Code 1", timeit(code1, number=10000))
print("Code 2", timeit(code1, number=10000))
