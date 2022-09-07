def extraction(file_name):
    with open(file_name) as f1:
        list_1 = f1.readlines()

    new_list_1 = []

    for n in list_1:
        n.strip("\n")
        new_list_1.append(int(n))

    return new_list_1

l1 = extraction("file1.txt")
l2 = extraction("file2.txt")

result = [n for n in l1 if n in l2]

# Write your code above 👆

print(result)
