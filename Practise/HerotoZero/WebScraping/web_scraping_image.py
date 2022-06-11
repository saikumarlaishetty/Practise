# Getting an image from a website
import requests,bs4

res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text,'lxml')

image_info = soup.select('.thumbimage')
#print(image_info)
#print(len(image_info))
computer = image_info[0]
#print(type(computer))
#print(computer['src'])

image_link = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png")
print(image_link.content)

f = open('my_new_file_name.jpg','wb')
f.write(image_link.content)
f.close()


