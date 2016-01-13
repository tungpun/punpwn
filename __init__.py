import pwn
from termcolor import colored

class PunPwn():
    def __init__(self, host, port):        
        print colored('>> Happy pwning !', 'cyan')
        self.conn = pwn.remote(host, port)


    def sent(self, s):
        self.conn.sendline(s)
        print colored('[+] Sent: ' + s, 'yellow')


    def recvall(self):
        print colored(self.conn.recvall(), 'green', 'on_grey')
        
    
    def recvuntil(self, s):
        print colored(self.conn.recvuntil(s), 'green', 'on_grey')


    def interactive(self):
        self.conn.interactive()


if __name__ == '__main__':    
    print colored('>> Happy pwning !', 'cyan')