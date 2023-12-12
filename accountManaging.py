account_data = [] 
with open('account.txt', 'r') as accounts:
    for line in accounts:
        values = line.strip().split(';')
        account_data.extend(values)



