# Turimas "users" masyvas.

# Parašykite funkcijas, kurios atlikas nurodytas užduotis:
# 1. funkcija "filter_dog_owners" - kaip argumentą priims masyvą ir duoto masyvo
# atveju grąžins "users", kurie turi augintinį.
# 2. funkcija "filter_adults" - kaip argumentą priims masyvą ir duoto masyvo
# atveju grąžins masyvą su "users", kurie yra pilnamečiai.

users = [
    {"id": '1', "name": 'John Smith', "age": 20, "hasDog": True},
    {"id": '2', "name": 'Ann Smith', "age": 24, "hasDog": False},
    {"id": '3', "name": 'Tom Jones', "age": 31, "hasDog": True},
    {"id": '4', "name": 'Rose Peterson', "age": 17, "hasDog": False},
    {"id": '5', "name": 'Alex John', "age": 25, "hasDog": True},
    {"id": '6', "name": 'Ronald Jones', "age": 63, "hasDog": True},
    {"id": '7', "name": 'Elton Smith', "age": 16, "hasDog": True},
    {"id": '8', "name": 'Simon Peterson', "age": 30, "hasDog": False},
    {"id": '9', "name": 'Daniel Cane', "age": 51, "hasDog": True},
]

# 1. funkcija "filter_dog_owners" - kaip argumentą priims masyvą ir duoto masyvo
# atveju grąžins "users", kurie turi augintinį.


def filter_dog_owners(masyvas):
    hasDog = []
    for user in masyvas:
        if user['hasDog']:
            hasDog.append(user)
    return hasDog


print(filter_dog_owners(users))

# 2. funkcija "filter_adults" - kaip argumentą priims masyvą ir duoto masyvo
# atveju grąžins masyvą su "users", kurie yra pilnamečiai.


def filter_adults(masyvas):
    adults = []
    for user in masyvas:
        if user['age'] >= 18:
            adults.append(user)
    return adults


print(filter_adults(users))
