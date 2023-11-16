import matplotlib.pyplot as plt


import csv
d = {}
with open('Emissions.csv','r') as file:
    reader = csv.reader(file)
    #print("A simple data Analysis program")
    #print(" ")
    for data in reader:
        #print(data)
        d[data[0]] = data[1:]

#print("All data from Emissions.csv has been read into a dictionary.")
#year = input("Select a year to find statistics (1997 to 2010) :  ")
#year_index = d['CO2 per capita'].index(year)

#list_of_emission = []
#dic = {}

#for key,value in d.items():
#    if key != 'CO2 per capita':
#        list_of_emission.append(float(value[year_index]))
#        dic.update({key:float(value[year_index])})

#minimum_country  = min(dic,key=dic.get)
#maxmium_country = max(dic,key=dic.get)

#average = sum(list_of_emission)/len(list_of_emission)

#print("In {0}, countries with minimum and maximum CO2 emission levels were: [{1}] and [{2}] respectively.".format(year,minimum_country,maxmium_country))
#print("Average CO2 emissions in {0} were {1} ".format(year,average))

#visual = input("Select the country to visualize : ")

#years = list(map(int,d['CO2 per capita']))
#emissions =list(map(float,d[visual]))

#ylabel = "Emissions in "+visual

#plt.xlabel("Years")
#plt.ylabel(ylabel)

#plt.plot(years,emissions)
#plt.show()


#countryname1,countryname2 = input("Write two comma seperated countries to visuialize data : ").split(',')

#years = list(map(int,d['CO2 per capita']))
#country1 = list(map(float,d[countryname1]))
#country2 = list(map(float,d[countryname2]))

#ylabel = "Emissions in "


#plt.title("Year Vs Emissions in Capita")

#plt.xlabel("Years")
#plt.ylabel(ylabel)

#plt.plot(years,country1,label=countryname1,color='b')
#plt.plot(years,country2,label=countryname2,color='r')

#plt.legend(loc='upper left')
#plt.show()

countries = input(f"Write up to three comma seperated countries for which you want to extract data : ").split(',')

if len(countries) > 3:
    print("ERR: Sorry at most 3 countries can be entered.")
else:
    print(countries)
    filename = "Emissions_subset.csv"
    fields = []
    rows = []
    for key,value in d.items():
        if 'CO2 per capita' in key:
            fields.append(key)
            fields.extend(value)

        for country in countries:
            if key in country:
                row = []
                row.append(key)
                row.extend(value)
                rows.append(row)

    with open(filename, 'w',newline='') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(fields)

        # writing the data rows
        csvwriter.writerows(rows)

    #print(fields)
    #print(rows)



"""
CODE WITH EXPERTS

"""



"""
# 
# Name: Python Data Analysis
# Purpose: Writing data to CSV
# 
# Algorithm:
# 
# Step 1: Take input up to three comma-separated countries and creating list of countries (Passing value to our next step function)
# Step 2: Creating function that will take one list input - Check for maximum three countries and write to Emissions_subset.csv file
# 
# """
#
# import matplotlib.pyplot as plt
#
# """
# Step 2: Creating function that will take one list input - Check for maximum three countries and write to Emissions_subset.csv file
# """
#
#
# def extract_data(country):
#     list_len = len(country)
#     for length in range(0, list_len):
#         # Validating input up to three countries - If there are more then three countries then return false
#         if list_len > 3:
#             print("ERR: Sorry, at most 3 countries can be entered.", end="\n\n")
#             return False
#     else:
#         # Creating string to write in CSV File
#         write_line_csv = list(emission_dict.keys())[0].title() + "," + ",".join(list(emission_dict.values())[0]) + "\n"
#         for num in range(0, len(country)):
#             write_line_csv += country[num].title() + "," + ",".join(
#                 emission_dict[country[num]]) + "\n"
#         # Open CSV in write mode and writing lines to CSV
#         with open('Emissions_subset.csv', 'w') as new_file:
#             new_file.writelines(write_line_csv)
#         # Printing the value in required format
#         print(f"Data successfully extracted for countries " + ", ".join(
#             country).title() + " saved into file Emissions_subset.csv", end="\n\n")
#     return True
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
#
# visualize_country = input("Select the country to visualize: ")
#
# number = list(emission_dict.keys()).index(visualize_country)
# plt.plot(list(map(float, list(emission_dict.values())[0])),
#          list(map(float, list(emission_dict.values())[number])))
# plt.title("Year vs Emissions in Capita")
# plt.xlabel("Year")
# plt.ylabel("Emissions in " + visualize_country.title())
# plt.show()
# print()
#
# country1, country2 = input("Write two comma-separated countries for which you want to visualize data: ").split(", ")
#
# index_num_1 = list(emission_dict.keys()).index(country1)
# index_num_2 = list(emission_dict.keys()).index(country2)
#
# plt.plot(list(map(float, list(emission_dict.values())[0])),
#          list(map(float, list(emission_dict.values())[index_num_1])), label=country1)
# plt.plot(list(map(float, list(emission_dict.values())[0])),
#          list(map(float, list(emission_dict.values())[index_num_2])), label=country2)
# plt.title("Year vs Emissions in Capita")
# plt.xlabel("Year")
# plt.ylabel("Emissions in ")
# plt.legend()
# plt.show()
# print()
#
# """
# Step 1: Take input up to three comma-separated countries and creating list of countries (Passing value to our function)
# """
#
# while True:
#     input_string = input("Write up to three comma-separated countries for which you want to extract data: ")
#     input_country = input_string.split(", ")
#     # Calling the Function to validate input
#     if not extract_data(input_country):
#         continue
#     else:
#         break
