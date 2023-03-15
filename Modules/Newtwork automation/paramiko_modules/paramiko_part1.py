import paramiko

import time

host = "10.106.141.33"
username = 'admin'
password = 'Lab@1234'
port = 1222
timeout = 0
command = 'show version'
prompt = '#'

def send_command_read_untill_prompt(ssh_channel, command, prompt="#"):
    '''
    This method send command to remote machine and reads the output untill the expected prompt is received
    for eg:  command = show clock, expected prompt: "#"  this method behave as shown in below log of this method
    2017-02-09 05:12:52,795 INFO [] sending command: show clock
    Positron-vm-2/admin# show clock
    2017-02-09 05:12:55,954 INFO [] does buffer ends with prompt False
    2017-02-09 05:12:56,455 INFO [] response received: Thu May 11 11:12:54 PDT 2017
    Positron-vm-2/admin#
    2017-02-09 05:12:56,456 INFO [] does buffer ends with prompt True
    :param ssh_channel:
    :param command:
    :param prompt:
    :return:
    '''
    buffer = ''
    #s_log.info("sending command: " + command)
    print("sending command: " + command)
    ssh_channel.send(command + '\n')
    # while (not buffer.endswith(prompt)) or (not buffer.endswith('#')) :
    while (not buffer.endswith(prompt)):
        resp = ssh_channel.recv(9999)
        buffer += resp.decode("utf-8", "ignore")
        #s_log.info("response received: " + resp.decode("utf-8", "ignore"))
        print("response received: " + resp.decode("utf-8", "ignore"))
        print("does buffer ends with prompt " + str(buffer.endswith(prompt)))
    print(buffer[buffer.rfind(command) - command.__len__():])
    return buffer[buffer.rfind(command) + len(command):]


print("Starting Connection Setup")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(host,port, username= username, password=password, look_for_keys=True)
#channel=ssh.invoke_shell()
#temp=str()
# while True:
#     if(channel.recv_ready()==True):
#         time.sleep(5)
#         output = channel.recv(8000)
#         temp+=output.decode("utf-8","ignore")
#         if (temp.endswith("Enter session number to resume or press <Enter> to start a new one:")==True):
#             channel.send("\n")
#         else:
#             break
#     else:
#         continue

#
# #print("________________________________")
# print("temp",temp)
# #print("________________________________")
# time.sleep(5)


# channel.send(command +'\n')
# while True:
#     if (channel.recv_ready() == True):
#         time.sleep(5)
#         break
#     else:
#         continue
# if timeout:
#     time.sleep(timeout)



buffer = ''
#s_log.info("sending command: " + command)
print("sending command: " + command)
#channel.send(command + '\n')
stdin,stdout,stderr = ssh.exec_command('show version')
#exit_status = stdout.recv_exit_status()
print(stdout.readlines())
# # while (not buffer.endswith(prompt)) or (not buffer.endswith('#')) :
# while (not buffer.endswith(prompt)):
#     resp = channel.recv(9999)
#     buffer += resp.decode("utf-8", "ignore")
#     #s_log.info("response received: " + resp.decode("utf-8", "ignore"))
#     print("response received: " + resp.decode("utf-8", "ignore"))
#     print("does buffer ends with prompt " + str(buffer.endswith(prompt)))
# #print(buffer[buffer.rfind(command) - command.__len__():])
# print(buffer[buffer.rfind(command)+len(command):])



#result = output.decode("utf-8")

#print(result)






# try:
#
#     # create a session
#     session = paramiko.SSHClient()
#
#     # Added for missing host keys
#     session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
#
#     session.connect(hostname=hostname,port=port,username=username,password=password,look_for_keys=True,timeout=10)
#     channel = session.invoke_shell(term='vt100', width=100, height=100, width_pixels=0, height_pixels=0)
#     print("Connection success")
#
#     ssh_stdin, ssh_stdout, ssh_stderr = session.exec_command(command,timeout=10)
#
#     output = ssh_stdout.read(200)
#     result = output.decode("utf-8")
#     print(result)





#     temp = str()
#     while True:
#         if (channel.recv_ready() == True):
#             time.sleep(5)
#             output = channel.recv(8000)
#             temp += output.decode("utf-8")
#             if (temp.endswith("Enter session number to resume or press <Enter> to start a new one:") == True):
#                 channel.send("\n")
#             else:
#                 break
#         else:
#             continue
#
#     print(temp)
#     time.sleep(5)
#
#     channel.send(command)
#     while True:
#         if (channel.recv_ready() == True):
#             time.sleep(5)
#             break
#         else:
#             continue
#     if timeout:
#         time.sleep(timeout)
#
#     output = channel.recv(8000)
#     result = output.decode("utf-8")
#
#     print("Result command :",result)
#
#     # output = stdout.readlines(300)
#     print(output)
# except Exception as e:
#      print("Exeception as ", e)


# channel=session.invoke_shell(term='vt100', width=100, height=100, width_pixels=0,height_pixels=0)
#
# output = channel.recv(8000)
#
# result=output.decode("utf-8")
#
# print(result)