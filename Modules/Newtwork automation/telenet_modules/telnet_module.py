# Uses Transmission Control Protocol for data transmission

# ===================================
# Pending  ....YET TO WORK ON IT
###################################

"""
Important Functions:

Telnet.read_until(expected, timeout=None)
Telnet.read_all()
Telnet.open(host, port=0[, timeout])
Telnet.close()
Telnet.write(buffer)
Telnet.interact()

"""

import telnetlib

host = "10.106.141.33"
port = '1622'
username = 'admin'
password = 'Lab@1234'


tn = telnetlib.Telnet(host,port)

#print(tn)

tn.open(b'10.106.141.33','1622')

tn.read_until(b':')
tn.write(b'admin')
#tn.write(b'\n')

tn.read_until(b'Password:')
tn.write(b'Lab@1234')

tn.write(b'show application')
tn.write(b':')
#tn.write()