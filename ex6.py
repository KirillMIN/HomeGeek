
subj = {}
with open('test.txt', 'r') as file_n:
    for line in file_n:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {subj}')
