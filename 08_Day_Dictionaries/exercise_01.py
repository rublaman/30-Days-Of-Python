# Create an empty dictionary called dog
dog = {}
# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Terry'
dog['color'] = 'Black'
dog['breed'] = 'German Shepherd'
dog['legs'] = 4
dog['age'] = 7
print(dog)
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'Ruben',
    'last_name': 'Blanco',
    'gender': 'male',
    'marital_status': 'single',
    'skills': {
        'programming_languages': {'Python', 'JavaScrpit', 'TypeScript'},
        'languages': {'Spanish', 'English'}
    },
    'country': 'Spain',
    'city': 'Leon'
}
# Get the length of the student dictionary
print(len(student))
# Get the value of skills and check the data type, it should be a list
print(student['skills'].values())
# Modify the skills values by adding one or two skills
student['skills']['programming_languages'].add('Java')
print(student['skills']['programming_languages'])
# Get the dictionary keys as a list
print(student.keys())
# Get the dictionary values as a list
print(student.values())
# Change the dictionary to a list of tuples using items() method
print(student.items())
# Delete one of the items in the dictionary
del student['city']
# Delete one of the dictionaries
del student
