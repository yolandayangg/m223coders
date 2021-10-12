dict_person = { "name":"Joe", "age":61, "city":"San Diego"}

print(dict_person['name'])
print(dict_person.get['name'])
print("Keys: ")
for key in dict_person:
    print(key)

print("Function Keys(): ")
for key in dict_person.keys():
    print(key)

print("Values: ")
for value in dict_person:
    print(dict_person[value])

print("Function Values(): ")
for value in dict_person.values():
    print(value)

print("Function Items(tuple): ")
for pair in dict_person.items():
    print(pair)


p1 = { "name":"John", "age":61, "city":"Eugene"}
p2 = { "name":"Risa", "age":16, "city":"New York"}
p3 = { "name":"Ryan", "age":16, "city":"Los Angeles"}
p4 = { "name":"Shekar", "age":16, "city":"San Francisco"}
# a list of dictionaries
list_of_people = [p1, p2, p3, p4]
# write some code to Print List of people one by one


# turn list to dictionary of people
dict_people = {'people': list_of_people}
print("List to Dictionary of people")
print(type(dict_people))
print(dict_people)
# write some code to Print People from Dictionary