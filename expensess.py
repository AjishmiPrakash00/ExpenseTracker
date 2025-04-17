import csv 
import pandas as pd
import matplotlib.pyplot as plt

fname = "expenses.csv"

def main():
    createcsv()
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Log an Expense")
        print("2. Analyze Data")
        print("3. Visualize Data")
        print("4. Exit")

        ch = input("Choose an option: ")
        if ch == "1":
            expense()
        elif ch == "2":
            andata()
        elif ch == "3":
            vdata()
        elif ch == "4":
            print("Thank you! .....Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def createcsv():
    try:
        with open(fname, "r"):
            pass
    except FileNotFoundError:
        with open(fname, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])

def expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Transport, Rent): ")
    try:
        amount = float(input("Enter the amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    description = input("Enter a description (optional): ")

    with open(fname, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print("Expense logged successfully!")

def andata():
    try:
        df = pd.read_csv(fname)
        print("\n--- Summary Statistics ---")
        print(df.groupby("Category")["Amount"].sum())
        print("\n--- Total Expenses ---")
        print(f"₹{df['Amount'].sum()}")
    except FileNotFoundError:
        print("No data found. Please log some expenses first.")

def vdata():
    try:
        df = pd.read_csv(fname)
        datotals = df.groupby("Date")["Amount"].sum()
        cattotals = df.groupby("Category")["Amount"].sum()

        print("1. Category VS Amount chart")
        print("2. Date VS Amount chart")
        x = input("Enter Type: ")
        if x == "1":
            plt.bar(cattotals.index, cattotals.values)
            plt.xlabel("Category")
            plt.ylabel("Total Amount")
            plt.title("Expenses by Category")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        elif x == "2":
            plt.bar(datotals.index, datotals.values)
            plt.xlabel("Date")
            plt.ylabel("Total Amount")
            plt.title("Expenses by Date")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        else:
            print("Invalid choice.")
    except FileNotFoundError:
        print("No data found. Please log some expenses first.")

if __name__ == "__main__":
    main()
