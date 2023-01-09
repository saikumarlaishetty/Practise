
line = input("Enter values: ")
line_list = line.split(",")
with open("user_data_commas.txt", "a+") as file:
    for i in line_list:
        file.write(i + "\n")