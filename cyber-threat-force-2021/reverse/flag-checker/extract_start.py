import string

alphabet = (
    '_' +
    string.ascii_lowercase +
    string.ascii_uppercase +
    string.digits +
    string.punctuation
)

found = ''
running = True

while running:
    for char in alphabet:
        # To avoid substitution errors, skip '.
        if char == "'":
            continue

        print(found + char)

        # Run the program.
        gdb.execute("r '" + found + char + "'")

        # Skip over the first N chars we already found.
        if len(found) > 0:
            gdb.execute('continue ' + str(len(found)))

        # Get the values of the registers.
        try:
            rdi = int(gdb.parse_and_eval("$rdi"))
            rsi = int(gdb.parse_and_eval("$rsi"))
        except:
            running = False
            break

        if rdi == rsi:
            found += char
            break
    else:
        break

print('=>', found)

