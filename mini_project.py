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
        self.time_entry.insert(0, datetime.now().strftime("%H:%M"))  # Set initial time to current time

        self.category_label = ttk.Label(self.root, text="Category:")
        self.category_combobox = ttk.Combobox(self.root, values=self.categories)

        self.currency_label = ttk.Label(self.root, text="Currency:")
        self.currency_combobox = ttk.Combobox(self.root, values=["INR","USD", "EUR", "GBP", "JPY"], textvariable=self.selected_currency)

        self.add_button = ttk.Button(self.root, text="Add Expense", command=self.add_expense)
        self.total_button = ttk.Button(self.root, text="Show Total Expense", command=self.show_total_expense)

        self.tree = ttk.Treeview(self.root, columns=('Amount', 'Description', 'Date', 'Time', 'Category', 'Currency'))
        self.tree.heading('#0', text='ID')
        self.tree.heading('#1', text='Amount')
        self.tree.heading('#2', text='Description')
        self.tree.heading('#3', text='Date')
        self.tree.heading('#4', text='Time')
        self.tree.heading('#5', text='Category')
        self.tree.heading('#6', text='Currency')

        self.total_label = ttk.Label(self.root, text="Total Expenses: 0.00", font=('Helvetica', 12, 'bold'))

        self.amount_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        self.description_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.description_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        self.date_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.date_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        self.time_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.time_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        self.category_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
        self.category_combobox.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)

        self.currency_label.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
        self.currency_combobox.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)

        self.limit_label.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)
        self.limit_entry.grid(row=6, column=1, padx=5, pady=5, sticky=tk.W)

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

    def check_limit_exceeded(self, limit):
        total_expenses = sum(exp[0] for exp in self.expenses)
        return total_expenses > limit

    def play_limit_exceeded_sound(self):
        winsound.Beep(int(round(1000)), int(round(1000)))

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
