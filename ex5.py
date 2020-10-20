def summary():
    with open('file.txt', 'w') as file_obj:
        line = input('Enter the numbers space-separated:')
        file_obj.writelines(line)
        numb = line.split()
        print(sum(map(int, numb)))


summary()
