


def get_frequency_and_spend(item_of_expenditure):
        daily_exp = "daily"
        weekly_exp = "weekly"
        monthly_exp = "monthly"
        
        while True:
            frequency_of_spend = input(f"How often do you spend money on {item_of_expenditure}.\n\tEnter:\n\tD for daily\n\tM for monthly\n\tW for weekly:\n").lower()
            
            if frequency_of_spend == 'd':
                money_spent = int(input(f"How much do you spend on {item_of_expenditure} {daily_exp} ?:\n"))
                return frequency_of_spend,money_spent
            elif frequency_of_spend == 'w':
                money_spent = int(input(f"How much do you spend on {item_of_expenditure} {weekly_exp} ?:\n"))
                return frequency_of_spend,money_spent
            elif frequency_of_spend == 'm':
                money_spent = int(input(f"How much do you spend on {item_of_expenditure} {monthly_exp} ?:\n"))
                return frequency_of_spend,money_spent
            else:
                print("\nInvalid answer")
                print("Please enter one of the provided options\n")
                continue

def get_input():
    list_of_expenditures = []
    #the first time the program is run
    i = 0

    while True:
        if i==0:
            add_item = 'y'
        else:

            #does the user want to end the session
            add_item = input("\nEnter Another Item?\n [Y=Yes] [N=No]: ").lower()

        #does the user have another add_item?
        if  add_item == 'y' or add_item == 'yes':
            expenditure = {}
            item_of_expenditure = input("\nEnter item of expenditure (something you spend money on):\n")
            frequency_of_spend,money_spent = get_frequency_and_spend(item_of_expenditure)
            #store these expenditures in a dictionary
            expenditure['name'] = item_of_expenditure
            expenditure['frequency'] = frequency_of_spend
            expenditure['cash_spent'] = money_spent
            list_of_expenditures.append(expenditure)
            i += 1
        elif add_item == 'n' or add_item == 'no':
            break
        else:
            print("\nInvalid input.")
            continue
    return list_of_expenditures