
#This is how we write CSV file in python:

```
import csv

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([1, 1000, 90.65])
    writer.writerow([2, 1001, 40.75])
    writer.writerow([3, 1001, 40.75])
```

Note that if the file is named csv.py , then when you import csv you will get erro. 
