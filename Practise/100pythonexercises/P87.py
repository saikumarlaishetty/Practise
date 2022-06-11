checklist = ['Portugal','Spain','Germany']
checlist = [i + "\n" for i in checklist]
#print(checklist)
with open("countries_missing.txt",'r') as file:
    content = file.readlines()
    #print(content)

updated_list = sorted(checklist+content)
#print(updated_list)

with open('countries_fixed.txt','w') as file:
    for i in updated_list:
        file.write(i)