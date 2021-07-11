import string
from pwn import *

context.log_level = 'ERROR'

def service(inp):
    r = remote('144.217.73.235', 29292)
    prompt = r.recvuntil(': ')
    r.sendline(inp)
    output = r.recvall()
    r.close()
    return output

known = b""

while not known.endswith(b'}'):
    # One char short
    l = 64 - 1 - len(known)
    target = service(b'0' * l)[:64]

    for b in string.printable.encode():
        b = bytes([b])
        block = service(known.zfill(64 - 1) + b)[:64]

        if target == block:
            print(b.decode(), end='')
            known += b
            break
    else:
        print()
        break

