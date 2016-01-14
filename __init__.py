import pwn
from termcolor import colored

def p32(h):
    return pwn.p32(h)

def p64(h):
    return pwn.p64(h)

class PunPwn():
    def __init__(self, host, port):        
        print colored('>> Happy pwning !', 'cyan')
        self.conn = pwn.remote(host, port)


    def sent(self, s):
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