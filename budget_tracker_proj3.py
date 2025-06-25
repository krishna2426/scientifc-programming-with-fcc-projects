class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []
  # Adding money to the category
  def deposit(self, amount, description=''):
    self.ledger.append({'amount': amount, 'description': description})
  #Taking money out if enough funds are available
  def withdraw(self, amount, description=''):
    if self.check_funds(amount):
      self.ledger.append({'amount': -amount, 'description': description})
      return True
    else:
      return False
  # Return the current balace
  def get_balance(self):
    balance = 0
    for item in self.ledger:
      balance += item['amount']
    return balance
  #  Move money from one category to another
  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount, 'Transfer to ' + category.name)
      category.deposit(amount, 'Transfer from ' + self.name)
      return True
    else:
      return False

  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    else:
      return True


  def __str__(self):
    # Title line
    title = self.name.center(30, "*") + "\n"

    # Ledger lines
    items = ""
    for entry in self.ledger:
        desc = entry["description"][:23]
        amt = "{0:.2f}".format(entry["amount"])
        items += f"{desc.ljust(23)}{amt.rjust(7)}\n"

    # Total line
    total = "Total: {:.2f}".format(self.get_balance())

    return title + items + total

 def create_spend_chart(categories):
    title = "Percentage spent by category\n"

    # Step 1: Calculate spending per category
    spend_amounts = []
    category_names = []

    for category in categories:
        total_spent = 0
        for item in category.ledger:
            if item['amount'] < 0:
                total_spent += abs(item['amount'])
        spend_amounts.append(total_spent)
        category_names.append(category.name)

    # Step 2: Calculate percentages (rounded down to nearest 10)
    total = sum(spend_amounts)
    percentages = [(int((spend / total) * 10) * 10) for spend in spend_amounts]

    # Step 3: Create chart rows (100 to 0)
    for i in range(100, -1, -10):
        row = f"{str(i).rjust(3)}|"
        for percent in percentages:
            if percent >= i:
                row += " o "
            else:
                row += "   "
        title += row + " \n"

    # Step 4: Add separator
    title += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Step 5: Add category names vertically
    max_len = max(len(name) for name in category_names)
    padded_names = [name.ljust(max_len) for name in category_names]

    for i in range(max_len):
        row = "     "
        for name in padded_names:
            row += name[i] + "  "
        if i < max_len - 1:
            title += row + "\n"
        else:
            title += row.rstrip()

    return title
