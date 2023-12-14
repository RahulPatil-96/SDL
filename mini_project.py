import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime
import winsound

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        self.expenses = []
        self.categories = ["Groceries", "Utilities", "Entertainment", "Dining Out", "Others"]

        self.selected_currency = tk.StringVar(value="INR")

        self.limit_label = ttk.Label(self.root, text="Expense Limit:")
        self.limit_entry = ttk.Entry(self.root)
        self.limit_entry.insert(0, "1000")

        self.create_widgets()

    def create_widgets(self):
        self.amount_label = ttk.Label(self.root, text="Amount:")
        self.amount_entry = ttk.Entry(self.root)

        self.description_label = ttk.Label(self.root, text="Description:")
        self.description_entry = ttk.Entry(self.root)

        self.date_label = ttk.Label(self.root, text="Date:")
        self.date_entry = DateEntry(self.root, width=12, background='darkblue', foreground='white', borderwidth=2)

        self.time_label = ttk.Label(self.root, text="Time:")
        self.time_entry = ttk.Entry(self.root)
        self.time_entry.insert(0, datetime.now().strftime("%H:%M"))

        self.category_label = ttk.Label(self.root, text="Category:")
        self.category_combobox = ttk.Combobox(self.root, values=self.categories)

        self.currency_label = ttk.Label(self.root, text="Currency:")
        self.currency_combobox = ttk.Combobox(self.root, values=["INR", "USD", "EUR", "GBP", "JPY"], textvariable=self.selected_currency)

        self.add_button = ttk.Button(self.root, text="Add Expense", command=self.add_expense)
        self.total_button = ttk.Button(self.root, text="Show Total Expense", command=self.show_total_expense)

        columns = ('Amount', 'Description', 'Date', 'Time', 'Category', 'Currency')
        self.tree = ttk.Treeview(self.root, columns=columns)
        for i, col in enumerate(columns):
            self.tree.heading(f'#{i}', text=col)
        self.tree.column('#0', stretch=tk.NO, width=0)  # Hide ID column

        self.total_label = ttk.Label(self.root, text="Total Expenses: 0.00", font=('Helvetica', 12, 'bold'))

        self.limit_label.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)
        self.limit_entry.grid(row=6, column=1, padx=5, pady=5, sticky=tk.W)

        widgets = [
            (self.amount_label, self.amount_entry),
            (self.description_label, self.description_entry),
            (self.date_label, self.date_entry),
            (self.time_label, self.time_entry),
            (self.category_label, self.category_combobox),
            (self.currency_label, self.currency_combobox),
        ]

        for i, (label, entry) in enumerate(widgets, start=1):
            label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky=tk.W)

        self.add_button.grid(row=7, column=0, pady=10)
        self.total_button.grid(row=7, column=1, pady=10)

        self.tree.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

        self.total_label.grid(row=9, column=0, columnspan=2, pady=10)

    def add_expense(self):
        amount = self.amount_entry.get()
        description = self.description_entry.get()
        date = self.date_entry.get_date()
        time_value = self.time_entry.get()
        category = self.category_combobox.get()
        currency = self.selected_currency.get()

        if amount and description and date and time_value and category:
            expense = (float(amount), description, date, time_value, category, currency)
            self.expenses.append(expense)

            self.amount_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)
            self.date_entry.delete(0, tk.END)
            self.time_entry.delete(0, tk.END)

            id = len(self.expenses)
            self.tree.insert('', 'end', text=id, values=(amount, description, date, time_value, category, currency))

    def show_total_expense(self):
        limit = float(self.limit_entry.get())
        if self.check_limit_exceeded(limit):
            self.play_limit_exceeded_sound()

        total_expenses = sum(exp[0] for exp in self.expenses)
        self.total_label.config(text=f"Total Expenses: {self.selected_currency.get()} {total_expenses:.2f}")

        self.write_to_file()  # Update the file when showing total expenses

    def check_limit_exceeded(self, limit):
        total_expenses = sum(exp[0] for exp in self.expenses)
        return total_expenses > limit

    def play_limit_exceeded_sound(self):
        winsound.Beep(int(round(1000)), int(round(1000)))

    def write_to_file(self, filename="expenses.txt"):
        with open(filename, 'w') as file:
            file.write("Expense Details:\n")
            for index, expense in enumerate(self.expenses, start=1):
                file.write(f"\nExpense {index}:\n")
                file.write(f"Amount: {expense[0]} {expense[5]}\n")
                file.write(f"Description: {expense[1]}\n")
                file.write(f"Date: {expense[2]}\n")
                file.write(f"Time: {expense[3]}\n")
                file.write(f"Category: {expense[4]}\n")

            total_expenses = sum(exp[0] for exp in self.expenses)
            file.write("\nTotal Expenses:\n")
            file.write(f"Total: {self.selected_currency.get()} {total_expenses:.2f}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
