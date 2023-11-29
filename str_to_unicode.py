QUOTE = '"'

def str_to_unicode(s):
    chars = []
    for ch in s:
        ord_of_ch = ord(ch)
        if ord_of_ch < 128: # normal ASCII range
            chars.append(ch)
        else:
            if ord_of_ch > 0xFFFF: #  needs \U
                chars.append(f"\\U{ord_of_ch:08x}")
            else:   # \u OK
                chars.append(f"\\u{ord_of_ch:04x}")
    return QUOTE + ''.join(chars) + QUOTE


if __name__ == "__main__":
    s = "39\u00b0\U0001F414"
    print(f"s: {s}")
    print(f"repr(s): {repr(s)}")
    
    print(f"str_to_unicode(s): {str_to_unicode(s)}")
    
    x = "abc"
    print(f"x: {x}")
    print(f"str_to_unicode(x): {str_to_unicode(x)}")
    