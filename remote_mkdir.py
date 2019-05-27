#!/usr/bin/python3
import pexpect
user='root'
host='192.168.114.58'
password='000000'
command = 'ssh '+user+'@'+host +'mkdir -p /root/bakcup/python'
child=pexpect.spawn(scpcommand,timeout=10)
child.expect('password:')
child.sendline(password)
