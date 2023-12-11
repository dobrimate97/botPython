all_values = [] 
with open('account.txt', 'r') as accounts:
    for line in accounts:
        values = line.strip().split(';')
        all_values.extend(values)
for value in all_values:
    print(value)


