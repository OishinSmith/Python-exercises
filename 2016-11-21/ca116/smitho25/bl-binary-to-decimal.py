import sys
binary = sys.argv[1]


i = 0
while i < len(binary):
  exponent = binary[i]
  binary[i] = binary[len(binary) - i - 1]
  binary[len(binary) - i - 1] = exponent
  i = i + 1
  print binary
  """decimal = 0
  if i < len(binary):
    decimal = decimal + (int(binary[i]) * (2 ** i))
  i = i + 1

print decimal"""
