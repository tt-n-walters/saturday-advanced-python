#          *  (asterisk)     **
#  Multiplication/Exponentiation


tuple

# a = 1
(a, b) = (1, 2)
a, b = 1, 2
print(type(a), a)
print(type(b), b)
a, b = b, a
print(a, b)

# Packing
a, b, *c, d = 1,2,3,4,5
print(a)
print(b)
print(c)
print(d)

d = [7, 8, 9]
a, b, c = d

#Unpacking

d = {"c": 9, "a":7, "b":8}

def f(b, a, c=99):
    print(a, b, c)

f(**d)

import copy



# Mutable unpacking

my_list = [4,5,78,65,4,5,674]

my_list += [None]
*copy_of, _ = my_list
my_list.pop()
# copy_of = [*my_list]

copy_of = [x for x in my_list]
copy_of = []
for x in my_list:
    copy_of.append(x)

copy_of[2] += 10

print(my_list)
print(copy_of)


bob = {"name": "Bob", "age": 42}
new_bob = {**bob}

new_bob["age"] += 1

print(bob)
print(new_bob)
