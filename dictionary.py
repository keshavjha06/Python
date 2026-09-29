# Dictionary is a collection of key-value pairs
person = {
    "name": "John",
    "age": 25,
    "city": "New York"
}
print(person["name"]) # John
print(person["age"]) # 25
print(person["city"]) # New York

# Dictionary methods
print(person.keys()) # dict_keys(['name', 'age', 'city'])
print(person.values()) # dict_values(['John', 25, 'New York'])
print(person.items()) # dict_items([('name', 'John'), ('age', 25), ('city', 'New York')])

dict = {}
dict["name"] = "John"
dict["age"] = 25
dict["city"] = "New York"
print(dict.get("name")) # John
print(dict) # {'name': 'John', 'age': 25, 'city': 'New York'}