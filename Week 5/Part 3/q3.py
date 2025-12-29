dict = [
    {"name": "Aashutosh", "age": 19},
    {"name": "Harry", "age": 20},
    {"name": "Carry", "age": 16},
    {"name": "Merry", "age": 17}
]

adultList = []

for detail in dict:
    if detail["age"] > 18:
        adultList.append(detail)

print(adultList)