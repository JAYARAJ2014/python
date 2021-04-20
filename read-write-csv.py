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
        print(list(reader))


readcsv()
