import sys
import re

def encrypt(input, rounds, roundkeys):
    
    def and_gate(fir_str, sec_str):
        fn = ''
        for item,val in enumerate(fir_str):
            if val == sec_str[item] == '1':
                fn += '1'
            else:
                fn += '0'       
        return fn

    def xor(fir_str,sec_str):
        fn = ''
        for item,val in enumerate(fir_str):
            if val == sec_str[item]:
                fn += '0'
            else:
                fn += '1'
        return fn
    
    counter = 0

    for roundkey in roundkeys:
        counter += 1
        left_bit = input[:4]
        right_bit = input[4:]
        
        left_bit = xor(and_gate(right_bit,roundkey),left_bit)
        input = right_bit+left_bit
        
        if rounds == counter:
            input = left_bit+right_bit
    return input


def decrypt(input, rounds, roundkeys):
    roundkeys = roundkeys[::-1]
    
    return encrypt(input, rounds, roundkeys)


opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

c = re.compile('^[01]{8}$')
try:
    input=args.pop(0)
except IndexError:
    raise SystemExit("Usage: {sys.argv[0]} [-d] input rounds roundkey1 roundkey2 ...")
if not c.search(input):
    raise SystemExit("input is not a valid bit string")

try:
    rounds=int(args.pop(0))
except IndexError:
    raise SystemExit("Usage: {sys.argv[0]} [-d] input rounds roundkey1 roundkey2 ...")
except ValueError:
    raise SystemExit("rounds is not a valid number")

if(len(args)<rounds):
    raise SystemExit("Usage: {sys.argv[0]} [-d] input rounds roundkey1 roundkey2 ...")

roundkeys=args
c = re.compile('^[01]{4}$')
if not all(c.search(elem) for elem in roundkeys):
    raise SystemExit("round key is not a valid bit string")

if "-d" in opts:
    result = decrypt(input,rounds,roundkeys)
else:
    result = encrypt(input,rounds,roundkeys)

print (result)

