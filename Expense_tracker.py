import json
import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, ttk

data_file = "expenses.json"

def load_expenses():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    with open(data_file, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(amount, description, category):
    expenses = load_expenses()
    expenses.append({"amount": amount, "description": description, "category": category, "date": datetime.now().strftime("%Y-%m-%d")})
    save_expenses(expenses)
    messagebox.showinfo("Success", "Expense added successfully!")

def view_expenses(tree):
    for item in tree.get_children():
        tree.delete(item)
    expenses = load_expenses()
    for exp in expenses:
        tree.insert("", "end", values=(exp["date"], exp["category"], exp["description"], exp["amount"]))

def create_ui():
    root = tk.Tk()
    root.title("Expense Tracker")
    root.geometry("500x400")
    
    tk.Label(root, text="Amount").pack()
    amount_entry = tk.Entry(root)
    amount_entry.pack()
    
    tk.Label(root, text="Description").pack()
    description_entry = tk.Entry(root)
    description_entry.pack()
    
    tk.Label(root, text="Category").pack()
    category_entry = tk.Entry(root)
    category_entry.pack()
    
    tk.Button(root, text="Add Expense", command=lambda: add_expense(amount_entry.get(), description_entry.get(), category_entry.get())).pack()
    
    tree = ttk.Treeview(root, columns=("Date", "Category", "Description", "Amount"), show='headings')
    tree.heading("Date", text="Date")
    tree.heading("Category", text="Category")
    tree.heading("Description", text="Description")
    tree.heading("Amount", text="Amount")
    tree.pack()
    
    tk.Button(root, text="View Expenses", command=lambda: view_expenses(tree)).pack()
    
    root.mainloop()

if __name__ == "__main__":
    create_ui()