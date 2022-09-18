# Here we have a person dictionary. Feel free to modify it!

person = {
    'first_name': 'Ruben',
    'last_name': 'Blanco',
    'age': 29,
    'country': 'Spain',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if person['skills']:
    print(person['skills'][len(person['skills']) // 2])
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if person['skills'] and 'Python' in person['skills']:
    print('THe person has Python skill')
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if 'JavaScript' in person['skills'] and 'React' in person['skills'] and len(person['skills']) == 2:
    print('He is a front end developer')
elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills'] and len(person['skills']) == 3:
    print('He is a backend developer')
elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills'] and len(person['skills']) == 3:
    print('He is a fullstack developer')
else:
    print('Unknown twitle')
    #  * If the person is single and if he lives in Spain, print the information in the following format:
    #     Ruben Blanco lives in Spain. He is single.
if person['first_name'] == 'Ruben' and person['last_name'] == 'Blanco' and person['is_married'] == False:
    print('Ruben Blanco lives in Spain. He is single')
