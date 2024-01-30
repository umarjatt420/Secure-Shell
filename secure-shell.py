import paramiko

# SSH connection parameters
hostname = '192.168.10.11'
username = 'mariana_squad'
password = 'Pass@420.'

# Create an SSH client
client = paramiko.SSHClient()
while True:
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password)
    stdin, stdout, stderr = client.exec_command(input('write command to execute: '))
    
    # Retrieve and print the output
    output = stdout.read().decode('utf-8')
    print(output)
