import struct
import itertools

def getUBytes(address, length):
  return bytearray([b & 0xff for b in getBytes(address, length)])

def u32(raw_bytes):
  return struct.unpack('<L', raw_bytes)[0]

def read_caml_array(pointer, data_len):
  array = []

  while True:
    try:
      array.append(getUBytes(toAddr(pointer), data_len))
    except:
      break

    pointer = u32(getBytes(toAddr(pointer + 8), 4))

  return array

# The address refers to the argument passed to camlReverse__firstCheck_268.
# For each value, map the bytes to an int, divide by two, and cast to char.
flag_start = b''.join(chr(u32(b) // 2) for b in read_caml_array(0x00160898, 4))

# The address refers to the argument passed to camlReverse__xor_103.
# For each value, map the bytes to an int.
xor_key = [u32(x) for x in read_caml_array(0x001601b0, 4)]

# The address refers to the argument passed to camlReverse__listequal_92.
# For each value, map the bytes to an int.
xor_data = [u32(x) for x in read_caml_array(0x00160208, 4)]

# Xor the key with the data, and divide each value by two before converting it to a char.
flag_end = ''.join(chr((a ^ b) // 2) for a, b in zip(itertools.cycle(xor_key), xor_data))

print(flag_start + flag_end)

