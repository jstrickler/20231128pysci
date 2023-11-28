import sys     #  get access to sys module

#  sys.argv  

print(f"sys.argv: {sys.argv}")

print(f"sys.argv[0]: {sys.argv[0]}")
print(f"sys.argv[1]: {sys.argv[1]}")

value = float(sys.argv[1])
print(value * 10)
