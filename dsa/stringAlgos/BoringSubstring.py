def boring_substring(string):
    
    char_set = set(string)
    even_chars = []
    odd_chars = []
    for c in char_set:
        if ord(c) % 2 == 0:
            even_chars.append(c)
        else:
            odd_chars.append(c)
    print(even_chars)
    print(odd_chars)
    if len(even_chars) > 2 or len(odd_chars) > 2:
        return True
    else:
        for char1 in even_chars:
            for char2 in odd_chars:
                if abs(ord(char1) - ord(char2)) != 1:
                    return True
    return False

# Without using set - We just need to find min_even, min_odd, max_even, max_odd
def boring_substring_2(string):
    min_even = 122
    min_odd = 121
    max_even = 98
    max_odd = 97

    for ch in string:
        if ord(ch) % 2 == 0:
            min_even = min(min_even, ord(ch))
            max_even = max(max_even, ord(ch))
        else:
            min_odd = min(min_odd, ord(ch))
            max_odd = max(max_odd, ord(ch))

    if abs(min_even - min_odd) != 1 or abs(min_even - max_odd) != 1:
        return True
    if abs(max_even - min_odd) != 1 or abs(max_even - max_odd) != 1:
        return True
    return False



print(boring_substring_2("aba"))