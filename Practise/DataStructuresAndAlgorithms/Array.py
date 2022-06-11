# In Python, list is implemented as dynamic array
# In other languages like C++, Java we have static and dynamic arrays both

# Exercises
# https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md

"""
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,
"""
expenses = [2200, 2350, 2600, 2130, 2190]

print(expenses)

# 1. In Feb, how many dollars you spent extra compare to January?
print(f'In Feb, We have spent {(expenses[1]-expenses[0])} extra compare to January')

# 2. Find out your total expense in first quarter (first three months) of the year.
print(f'Total expense in first quarter is {expenses[0]+expenses[1]+expenses[2]}')

# 3. Find out if you spent exactly 2000 dollars in any month
print("Did you spent 2000$ in any month? ", 2000 in expenses)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expenses.append(1980)
print("Expenses at the end of June:",expenses)

# 5. You returned an item that you bought in a month of April and got a refund of 200$.
#  Make a correction to your monthly expense list based on this

expenses[3] = expenses[3] - 200
print("Expenses after 200$ return in April :", expenses)



"""
You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
Using this find out,
"""
heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
print("Length of the list is ",len(heros))

# 2. Add 'black panther' at the end of this list
heros.append('black panther')
print("Added black panther",heros)

# 3. You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
heros.insert(3,'black panther')
print(heros)            # ['spider man', 'thor', 'hulk', 'black panther', 'iron man', 'captain america']


# 4. Now you don't like thor and hulk because they get angry easily :)
# So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).Do that with one line of code.

heros[1:3] = ['doctor strange']
print(heros)

# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
print(sorted(heros))
print(heros)
heros.sort()
print(heros)
print(dir(heros))


# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function


def odd_numbers(max):
    odd_list = [i for i in range(1,max) if i%2 !=0]
    print("Odd numbers list is ",odd_list)
max_number = int(input("Enter a max number"))
odd_numbers(max_number)



