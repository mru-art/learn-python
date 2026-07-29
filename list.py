lst = []
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
f_fruit = fruits[0]
print(f_fruit)  # Output: apple
s_fruit = fruits[1]
print(s_fruit)  # Output: banana

# accessing elements using negative indexing
l_fruit = fruits[-1]
print(l_fruit)  # Output: elderberry
sl_fruit = fruits[-2]
print(sl_fruit)  # Output: date

# unpacking the list items
countries = ["Lithuania", "Latvia", "Estonia", "Norway", "Finland", "Sweden"]
li, la, es, *rest = countries
print(li)  # Output: Lithuania
print(la)  # Output: Latvia
print(es)  # Output: Estonia
print(rest)  # Output: ['Norway', 'Finland', 'Sweden']
