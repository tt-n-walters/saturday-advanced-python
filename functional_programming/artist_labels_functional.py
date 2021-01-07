import csv
import operator
from functools import reduce


def open_file(filename):
    return open(filename, "r")


def create_tsv_reader(file):
    return csv.reader(file, dialect="excel-tab")


def replace_hyphens(string):
    if string == "-":
        return "2020"
    else:
        return string
    # return "2020" if string == "-" else string


# predicate function to keep the years in the data
def check_numbers(value):
    return value.isdigit()


def reverse(a, b):
    return b, a
    

def calculate_age(artist):
    a = map(replace_hyphens, artist)
    b = filter(check_numbers, a)
    c = map(int, b)
    d = reverse(*c)
    e = reduce(operator.sub, d)
    return e



def get_nationality(artist):
    return artist[3]


def get_first(value):
    return value[0]


def apply(function, value):
    return function(value)


artists = create_tsv_reader(open_file("artists.tsv"))
column_names = next(artists)
ages = map(calculate_age, artists)


artists = create_tsv_reader(open_file("artists.tsv"))
column_names = next(artists)
nationalities = map(get_nationality, artists)
letters = map(get_first, nationalities)
letters = map(str.upper, letters)

labels = map(operator.add, *zip(map(str, ages), letters))
for label in labels:
    print(label)

print(ages)



# currying    -> partial functions