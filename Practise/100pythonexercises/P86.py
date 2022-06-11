checklist = ["Portugal", "Germany", "Munster", "Spain"]

countries = []
with open('countries_clean.txt','r')as file:
    content = file.readlines()
    content = [i.rstrip('\n') for i in content]
    countries = [country for country in content if country in checklist]
    print(countries)

#print(countries)

#or

