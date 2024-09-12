with open("file1.txt") as file:
    file_1_data = file.readlines()
    file_1 = []
    for data in file_1_data:
        new_data = data.strip("\n")
        file_1.append(new_data)

with open("file2.txt") as file:
    file_2_data = file.readlines()
    file_2 = []
    for data in file_2_data:
        new_data = data.strip("\n")
        file_2.append(new_data)

result = [int(num) for num in file_1 if num in file_2]
print(result)