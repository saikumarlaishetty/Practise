import paramiko

# Create object of SSHClient and
# connecting to SSH
ssh = paramiko.SSHClient()

# Adding new host key to the local
# HostKeys object(in case of missing)
# AutoAddPolicy for missing host key to be set before connection setup.
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('10.106.141.33', port=1122, username='admin',
            password='Lab@1234', timeout=3)

# Execute command on SSH terminal
# using exec_command
#print(ssh.exec_command('show application status ise'))
stdin, stdout, stderr = ssh.exec_command('show application status ise')

stdin.read

#print(stdin)

#print(stdout)
