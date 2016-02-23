#!/usr/bin/python 2.7
# 
# punpwn
# A wrapper of pwntool with termcolor support for personal purpose
#
# https://github.com/tungpun/punpwn
#
# Author: tungpun_
#

import pwn

from termcolor import colored

def help():
    function = """
    [---------------------- Static ----------------------]

    [+] p64(h) 
    [+] u32(b) 
    [+] u64(b) 
    [+] xxw32(payload)
    [+] xxw64(payload)
    [+] embed(sub, big)
    """
    behavior = """
    [-------------------- PunPwn obj --------------------]

    [+] __init__(self, host, port)
    [+] __init__(self, process_addr)
    [+] sent(self, s)
    [+] recv(self, size) 
    [+] recv_h(self, size) 
    [+] recvall(self) 
    [+] recvall_h(self) 
    [+] recvuntil(self, s) 
    [+] recvuntil_h(self, s) 
    [+] interactive(self) 
    """    
    print colored(function, 'magenta')    
    print colored(behavior, 'cyan')    

def p32(h):
    return pwn.p32(h)

def p64(h):
    return pwn.p64(h)

def u32(b):
    return pwn.u32(b)

def u64(h):
    return pwn.u64(h)

def xxw32(payload):    
    # Padding
    while len(payload) % 4 != 0:
        payload += '\x00'

    buffer = ''
    for i in xrange(0, len(payload), 4):                
        block = hex(u32(payload[i:i+4]))            
        buffer += ('\n0x%0.4x | %s' % (i, block))        
    print colored(buffer, 'magenta')

def xxw64(payload):    
    # Padding
    while len(payload) % 8 != 0:
        payload += '\x00'

    buffer = ''
    for i in xrange(0, len(payload), 8):                
        block = hex(u64(payload[i:i+8]))            
        buffer += ('\n0x%0.4x | %s' % (i, block))        
    print colored(buffer, 'magenta')

def embed(sub, big):    
    big = sub + big[len(sub):]
    return big

class PunPwn():
    def __init__(self, host, port):        
        print colored('>> Happy pwning !', 'cyan')
        self.conn = pwn.remote(host, port)


    def __init__(self, pdir):        
        print colored('>> Happy pwning !', 'cyan')
        self.conn = pwn.process(pdir)


    def sent(self, s):
        s = str(s)
        self.conn.sendline(s)
        print colored('[+] Sent (' + str(len(s)) + ' bytes) : ' + s, 'yellow')


    def recv(self, size):
        data = self.conn.recv(size)
        print colored(data, 'green', 'on_grey')
        return data

    def recv_h(self, size):
        data = self.conn.recv(size)
        print colored(data.encode('hex'), 'green', 'on_grey')
        return data


    def recvall(self):
        data = self.conn.recvall()
        print colored(data, 'green', 'on_grey')
        return data
    

    def recvall_h(self):
        data = self.conn.recvall()
        print colored(data.encode('hex'), 'green', 'on_grey')
        return data
    

    def recvuntil(self, s):
        data = self.conn.recvuntil(s)
        print colored(data, 'green', 'on_grey')
        return data


    def recvuntil_h(self, s):
        data = self.conn.recvuntil(s)
        print colored(data.encode('hex'), 'green', 'on_grey')
        return data


    def interactive(self):
        self.conn.interactive()


if __name__ == '__main__':    
    print colored('>> Happy pwning !', 'cyan')