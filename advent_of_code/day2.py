
filename = "day2inputs"
with open(filename, "r") as file:
    contents = file.read()

passwords_to_check = contents.splitlines()

# "2-7 p: pbhhzpmppb"
# "5-6 x: xxxxxmxf"
def check_password(policy_and_password):        # Predicate
    policy, password = policy_and_password.split(": ")
    numbers, letter = policy.split(" ")
    minimum, maximum = map(int, numbers.split("-"))
    number_of = password.count(letter)
    if minimum <= number_of <= maximum:
        return True
    else:
        return False


valid = 0
for password in passwords_to_check:
    if check_password(password) == True:
        valid += 1

valid = sum(map(check_password, passwords_to_check))

print("Passwords valid:", valid)
