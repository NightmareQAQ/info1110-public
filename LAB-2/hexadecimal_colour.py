line = input('Enter the colour value: ')
value = int(line, 16)  # read user input as a hexadecimal number, and convert to an integer
red = (value & 0xFF0000) >> 16  # & = bitwise AND operator, >> = bitwise right shift operator
print(red)