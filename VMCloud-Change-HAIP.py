<<<<<<< HEAD
#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:VMCloud-StatLee
import os,sys,re
import subprocess
import time
import socket

def NetPortCheck(ip,port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(1)
    try: 
        tmp=sk.connect((ip,port))
        return "OK"
    except Exception:
        return "NotOk"
        os.system('echo PortFalse >> /var/log/vmclog.log')
        sk.close()

def NetCheck(ip):
    try:
        p = subprocess.Popen(["ping -c 1 -w 1 "+ ip],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        out=p.stdout.read()
    #err=p.stderr.read()
        regex=re.compile('100% packet loss')
    #print out
    #print regex
    #print err
        if len(regex.findall(out)) == 0:
            return 'UP'
        else:
            return 'DOWN'
    except:
        print 'NetCheck work error!'
        return 'ERR'
def GetCVMInstance(insid):
    try:
        gvminrs=os.popen('python2.6 VMCloud-Display-HAIP.py ' + insid).read().strip()
        if "192.168.108.219" in gvminrs:
            return 'SQL01'
            os.system('echo' + insid + 'SQL01 Successful >> /var/log/vmclog.log')
        else:
            return 'SQL02'
            os.system('echo' + insid + 'SQL02 Successful >> /var/log/vmclog.log')
    except:
        print 'GetError'
        os.system('echo' + insid + 'Connect Error >> /var/log/vmclog.log')
        return 'ERR'    
if __name__ == '__main__':
    iprs=NetCheck('需要检查的群集IP')
    if iprs == 'DOWN': 
        nodename=GetCVMInstance('第一个节点的网卡实例ID')
        if nodename == 'SQL01':
            mvto2a=os.system('python2.6 VMCloud-Migrate-HAIP.py VPC网络的ID 需要检查的群集IP 第一个节点的网卡实例ID 第二个节点的网卡实例ID')
            os.system('echo 切换到SQL02 成功 >> /var/log/vmclog.log')
        else:
            mvto2b=os.system('python2.6 VMCloud-Migrate-HAIP.py VPC网络的ID 需要检查的群集IP 第二个节点的网卡实例ID 第一个节点的网卡实例ID')
            os.system('echo 切换到SQL01 成功 >> /var/log/vmclog.log')
=======
#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:VMCloud-StatLee
import os,sys,re
import subprocess
import time
import socket

def NetPortCheck(ip,port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(1)
    try: 
        tmp=sk.connect((ip,port))
        return "OK"
    except Exception:
        return "NotOk"
        os.system('echo PortFalse >> /var/log/vmclog.log')
        sk.close()

def NetCheck(ip):
    try:
        p = subprocess.Popen(["ping -c 1 -w 1 "+ ip],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        out=p.stdout.read()
    #err=p.stderr.read()
        regex=re.compile('100% packet loss')
    #print out
    #print regex
    #print err
        if len(regex.findall(out)) == 0:
            return 'UP'
        else:
            return 'DOWN'
    except:
        print 'NetCheck work error!'
        return 'ERR'
def GetCVMInstance(insid):
    try:
        gvminrs=os.popen('python2.6 VMCloud-Display-HAIP.py ' + insid).read().strip()
        if gvminrs.find("XX.XX.XX.XX") == -1:
            return 'SQL01'
            os.system('echo' + insid + 'SQL01 Successful >> /var/log/vmclog.log')
        else:
            return 'SQL02'
            os.system('echo' + insid + 'SQL02 Successful >> /var/log/vmclog.log')
    except:
        print 'GetError'
        os.system('echo' + insid + 'Connect Error >> /var/log/vmclog.log')
        return 'ERR'    
if __name__ == '__main__':
    iprs=NetCheck('XX.XX.XX.XX')
    if iprs == 'DOWN': 
        nodename=GetCVMInstance('network interface id')
        if nodename == 'SQL01':
            mvto2a=os.system('python2.6 VMCloud-Migrate-HAIP.py vpc-doy7i4kl 192.168.108.99 eni-4z33qfan eni-onyhdpad')
            os.system('echo 切换到SQL02 成功 >> /var/log/vmclog.log')
        else:
            mvto2b=os.system('python2.6 VMCloud-Migrate-HAIP.py vpc-doy7i4kl 192.168.108.99 eni-onyhdpad eni-4z33qfan')
            os.system('echo 切换到SQL01 成功 >> /var/log/vmclog.log')
    iportrs=NetPortCheck('192.168.108.99',1433)
    print iportrs
    if iportrs == 'NotOk':
        nodename=GetCVMInstance('network interface id')
        if nodename == 'SQL01':
            mvto2a=os.system('python2.6 VMCloud-Migrate-HAIP.py vpc-doy7i4kl 192.168.108.99 eni-4z33qfan eni-onyhdpad')
            os.system('echo 佈~G彍¢佈°SQL02 彈~P佊~_ >> /var/log/vmclog.log')
        else:
            mvto2b=os.system('python2.6 VMCloud-Migrate-HAIP.py vpc-doy7i4kl 192.168.108.99 eni-onyhdpad eni-4z33qfan')
            os.system('echo 佈~G彍¢佈°SQL01 彈~P佊~_ >> /var/log/vmclog.log')
>>>>>>> origin/master
