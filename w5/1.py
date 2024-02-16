def count_vowels_and_consonants(input_string):
    input_string = input_string.lower()  # Convert to lowercase to ignore case
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0
    
    for char in input_string:
        if char.isalpha():  # Check if the character is an alphabet
            if char in vowels: # Check if the character is a vowel
                vowel_count += 1 # Add 1 to the vowel count if the character is a vowel
            else:
                consonant_count += 1 # Add 1 to the consonants count if the character is a consonant
    
    return vowel_count, consonant_count


input_string = input("Enter a string: ") # Asks for a string to user
vowels, consonants = count_vowels_and_consonants(input_string) # Calls the function to count vowels and consonants, and assigns its return value to vowels and consonants
print("Number of vowels:", vowels) # Prints the number of vowels found in the string
print("Number of consonants:", consonants) # Prints the number of consonants found in the string
