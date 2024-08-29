def count_letter_a(string):
    count = string.lower().count('a')
    return count

test_string = "Abracadabra"


count = count_letter_a(test_string)
print(f"A letra 'a' aparece {count} vezes na string '{test_string}'.")
