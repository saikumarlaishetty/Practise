from datetime import datetime

present_year = datetime.now().year


age = int(input("Enter your age :"))
print("we think you were born back in ",(present_year-age))