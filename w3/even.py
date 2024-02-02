def even(integer):
    even_arr = []
    for i in range(1, integer):
        if i % 2 == 0:
            even_arr.append(i)
    return even_arr


print(even(50))
