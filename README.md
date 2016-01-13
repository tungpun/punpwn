# punpwn
A wrapper of `pwntool` with `termcolor` support for personal purpose

## Requirements
* python 2.7 on Linux (tested) / MacOS
* python modules: `pwntool`, `termcolor`

## Install
```
cd /usr/local/lib/python2.7/dist-packages/ & git clone git@github.com:tungpun/punpwn.git
```

## Example
```
#!/usr/bin/python 2.7
from punpwn import *

pp = PunPwn(host='127.0.0.1', port=2323)
pp.recvuntil(':')
pp.sent('Joe')
pp.recvall()
pp.interactive()
```
