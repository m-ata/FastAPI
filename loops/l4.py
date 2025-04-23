sen = "Pypthoan"

non_repeated_chars = ""

for ltr in sen:
    if sen.count(ltr) == 1:
        non_repeated_chars += ltr  # add to result

print("------")
print("ALL NON-REPEATED CHARACTERS =", non_repeated_chars)
