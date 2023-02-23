from bs4 import BeautifulSoup


with open("index2.html","r") as f:
    doc = BeautifulSoup(f,"html.parser")

# searching for tags
# result = doc.find_all("option")
# print(result)

# changing the values of the tag.
tag = doc.find("option")
tag['value'] ="new value"   # we can change and acess these values like dictionary
tag["selected"] = "False"
tag["color"] = "bule"         # we can add new value like color as well
# print(tag.attrs)           # To see all the attributes


# To find multiple tag name at the same time
tags = doc.find_all(["p","div","li"])
# print(tags)

# To find tag with combination of text
tags = doc.find_all(["option"],text="Undergraduate")
# print(tags)

# To find tag with specific attributes
tags = doc.find_all(["option"],text="Undergraduate",value="undergraduate")
# print(tags)


# To find the class names
# As class is a reseverd keyword in python we should use class_
tags = doc.find_all(class_='btn-item')
# print(tags)

# use regular expression
import re
tags = doc.find_all(text=re.compile('\$.*'))
#for tag in tags:
#    print(tag.strip())

# Find limit -> To limit the result
tags = doc.find_all(text=re.compile('\$.*'),limit=1)
#for tag in tags:
#    print(tag.strip())


# Save the modified HTML
tags = doc.find_all("input",type="text")
for tag in tags:
    tag['placeholder'] ='I changed you!'

with open('changed.html','w') as file:
    file.write(str(doc))








