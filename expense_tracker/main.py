import csv
import os

FILE = "expenses.csv"

def add_record(amount, category, note):
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([amount, category, note])

def view_records():
    if not os.path.exists(FILE):
        print("No records yet.")
        return
    with open(FILE) as f:
        reader = csv.reader(f)
        print("Amount | Category | Note")
        for row in reader:
            print(" | ".join(row))

def summary():
    total = 0
    if not os.path.exists(FILE):
        print("No records yet.")
        return
    with open(FILE) as f:
        reader = csv.reader(f)
        for row in reader:
            total += float(row[0])
    print(f"Total balance: {total}")

def main():
    print("Expense Tracker. Commands: add, view, summary, quit")
    while True:
        cmd = input("> ").strip().split(maxsplit=1)
        if not cmd:
            continue
        action = cmd[0]
        arg = cmd[1] if len(cmd) > 1 else None
        if action == "add" and arg:
            try:
                amount, category, note = arg.split(maxsplit=2)
                add_record(float(amount), category, note)
            except:
                print("Format: add <amount> <category> <note>")
        elif action == "view":
            view_records()
        elif action == "summary":
            summary()
        elif action == "quit":
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()