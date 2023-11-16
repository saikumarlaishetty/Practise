import matplotlib.pyplot as plt


import csv
d = {}
with open('Emissions.csv','r') as file:
    reader = csv.reader(file)
    #print("A simple data Analysis program")
    #print(" ")
    for data in reader:
        d[data[0]] = data[1:]

#print("All data from Emissions.csv has been read into a dictionary.")
year = input("Select a year to find statistics (1997 to 2010) :  ")
year_index = d['CO2 per capita'].index(year)

list_of_emission = []
dic = {}

for key,value in d.items():
    if key != 'CO2 per capita':
        list_of_emission.append(float(value[year_index]))
        dic.update({key:float(value[year_index])})

minimum_country  = min(dic,key=dic.get)
maxmium_country = max(dic,key=dic.get)

average = sum(list_of_emission)/len(list_of_emission)

#print("In {0}, countries with minimum and maximum CO2 emission levels were: [{1}] and [{2}] respectively.".format(year,minimum_country,maxmium_country))
#print("Average CO2 emissions in {0} were {1} ".format(year,average))

visual = input("Select the country to visualize : ")

years = list(map(int,d['CO2 per capita']))
emissions =list(map(float,d[visual]))

ylabel = "Emissions in "+visual

plt.xlabel("Years")
plt.ylabel(ylabel)



plt.plot(years,emissions)
plt.show()




"""Code with experts"""

#
#
# """
# Name: Python Data Analysis
# Purpose: Plotting emission graph for country
#
# Algorithm:
#
# Step 1: Take the input from user to visualize data
# Step 2: Getting the index of Country and passing it to plot function, Setting the Title and Label of Plot
#
# """
#
# import matplotlib.pyplot as plt
#
#
# print("A Simple Data Analysis Program")
# print()
#
# emission_dict = {}
#
# with open('Emissions.csv', 'r') as file:
#     for data in file.read().split('\n'):
#         emission_dict.update({data.split(',')[0]: data.split(',')[1:]})
#
# print("All data from Emissions.csv has been read into a dictionary.", end="\n\n")
#
# input_year = input("Select a year to find statistics (1997 to 2010): ")
#
# index_of = int()
# lines = []
#
# for item in emission_dict.values():
#     if input_year in item:
#         index_of = (item.index(input_year))
#
# total = 0
# i = 0
# emissions_in_year = []
#
# for value in emission_dict.values():
#     if i != 0:
#         total += float(value[index_of])
#         emissions_in_year.append(list(emission_dict.values())[i][index_of])
#     i += 1
#
# max_country_index = int(emissions_in_year.index(str(max(float(str_value) for str_value in emissions_in_year))))
# min_country_index = int(emissions_in_year.index(str(min(float(str_value) for str_value in emissions_in_year))))
# average_emissions = total / 195
#
# max_emission = list(emission_dict.keys())[max_country_index + 1]
# min_emission = list(emission_dict.keys())[min_country_index + 1]
#
# print(f'In {input_year}, countries with minimum and maximum CO2 emission levels were: [{min_emission}] '
#       f'and [{max_emission}] respectively.')
# print(f'Average CO2 emissions in {input_year} were {"%.6f" % round(average_emissions, 6)}')
# print()
#
# """
# Step 1: Take the input from user to visualize data
# """
# visualize_country = input("Select the country to visualize: ")
#
# """
# Step 2: Getting the index of Country and passing it to plot function, Setting the Title and Label of Plot
# """
# # From user entered value we extracted the Index value of country
# number = list(emission_dict.keys()).index(visualize_country)
# # Passed that index value to matplotlib plot function. As x value we passed years and as y value we passed emission value
# plt.plot(list(map(float, list(emission_dict.values())[0])),
#          list(map(float, list(emission_dict.values())[number])))
# # Given the Title and Lable to Plot
# plt.title("Year vs Emissions in Capita")
# plt.xlabel("Year")
# plt.ylabel("Emissions in " + visualize_country.title())
# plt.show()
# print()
