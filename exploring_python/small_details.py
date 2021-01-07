
# Mutability
# The in-place (in-situ) changing of data.

# lists are mutable
numbers = [6, 7, 8, 9, 10]
print(hex(id(numbers)))

numbers2 = numbers
print(hex(id(numbers2)))
numbers2[3] = 0

print(numbers)
print(numbers2)


# strings are immutable
string = "hello world"
string2 = string
string2 = string2 + "!"

print("numbers2 =", numbers2, hex(id(numbers2)))
print("numbers =", numbers, hex(id(numbers)))
print("string2 =", string2, hex(id(string2)))
print("string =", string, hex(id(string)))


# Affect 1
numbers[4] = 100
print(numbers)

# string[8] = "R"
# print(string[8])



sentence = "Python is wonderful"
letters = list(sentence)

ordered_letters = sorted(letters)     # immutable instruction
print("IMM letters = ", letters)
print("IMM ordered_letters = ", ordered_letters)

letters.sort()      # mutable instruction
print("MUT letters = ", letters)



from functools import partial
# Bit(wise) manipulation
# Bit 0/1   Bytes 10101101
binary = partial(int, base=2)

print(binary("101101011"))
print(bin(124))

#  arithmetic operators:  + - * /
#  bitwise operators:     | ^ & << >> ~

a = 3 & 12  # & bitwise AND
b = 8 ^ 12  # ^ bitwise XOR
c = 4 | 15  # | bitwise OR
print(type(a), a)
print(type(b), b)
print(type(c), c)
                # 1 = Shift
                # 2 = Ctrl
                # 4 = Alt
                # 8 = Function
                #  8421
modifiers = 7   #  1001
shift = 1
ctrl = 2
alt = 4
fn = 8

if modifiers & shift:
    print("Shift pressed!")
if modifiers & ctrl:
    print("ctrl pressed!")
if modifiers & alt:
    print("alt pressed!")
if modifiers & fn:
    print("fn pressed!")



# A-typical slicing
print("\n\n\n\n")

string = "python-advanced-saturday"
x = slice(7, 18, 2)
print(string[x])

get = partial(slice, 7)
for i in range(10):
    print(string[get(i + 7)])



# String literals

str(10)   # string object
a = "10"      # string literal
b = '10'
c = '''10       
11'''       # replace newlines with a newline character  (\n)
print(a, b, c)

a = f"Hello world!"     # formatted
b = r"Hello world!"     # raw
c = r"D:\TechTalents\Classes\Active\nico\python-advanced-saturday\small_details.py"
print(a)
print(b)
print(c)

n = 56.32464323
print(f"a = {a}")
print(f"{a = }")
print("a = {}".format(a))



# Views / Lenses
bob = { "name": "Bob", "job": "Builder" }


keys = bob.keys()
values = bob.values()
items = bob.items()

print("Before")
print(keys)
print(values)
print(items)

bob["age"] = 42
bob2 = bob
bob2["height"] = 140

print("After")
print(keys)
print(values)
print(items)