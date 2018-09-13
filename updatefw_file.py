from paramiko import SSHClient
import paramiko, socket
import sys

f = open("listhosts.txt", 'r')
listhosts = f.readlines()

cont = 1
index = 0

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

while cont <= (len(listhosts)):
    try:
        testpass = ssh.connect(hostname=listhosts[index],port=8822,username='admin',password='trypassword', timeout=5)
        stdin,stdout,stderr = ssh.exec_command("config system central-management \n set type fortimanager \n set fmg 200.238.106.21 \n end")
        if stderr.channel.recv_exit_status() != 0:
            print stderr.read()
        else:
            print "Host:", listhosts[index], "- ok"

            cont += 1
            index += 1

    except paramiko.AuthenticationException:
        testpass = ssh.connect(hostname=listhosts[index],port=8822,username='admin',password='trypassword2', timeout=5)
        stdin,stdout,stderr = ssh.exec_command("config system central-management \n set type fortimanager \n set fmg 200.238.106.21 \n end")
        if stderr.channel.recv_exit_status() != 0:
            print stderr.read()
        else:
            print "Host:", listhosts[index], "- ok"

            cont += 1
            index += 1

    except socket.timeout:
        print "Host:", listhosts[index],"- IP ou Porta invalida"
        cont += 1
        index += 1

    


