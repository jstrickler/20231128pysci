def hello():
    print("Hello, world")

hello()

def get_message():
    return "Howdy, Earth!"

m = get_message()
print(f"m: {m}")
print(get_message())

#        positional parameter  (required)
def greet(greetee: str="world") -> None:  # args are copied to parameters (by reference)
    print(f"Greetings, {greetee}")

greet('world')  # passing args
greet('students')
greet('Mom')
greet()
# greet(1.234)

x = greet('Ryan Reynolds')
# print(x + 5)

