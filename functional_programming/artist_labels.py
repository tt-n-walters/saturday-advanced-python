
# Label format
#   F = First letter of a first name, in uppercase
#   L = Letters of last name, up to 5 in length, in uppcase
#   N = Nationality, first letter uppercase
#   XX = Age at death
#      FFFFLLLLL-NXX

import csv


filename = "artists.tsv"
file = open(filename, "r")
parsed_data = csv.reader(file, dialect="excel-tab")

labels = []

data_names = next(parsed_data)
for row in parsed_data:
    name, birth, death, nationality = row

    try:
        age = int(death) - int(birth)
    except ValueError:
        age = 2020 - int(birth)

    names = name.split(" ")
    all_names = []
    for f_name in names:
        all_names.extend(f_name.split("-"))
    
    last = all_names[-1]
    firsts = all_names[:-1]
    
    letters = ""
    for first in firsts:
        letters += first[0]
    
    if len(last) >= 5:
        letters += last[0:5]
    else:
        letters += last

    label = letters + "-" + nationality[0] + str(age)
    label = label.upper()

    if age >= 60:
        labels.append(label)


print(labels)
