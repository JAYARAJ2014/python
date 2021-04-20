import csv


def writecsv():
    with open("data.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["transaction_id", "product_id", "price"])
        writer.writerow([1, 1000, 90.65])
        writer.writerow([2, 1001, 40.75])
        writer.writerow([3, 1001, 40.75])


def readcsv():
    with open("data.csv") as file:
        reader = csv.reader(file)
        # print(list(reader)) # commented because you can iterate only once.
        for row in reader:
            if row[0] == 'transaction_id':
                print(f"{row[0]}\t{row[1]}\t{row[2]}")
            else:
                print(
                    f"{row[0].ljust(14,' ')}\t{row[1].ljust(14,' ')}\t{row[2].ljust(14,' ')}")


writecsv()
readcsv()
