from lxml import etree

doc = etree.parse("data.xml")
root = doc.getroot()
res = root.findall(".//record/name")
print("Res",res)
print([e.text for e in res])

from lxml import etree
doc = etree.parse("data.xml")
root = doc.getroot()
res = root.iterfind("record/name")
alst1 = [e.text for e in res ]
root = doc.getroot()
res = root.iterfind("record/branch")
alst2 = [e.text for e in res ]
print(dict(zip(alst1, alst2)))