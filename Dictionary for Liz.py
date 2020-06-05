# Python Dictionary
python_dict = {
    'key1' : 'value1',
    'key2' : 'value2',
}

# A few Dictionary Methods
# .get()
print(python_dict.get('key1'))

# .update()
print(python_dict.update({'key3' : 'value3'}))
print(python_dict)

# Dictionary -> Creating a dictionary but the more cool way, AKA the one line
students = ['Elizabeth', 'Elizabeast', 'Beast'] # Keys
age = [21, 22, 23] # Values
students_ages = {key : value for key, value in zip(students, age)}
print(students_ages)

