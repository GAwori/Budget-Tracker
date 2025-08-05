import json

# Load data from JSON file
def load_data():
    try:
        with open('storage.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"income": [], "expenses": [], "balance": 0}

def save_data():
    with open('storage.json', 'w') as f:
        json.dump({"income": income, "expenses": expenses, "balance": balance}, f, indent=4)

# Initialize budget variables
data = load_data()
income = data.get("income", [])
expenses = data.get("expenses", [])
balance = data.get("balance", 0)

#return to main menu
def return_to_main():
    input("Press Enter to return to the main menu...")
    from main import main
    main()

#add income to balance
def add_income():
    #allows vars
    global balance, income
    #takes income
    amount = float(input("Enter income amount: "))

    #adds income to balance and saves
    balance += amount
    income.append(amount)
    save_data()

    #return to main?
    return_to_main()

#take expense from balance
def add_expense():
    #allows vars
    global balance, expenses
    #takes expense
    amount = float(input("Enter expense amount: "))
    #tests for sufficient amount
    if amount > balance:
        print("Insufficient balance.")
        return
    #subtract expsense from balance and saves
    else:
        balance -= amount
        expenses.append(amount)
        save_data()
    
    #return to main?
    return_to_main()

#view balance
def view_balance():
    print(f"Current balance: ${balance:.2f}")

    #return to main?
    return_to_main()

#view summary of income and expenses
def view_summary():
    #allows vars
    global income, expenses, balance
    print("========Budget Summary========")
    print("Income Summary:")
    for i, inc in enumerate(income, start=1):
        print(f"{i}. ${inc:.2f}")

    print("Expense Summary:")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. ${exp:.2f}")

    print(f"Total Balance: ${balance:.2f}")
    print("==============================")

    #return to main?
    return_to_main()


