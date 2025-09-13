#define variables
banana_length = 15.5
num_bananas = 5100

#calculate total length in cm
total_length_cm = banana_length * num_bananas

#convert to meters (dividing by 100)
total_length_meters = total_length_cm / 100

print("Total length of", num_bananas, "bananas:", total_length_meters, "meters")

print('Hi there')
print("Hi there")
print("I contain an apostrophe, don't I?")
print('I was told, "Double quotes go inside single quotes!"')

s = 'hi mom'
longstr = """As I was going to St. Ives,
I met a man with seven wives.
Each wife had seven sacks,
Each sack had seven cats,
Each cat had seven kits.
Kits, cats, sacks, and wives:
How many were going to St. Ives?"""

print("s =", s)
print("longstr =", longstr)

#test string operations
print("Length of 'foo':", len('foo'))
print("Concatenation:", 'foo' + 'bar')
print("Repetition:", 'foo' * 3)
print("'mom' in s:", 'mom' in s)
print("Character at s[3]:", s[2])
print("Slice s[3:5]:", s[0:5])

#test these predictions:
print("Length of longstr:", len(longstr))
print("'kits' in longstr:", 'kits' in longstr)
print("longstr[36:39]:", longstr[36:39])