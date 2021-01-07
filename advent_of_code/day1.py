import itertools

filename = "day1inputs"
with open(filename, "r") as file:
    contents = file.read()

lines = contents.splitlines()
expenses = []
for number in lines:
    expenses.append(int(number))

combinations = list(itertools.combinations(expenses, 3))
for number_a, number_b, number_c in combinations:
    if number_a + number_b + number_c == 2020:
        print("Found:", number_a, number_b, number_c)
        print("Product:", number_a * number_b * number_c)

# expenses = expenses[:25]
# for number_a in expenses:
#     for number_b in expenses:
#         print(number_a, number_b)
#         if number_a + number_b == 2020:
#             print("Found:", number_a, number_b)
#             print("Product:", number_a * number_b)


# for x in range(10):
#     for y in range(10):
#         print(x, y)

# print(list(itertools.product(range(10), range(10))))