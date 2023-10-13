print("Write your own list:")
vowels = input()
vowels = ''.join(letter for letter in vowels if letter in 'AaIiOoUuYyEe')[:-1]
print("Your newest list:\n"+ vowels)