def vowels_in_string(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

print(vowels_in_string('Deoxyribonucleic'))