#1. Encapsulation in Personal Budget Management
#Problem Statement: You are required to build a Personal Budget Management application. 
# The application will manage budget categories like food, entertainment, utilities, etc., 
# ensuring that budget details remain private and are accessed or modified through public methods.

#Task 1: Define Budget Category Class Create a class `BudgetCategory` with private attributes for category name and allocated budget. 
# - Initialize these attributes in the constructor.
#Task 2: Implement Getters and Setters - Write getter and setter methods for both the category name and the allocated budget.
#  - Ensure that the setter methods include validation (e.g., budget should be a positive number).
#Task 3: Add Budget Functionality Implement a method to add expenses to a category and adjust the budget accordingly. - Validate the expense amount before making deductions from the budget.
#Task 4: Display Budget Details Create a method to display the details of a budget category, including the name, allocated budget, and remaining budget after expenses.

class BudgetCategory:
    # Constructor and private attributes (task 1)
    def __init__ (self, category_name, budget):
        self.__category_name = category_name
        self.__budget = budget
        self.__expenses = 0
    # Getters and setters for category name and budget (task 2)
    def get_category_name(self):
        return self.__category_name
    def set_category_name(self, name):
        self.__category_name = name
    def get_budget(self):
        return self.__budget
    def set_budget(self, budget):
        self.__budget = budget

    def add_expense(self, amount):
        # Method to add an expense to the category (task 3)
        if amount > 0:
            self.__expenses += amount
        else:
            print("Enter a positive number to add to expenses")

    def display_category_summary(self):
        # Method to display the budget category details (task 4)
        print(f"Category: {self.__category_name}\nBudget: ${self.__budget}\nExpenses: ${self.__expenses}")
        print(f"Remaining Budget: ${self.__budget - self.__expenses}")

food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()