

try:
    age = int(input("Age"))
    xfactor = 10/age
except (ValueError, ZeroDivisionError): #Multiple exceptions in oneline.
    print("You didn't enter a valid age")
else:
    print("THere was no errors")
print("Execution continues...")
