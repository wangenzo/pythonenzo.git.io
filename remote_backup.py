#!/usr/bin/python3
import pexpect
user='root'
host='192.168.114.58'
password='000000'
command='ssh ' + user +'@'+host + ' sudo mkdir /root/test '
child=pexpect.spawn(command,timeout=10)
child.expect('password:')
child.sendline(password)
