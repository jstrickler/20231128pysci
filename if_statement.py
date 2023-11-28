value = 42

if value > 75:
    print("koala")
    print("kangaroo")
elif value > 50:  # else if
    print("wallaby")
    print("wombat")
else:
    print('quokka')
    print('platypus')

print("ALL DONE")

# if elif else while for def class with try except finally 

# if X is a number: 
#      0 is False, non-0 is True
# if X has a length: list, dict, tuple, str, set, bytes 
#      len(X) == 0 is False, otherwise true
# Also false:  False, None
# Also true: True

debug = True

#  C/Java/C# etc:   color = debug?'red':'green'
color = 'red' if debug else 'green'
print(f"color: {color}")

if debug:
    color = 'red'
else:
    color = 'green'

#  == != > < >= <=


#   x and y   true only if x AND y are true
#   a or b    true if either a OR b are true (or both) -- false only if both a AND b are false
#  not j
