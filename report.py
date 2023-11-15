def print_report(expenditures):
    print('-'*13)
    print('Report for your monthly expenditure')
    for expenditure in expenditures:
        print('Item\t Frequency\t Monthly Expenditure')
        print('-'*36)
        print(f"{expenditure['name']}\t {expenditure['frequency']}\t {expenditure['cash_spent']}")