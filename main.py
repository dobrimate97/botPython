with open('account.txt', 'r') as accounts:
    for line in accounts:
        values = line.strip().split(';')
for value in values:
    print(value)
