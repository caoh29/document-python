def reverse_str(string):
    length = len(string)
    if length == 0:
        return string
    else:
        return string[-1:-length-1:-1]

print(reverse_str("camilo"))