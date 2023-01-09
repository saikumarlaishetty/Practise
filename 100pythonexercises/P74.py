import pandas

data1 = pandas.read_csv("https://pythonhow.com/media/data/sampledata.txt")
data2 = pandas.read_csv("https://pythonhow.com/media/data/sampledata_x_2.txt")

con = pandas.concat([data1,data2])
con.to_csv("cont.txt",index = None)


# or

import io
import pandas
import requests

r = requests.get("http://www.pythonhow.com/data/sampledata.txt")
c = r.content
data1 = pandas.read_csv(io.StringIO(c.decode('utf-8')))
data2 = pandas.read_csv("sampledata_x_2.txt")
data12 = pandas.concat([data1, data2])
data12.to_csv("sampledata12.txt", index=None)