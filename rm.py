#!/usr/bin/python
import paramiko
import os
import  subprocess
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('139.199.199.31',66,'root','yangyang2134')   #IP,端口,用户名,密码
cmd = 'rm -rf /root/testt/*'   #远程要执行的命令
ssh.exec_command(cmd)
