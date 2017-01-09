my_family = { 'sister': {'name': 'Jane', 'age': str(35)}, 'mother': {'name': 'Junghee', 'age': str(68)}}

my_sister = my_family['sister']
my_mother = my_family['mother']
print(my_sister)
print(my_sister['name'] + " is my sister and " )
print(my_sister['age'] + " years old")

my_sister = { "my sister's " + key  + " is " + value  for (key, value) in my_sister.items() }
my_mother = { "my mother's " + key + " is " + value for (key, value) in my_mother.items()}
print(my_sister)
print(my_mother)