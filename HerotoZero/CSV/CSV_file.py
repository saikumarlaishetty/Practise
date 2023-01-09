import csv

data = open('example.csv',encoding='utf-8')
#print(data)
csv_data = csv.reader(data)
#print(csv_data)
data_lines =list(csv_data)
#print(data_lines)

#print(data_lines[:3])

for line in data_lines[:5]:
    print(line)

print(len(data_lines))

all_emails =[]
for line in data_lines[1:15]:
    all_emails.append(line[3])

#print(all_emails)

# Writing to csv files
file_to_output= open('to_save_file.csv','w',newline='')
csv_writer = csv.writer(file_to_output,delimiter=',')
csv_writer.writerow(['a','b','c'])
csv_writer.writerows([['1','2','3'],['4','5','6']])
file_to_output.close()

# read the file
file_to_output = open('to_save_file.csv',encoding='utf-8')
csv_reader = csv.reader(file_to_output)
print(list(csv_reader))

