print("Write your own list:")
vowels = input()
print("Your newest list:\n" + ''.join(letter for letter in vowels if letter in 'AaIiOoUuYyEe')[:-1])