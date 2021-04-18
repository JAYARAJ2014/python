from pprint import pprint

try:
    file = open("app.py")
    pprint(file.readlines())
    age = int(input("Age"))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
else:
    print("THere was no errors")
finally:
    file.close() #finally block closes the open file
print("Execution continues...")

## Compare this to try-catch-finally in C#
