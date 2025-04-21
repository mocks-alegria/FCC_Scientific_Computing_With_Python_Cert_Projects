import math

class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
        
    def __str__(self):
        title = self.category.center(30, "*") + "\n"
        items = ""
        for item in self.ledger:
            items += f"{item['description'][:23]:<23}{item['amount']:>7.2f}\n"
        total = self.get_balance()
        return title + items + "Total: " + str(total)
    
    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
        
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False
        
    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total
  
    def check_funds(self, amount):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total >= amount
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.category}")
            category.deposit(amount, f"Transfer from {self.category}")
            return True
        else:
            return False

def create_spend_chart(categories):
    total = 0
    categorySpending = []
    percentages = []

    for category in categories:
        totalSpent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                totalSpent += item["amount"]
        totalSpent = abs(totalSpent)
        total += totalSpent
        categorySpending.append(totalSpent)

    for spending in categorySpending:
        percentages.append(math.floor((spending / total) * 100 // 10) * 10)

    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for percentage in percentages:
            chart += " o " if percentage >= i else "   "
        chart += " \n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_length = max(len(category.category) for category in categories)
    for i in range(max_length):
        chart += "     "
        for category in categories:
            if i < len(category.category):
                chart += category.category[i] + "  "
            else:
                chart += "   "
        if i < max_length - 1:
            chart += "\n"

    return chart

# Example usage:
if __name__ == "__main__":
    food = Category("Food")
    food.deposit(1000, "Initial deposit")
    food.withdraw(200, "Groceries")
    food.withdraw(150.75, "Restaurants")

    clothing = Category("Clothing")
    clothing.deposit(500, "Initial deposit")
    clothing.withdraw(50, "Shirt")
    clothing.withdraw(20, "Pants")

    entertainment = Category("Entertainment")
    entertainment.deposit(300, "Initial deposit")
    entertainment.withdraw(100, "Concert tickets")

    print(food, "\n")
    print(clothing, "\n")
    print(entertainment, "\n")

    print(create_spend_chart([food, clothing, entertainment]))
    food.transfer(50, clothing)
    print("\nAfter transfer:")
    print(food, "\n")
    print(clothing)