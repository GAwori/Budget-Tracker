#add JSON and files
import json
import budget

#print main menu to show options
def main():

    while True:
        print("========Main Menu========")
        print("1. Add Income")
        print("2. Add Expenses")
        print("3. View Balance")
        print("4. View Summary")
        print("5. Exit")
        print("=========================")
        choice = input("Enter your choice: ")

        #give appropriate function based on choice
        if choice == "1":
            budget.add_income()
        elif choice == "2":
            budget.add_expense()
        elif choice == "3":
            budget.view_balance()
        elif choice == "4":
            budget.view_summary()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            #if invalid choice, prompt again
            print("Invalid choice. Please try again.")

main()
