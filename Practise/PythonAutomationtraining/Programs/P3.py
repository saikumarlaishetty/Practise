# tuple class
# values to be unpacked

dob = "15-aug-1947"
day,month,year = dob.split("-")
print(day)
print(month)
print(year)

"-------OR---------"
print((dob.split("-"))[0])
print((dob.split("-"))[1])
print((dob.split("-"))[2])
