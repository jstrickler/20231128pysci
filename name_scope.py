
actor = "Ryan Reynolds"  # global variable

def spam():
    animal = "Pine Marten"  #  local variable
    print(f"actor: {actor}")
    return animal    

print(f"actor: {actor}")

x = spam()
print(f"x: {x}")

# print(f"animal: {animal}")
