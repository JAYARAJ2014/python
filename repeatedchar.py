# Find most repeated character from a sentence

sentence = "This is a common interview question"
# loop through each char and
dix = {}
for c in sentence:
    # find the occourance of c and add the result to another dictionary
    if not c in dix:
        dix[c] = sentence.count(c)

# Sort dictionary in reverse order
# We have to convert the dix to iterable and pass lambda
sort = sorted(dix.items(), key=lambda kv: kv[1], reverse=True)
# pick the first item from the sorted.
print(sort[0])
