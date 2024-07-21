# Feistel Structure Cryptography

## Program Description

This Python script implements a simple encryption and decryption algorithm using bitwise operations. It can encrypt or decrypt an 8-bit input string using a specified number of rounds and round keys.

## Usage

```
python script_name.py [-d] input rounds roundkey1 roundkey2 ...
```

- `-d`: Optional flag for decryption mode
- `input`: 8-bit string to encrypt/decrypt
- `rounds`: Number of encryption/decryption rounds
- `roundkey1`, `roundkey2`, ...: 4-bit round keys (one for each round)

## Key Components

### Main Functions

1. `encrypt(input, rounds, roundkeys)`: Encrypts the input
2. `decrypt(input, rounds, roundkeys)`: Decrypts the input (uses `encrypt` with reversed round keys)

### Helper Functions

1. `and_gate(fir_str, sec_str)`: Performs bitwise AND operation
2. `xor(fir_str, sec_str)`: Performs bitwise XOR operation

### Input Validation

- Checks for correct number of arguments
- Validates input as an 8-bit string
- Ensures `rounds` is a valid number
- Verifies each round key is a 4-bit string

## Algorithm Overview

1. Split input into left and right halves (4 bits each)
2. For each round:
   - Apply AND operation between right half and round key
   - XOR the result with the left half
   - Swap left and right halves (except for the last round)
3. Concatenate final left and right halves

## Decryption Process

Decryption uses the same algorithm as encryption but with the round keys applied in reverse order.

## Error Handling

The script includes error messages for:
- Incorrect usage
- Invalid input format
- Invalid number of rounds
- Insufficient round keys
- Invalid round key format

## Notes and Potential Improvements

1. The encryption method is a simplified version of a Feistel network
2. Consider adding more robust input validation and error handling
3. Potential for performance optimization for larger inputs
4. Could be extended to support variable input sizes and key lengths

