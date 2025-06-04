import customtkinter as ctk

c = 0

def update_total_label():
    total_label.configure(text=f"Total: ${c:.2f}")  # ✅ آپدیت لیبل

def delete_expense(expense_frame, line_to_remove):
    global c
    expense_frame.destroy()

    try:
        with open('info.txt', 'r') as file:
            lines = file.readlines()

        with open('info.txt', 'w') as file:
            for line in lines:
                if line.strip() != line_to_remove.strip():
                    file.write(line)
                else:
                    try:
                        _, amount_str, _ = line.strip().split(',')
                        n = float(amount_str.replace('$', ''))
                        c -= n  # ✅ از total کم کن
                    except:
                        pass

        update_total_label()  # ✅ آپدیت total
    except FileNotFoundError:
        print('Error: info.txt not found')


def read_expense_from_file():
    global c
    with open('info.txt', 'r') as file_of_information:
        for line in file_of_information:
            name_of_expense, amount_of_expense, date_of_expense = line.strip().split(',')
            n = float(amount_of_expense.replace('$', ''))
            c += n  # ✅ جمع هزینه‌ها

            expense_frame = ctk.CTkFrame(expense_list_frame, fg_color='transparent')
            expense_frame.pack(fill='x', padx=10, pady=2)

            expense_label = ctk.CTkLabel(
                expense_frame,
                text=f"{name_of_expense} - {amount_of_expense} - {date_of_expense}",
                font=('Inter', 15),
                anchor="w"
            )
            expense_label.pack(side='left', fill='x', expand=True)

            delete_button = ctk.CTkButton(
                expense_frame,
                text="✕",
                width=30,
                command=lambda f=expense_frame, l=line: delete_expense(f, l)
            )
            delete_button.pack(side='right', padx=5)

    update_total_label()  # ✅ بعد از خوندن فایل، لیبل رو آپدیت کن


def add_expense_in_scroll_bar():
    global c
    name_of_expense, amount_of_expense, date_of_expense = label_entry.get(), amount_entry.get(), date_entry.get()
    if not name_of_expense or not amount_of_expense or not date_of_expense:
        return

    try:
        n = float(amount_of_expense.replace('$', ''))
        c += n  # ✅ اضافه کردن هزینه جدید
    except ValueError:
        return

    line_to_add = f"{name_of_expense},{amount_of_expense},{date_of_expense}"

    expense_frame = ctk.CTkFrame(expense_list_frame, fg_color='transparent')
    expense_frame.pack(fill='x', padx=10, pady=2)

    expense_label = ctk.CTkLabel(expense_frame, text=f"{name_of_expense} - {amount_of_expense} - {date_of_expense}", font=('Inter', 15), anchor="w")
    expense_label.pack(side='left', fill='x', expand=True)

    delete_button = ctk.CTkButton(
        expense_frame,
        text="✕",
        width=30,
        command=lambda f=expense_frame, l=line_to_add: delete_expense(f, l)
    )
    delete_button.pack(side='right', padx=5)

    try:
        with open('info.txt', 'a+') as file_of_information:
            file_of_information.write(line_to_add + '\n')
    except FileNotFoundError:
        print('This file doesnt exist')

    update_total_label()  # ✅ آپدیت مجموع
    label_entry.delete(0, 'end')
    amount_entry.delete(0, 'end')
    date_entry.delete(0, 'end')


app = ctk.CTk()
app.title("Expense Tracker")
app.geometry("400x500")
app.resizable(False, False)

main_frame = ctk.CTkFrame(app, corner_radius=15)
main_frame.pack(padx=20, pady=20, fill="both", expand=True)

title_label = ctk.CTkLabel(main_frame, text="💰 Expense Tracker", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

label_entry = ctk.CTkEntry(main_frame, placeholder_text="Expense Title (e.g., Lunch)")
label_entry.pack(pady=10, padx=10, fill="x")

amount_entry = ctk.CTkEntry(main_frame, placeholder_text="Amount (e.g., 25.00)")
amount_entry.pack(pady=10, padx=10, fill="x")

date_entry = ctk.CTkEntry(main_frame, placeholder_text="Date (e.g., 2025-06-04)")
date_entry.pack(pady=10, padx=10, fill="x")

add_button = ctk.CTkButton(main_frame, text="➕ Add Expense", command=add_expense_in_scroll_bar)
add_button.pack(pady=10)

expense_list_frame = ctk.CTkScrollableFrame(main_frame, label_text="Expenses List", height=200)
expense_list_frame.pack(padx=10, pady=10, fill="both", expand=True)

total_label = ctk.CTkLabel(main_frame, text="Total: $0.00", font=("Arial", 16, "bold"))  # ✅ لیبل مجموع
total_label.pack(pady=10)

read_expense_from_file()

app.mainloop()
