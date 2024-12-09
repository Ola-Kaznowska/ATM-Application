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
        print("✅ Transakcja dodana pomyślnie!")

    def view_transactions(self):
        if not self.transactions:
            print("\n📜 Brak transakcji.")
            return

        print("\n📜 Wszystkie transakcje:")
        for idx, t in enumerate(self.transactions, start=1):
            print(f"{idx}. [{t['date']}] {t['type']} - {t['amount']} ({t['category']}) -> {t['description']}")

    def analyze_data(self):
        if not self.transactions:
            print("\n📊 Brak transakcji do analizy.")
            return

        total_income = sum(float(t['amount']) for t in self.transactions if t['type'] == 'Income')
        total_expenses = sum(float(t['amount']) for t in self.transactions if t['type'] == 'Expense')
        largest_expense = max(
            (t for t in self.transactions if t['type'] == 'Expense'),
            key=lambda x: float(x['amount']),
            default=None
        )

        print("\n📊 Analiza:")
        print(f"Całkowite dochody: {total_income}")
        print(f"Całkowite wydatki: {total_expenses}")
        print(f"Bilans netto: {total_income - total_expenses}")
        if largest_expense:
            print(f"Największy wydatek: {largest_expense['amount']} ({largest_expense['category']}) -> {largest_expense['description']}")

    def export_report(self):
        if not self.transactions:
            print("\n📊 Brak transakcji do uwzględnienia w raporcie.")
            return

        total_income = sum(float(t['amount']) for t in self.transactions if t['type'] == 'Income')
        total_expenses = sum(float(t['amount']) for t in self.transactions if t['type'] == 'Expense')

        print("\n📊 Raport finansowy:")
        print(f"Całkowite dochody: {total_income}")
        print(f"Całkowite wydatki: {total_expenses}")
        print(f"Bilans netto: {total_income - total_expenses}")
        print("\nSzczegółowe transakcje:")
        for t in self.transactions:
            print(f"[{t['date']}] {t['type']} - {t['amount']} ({t['category']}) -> {t['description']}")

def main():
    manager = FinanceManager()

    while True:
        print("\n📂 Menedżer Finansów")
        print("1. Dodaj transakcję")
        print("2. Pokaż transakcje")
        print("3. Analizuj dane")
        print("4. Eksportuj raport")
        print("5. Wyjście")

        choice = input("Wybierz opcję: ")
        if choice == '1':
            type_ = input("Wpisz typ transakcji (Dochód/Wydatki): ")
            amount = input("Wpisz kwotę: ")
            category = input("Wpisz kategorię: ")
            description = input("Wpisz opis: ")
            manager.add_transaction(type_, amount, category, description)
        elif choice == '2':
            manager.view_transactions()
        elif choice == '3':
            manager.analyze_data()
        elif choice == '4':
            manager.export_report()
        elif choice == '5':
            print("👋 Do widzenia!")
            break
        else:
            print("❌ Nieprawidłowa opcja, spróbuj ponownie!")


if __name__ == "__main__":
    main()
