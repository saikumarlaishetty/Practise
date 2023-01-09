import glob

file_list = glob.glob("letters/*.txt")
letters =[]
for filename in file_list:
    with open(filename,'r') as file:
        letter = file.read()
    if letter in 'python':
        letters.append(letter)

print(letters)
