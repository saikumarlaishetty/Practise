import re
import platform
import subprocess


def myping(host):
    parameter = '-n' if platform.system().lower() == 'windows' else '-c'

    command = ['ping', parameter, '1', host]
    response = subprocess.call(command)

    if response == 0:
        return True
    else:
        return False

with open('data.txt') as file:
    f = file.readlines()

pattern =re.compile('''((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.)
{3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)''')

import re

ip = ["255.255.255.0",
      "127.0.0.1",
      "123.123.333.333",
      "255,255.255.255"]

pattern =


for i in ip:
    validip = re.match(
        r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", i)

    if validip:
        print(validip.group())
    else:
        print(i)


valid = []
invalid = []
for line in f:
    line = line.rstrip()
    result = pattern.search(line)
    if result:
        valid.append(line)
    else:
        invalid.append(line)

print(valid)
print(invalid)

reach = []
unreach = []
for ip in valid:
    if myping(ip):
        reach.append(ip)
    else:
        unreach.append(ip)

print(reach)
print(unreach)
