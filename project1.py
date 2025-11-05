import datetime

def Add():

    expense_amt = float(input("Enter Amount:  "))
    expense_des = input("Enter Description:  ")
    expense_cat = input("Enter Category:  ")

    today = datetime.date.today().strftime("%Y-%m-%d")

    custom_date = input(f"Enter Date (YYYY-MM-DD) or press Enter for today [{today}]: ").strip()
    if custom_date == "":
        expense_date = today
    else:
        expense_date = custom_date

    with open("expensetracker.txt", "a") as file:
        file.write(f"{expense_amt} | {expense_des} | {expense_cat} | {expense_date}\n")
    
    print("Entry Saved.....")


def View():
    
    try:
        with open("expensetracker.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("No Entries Yet!!!")
            else:
                print("-----Your Expenses" + "-"*32)
                print(f"{'Index':>6} {'Amount':>10} {'Description':>20} {'Category':>15} {'Date':>12}")
                print("-"*50)
                total = 0
                for num, line in enumerate(lines, start=1):
                    parts = line.strip().split("|")
                    if len(parts) == 3:
                        date_str = "No Date"
                    else:
                        date_str = parts[3].strip()
                    amount = float(parts[0].strip())
                    total += amount
                    print(f"{num:>3} {parts[0].strip():>10} {parts[1].strip():>20} {parts[2].strip():>15} {date_str:>12}")
                print("-"*50)
                print(f"{'Total':>10} {total:>20.2f}")
                print("-"*50)

    except FileNotFoundError:
        print("No Entries Yet!!!")


def filterexpenses():

    filterby = int(input("Do you want to filter by? : \n1. Date\n2. Category  \n"))

    if filterby == 1:

        bydate = input("Enter Date(YYYY-MM-DD): ")

        try:
            with open("expensetracker.txt", "r") as file:
                found = False
                lines = file.readlines()
                if not lines:
                    print("No Entries Yet!!!")
                    return
                print("-----Your Expenses" + "-"*32)
                print(f"{'Amount':>10} {'Description':>20} {'Category':>15} {'Date':>12}")
                print("-"*50)
                for line in lines:
                    parts = line.strip().split("|")
                    if len(parts) < 4:
                        date = "No Date"
                    else:
                        date = parts[3].strip()
                    if date == bydate:
                        found = True
                        print(f"{parts[0].strip():>10} {parts[1].strip():>20} {parts[2].strip():>15} {date:>12}")
                print("-"*50)

                if found == False:
                        print("No expenses found on this date.")
        except FileNotFoundError:
            print("No Entries Yet!!!")
            return
                    

    elif filterby == 2:

        cat = input("Enter category to filter: ").lower()

        try:
            with open("expensetracker.txt", "r") as file:
                found = False
                lines = file.readlines()
                if not lines:
                    print("No Entries Yet!!!")
                    return
                print("-----Your Expenses" + "-"*32)
                print(f"{'Amount':>10} {'Description':>20} {'Category':>15} {'Date':>12}")
                print("-"*50)
                for line in lines:
                    parts = line.strip().split("|")
                    category = parts[2].strip()
                    if len(parts) < 4:
                        date = "No Date"
                    else:
                        date = parts[3].strip()
                    if category.lower() == cat:
                        found = True
                        print(f"{parts[0].strip():>10} {parts[1].strip():>20} {parts[2].strip():>15} {date:>12}")
                print("-"*50)
                if found == False:
                    print("No expenses found in this category.")
        except FileNotFoundError:
            print("No Entries Yet!!!")
            return


def viewtotalsbycategory():

    try:
        with open("expensetracker.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("No Entries Yet!!!")
                return
            totals = {}
            for line in lines:
                parts = line.strip().split("|")
                category = parts[2].strip().title()
                amount = float(parts[0])
                if category in totals:
                    totals[category] += amount
                else:
                    totals[category] = amount
            print("-"*50)
            for category, amount in totals.items():
                print(f"{category:<15} --> {amount:>10.2f}")
            print("-"*50)
    except FileNotFoundError:
        print("No Entries Yet!!!")

def deleteexpenses():

    num_delete = int(input("Which number do you want to delete?  "))

    try:
        with  open("expensetracker.txt", "r") as file:
            lines = file.readlines()

            if not lines:
                print("No Entries Yet!!!")
                return
            for i, line in enumerate(lines, start=1):
                print(f"{i}. {line.strip()}")

            if 1 <= num_delete <= len(lines):

                ask = input(f"Are you sure you want to delete {num_delete} (y/n)?  ").lower()

                if ask == "y":
                    removed_line = lines.pop(num_delete-1)
                    print(f"Deleted: {removed_line}")

                    with open("expensetracker.txt", "w") as file:
                        file.writelines(lines)
                
                elif ask == "n":
                    return
                
                else:
                    print("Invalid Input!!!")    

            else:
                print("Invalid Number!!!")

    except FileNotFoundError:
        print("No Entries Yet!!!")
                        
def editexpense():
    

    while True:
        try:
            menu = int(input("=== Expense Tracker ===\n1. Add Expense\n2. View Expenses\n3. Filter Expenses\n4. View Totals by Category:  \n5. Edit Expense:  \n6. Delete Expense:  \n7. Exit:  \n"))
        except ValueError:
            print("Please enter a number (1, 2,3 or 4)!")
            continue

        if menu == 1:
            Add()

        elif menu == 2:
            View()

        elif menu == 3:
            filterexpenses()

        elif menu == 4:
            viewtotalsbycategory()

        elif menu == 6:
            deleteexpenses()

        elif menu == 7:
            print("EXITING.....")
            break

        else:
            print("Invalid Input!!!")
            continue