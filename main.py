class ExpenseSplitter:

    def __init__(self):
        self.people = {}

    def add_expense(self, payer, amount, participants):
        try:
            amount = float(amount)
        except ValueError:
            print("Invalid amount! Please enter a numeric value.")
            return
        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        self.people[payer] = self.people.get(payer, 0) + amount
        split_amount = amount / len(participants) if participants else 0
        for person in participants:
            if person != payer:
                self.people[person] = self.people.get(person, 0) - split_amount

    def show_balances(self):
        print("\nBalances:")
        for person, balance in self.people.items():
            status = "owes" if balance < 0 else "is owed"
            print(f"{person}: {status} ₹{abs(balance):.2f}")

    def calculate_settlements(self):
        debtors = {p: b for p, b in self.people.items() if b < 0}
        creditors = {p: b for p, b in self.people.items() if b > 0}
        settlements = []

        for debtor, debt in debtors.items():
            for creditor, credit in list(creditors.items()):
                if credit > 0:
                    settle_amount = min(-debt, credit)
                    debt += settle_amount
                    creditors[creditor] -= settle_amount
                    settlements.append(
                        f"{debtor} pays {creditor}: ₹{settle_amount:.2f}")
                    if debt >= 0:
                        break

        print("\nSettlements:")
        for settlement in settlements:
            print(settlement)


def main():
    splitter = ExpenseSplitter()
    while True:
        print(
            "\nOptions: (1) Add Expense (2) Show Balances (3) Calculate Settlements (4) Exit"
        )
        choice = input("Choose an option: ")

        if choice == "1":
            payer = input("Who paid? ")
            amount = input("Amount paid: ₹")
            participants = input(
                "Enter participants (comma-separated): ").split(",")
            participants = [p.strip() for p in participants]
            splitter.add_expense(payer, amount, participants)
            print("Expense added.")
        elif choice == "2":
            splitter.show_balances()
        elif choice == "3":
            splitter.calculate_settlements()
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
