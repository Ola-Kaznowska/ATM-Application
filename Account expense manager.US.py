from datetime import datetime


class FinanceManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, type_, amount, category, description):
        transaction = {
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'type': type_,
            'amount': float(amount),
            'category': category,
            'description': description
        }
        self.transactions.append(transaction)
        print("✅ Transaction added successfully!")

    def view_transactions(self):
        if not self.transactions:
            print("\n📜 No transactions found.")
            return

        print("\n📜 All Transactions:")
        for idx, t in enumerate(self.transactions, start=1):
            print(f"{idx}. [{t['date']}] {t['type']} - {t['amount']} ({t['category']}) -> {t['description']}")

    def analyze_data(self):
        if not self.transactions:
            print("\n📊 No transactions to analyze.")
            return

        total_income = sum(float(t['amount']) for t in self.transactions if t['type'] == 'Income')
        total_expenses = sum(float(t['amount']) for t in self.transactions if t['type'] == 'Expense')
        largest_expense = max(
            (t for t in self.transactions if t['type'] == 'Expense'),
            key=lambda x: float(x['amount']),
            default=None
        )

        print("\n📊 Analysis:")
        print(f"Total Income: {total_income}")
        print(f"Total Expenses: {total_expenses}")
        print(f"Net Balance: {total_income - total_expenses}")
        if largest_expense:
            print(f"Largest Expense: {largest_expense['amount']} ({largest_expense['category']}) -> {largest_expense['description']}")

    def export_report(self):
        if not self.transactions:
            print("\n📊 No transactions to include in the report.")
            return

        total_income = sum(float(t['amount']) for t in self.transactions if t['type'] == 'Income')
        total_expenses = sum(float(t['amount']) for t in self.transactions if t['type'] == 'Expense')

        print("\n📊 Financial Report:")
        print(f"Total Income: {total_income}")
        print(f"Total Expenses: {total_expenses}")
        print(f"Net Balance: {total_income - total_expenses}")
        print("\nDetailed Transactions:")
        for t in self.transactions:
            print(f"[{t['date']}] {t['type']} - {t['amount']} ({t['category']}) -> {t['description']}")


def main():
    manager = FinanceManager()

    while True:
        print("\n📂 Finance Manager")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Analyze Data")
        print("4. Export Report")
        print("5. Exit")

        choice = input("Select an option: ")
        if choice == '1':
            type_ = input("Enter transaction type (Income/Expense): ")
            amount = input("Enter amount: ")
            category = input("Enter category: ")
            description = input("Enter description: ")
            manager.add_transaction(type_, amount, category, description)
        elif choice == '2':
            manager.view_transactions()
        elif choice == '3':
            manager.analyze_data()
        elif choice == '4':
            manager.export_report()
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option, try again!")


if __name__ == "__main__":
    main()
