def sum_digits(integer):
    integer = str(integer)
    length =  len(integer)
    if length == 1:
        return integer
    else:
        sumatory = 0
        for i in range(length):
            sumatory += int(integer[i])
        return sumatory

print(sum_digits(14892))