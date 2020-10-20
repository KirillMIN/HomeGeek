my_file = open('file.txt', 'r')
content = my_file.readlines()
print(f'amount of str in file : {len(content)}')
number = 1
for line in content:
    print(f' amount of words in {number} str: {len(line.split())}')
    number += 1



