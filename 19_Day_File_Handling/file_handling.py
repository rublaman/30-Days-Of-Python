'''
Opening, writing and deleting files
'''
import os

with open('./files/reading_file_example.txt', 'a') as f:
    f.write('This text has to be appended at the end')

with open('./files/writing_file_example.txt', 'w') as f:
    f.write('This text will be written in a newly created file')


if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')
