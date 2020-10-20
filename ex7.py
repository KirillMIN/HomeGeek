import json
profit_in_company = {}
profit_in_dict = {}
prof = 0
prof_aver = 0
i = 0
with open('file.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit_in_company[name] = int(earning) - int(damage)
        if profit_in_company.setdefault(name) >= 0:
            prof = prof + profit_in_company.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует')
    profit_in_dict = {'средняя прибыль': round(prof_aver)}
    profit_in_company.update(profit_in_dict)
    print(f'Прибыль каждой компании - {profit_in_company}')

with open('file.json', 'w') as write_js:
    json.dump(profit_in_company, write_js)

    js_str = json.dumps(profit_in_company)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')