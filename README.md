# 💰 Expense Tracker

A modern and minimal desktop app for tracking your daily expenses, built with Python and CustomTkinter.

![Screenshot 2025-06-04 124804](https://github.com/user-attachments/assets/7084e4b9-4535-4f12-be2e-861509e7e1c9)

---

## ✨ Features

- 🧾 Add new expenses with title, amount, and date
- 📜 View all expenses in a scrollable list
- ❌ Delete individual expenses (automatically removes from file)
- 📊 Automatically updates and displays total amount spent
- 💾 Saves data in a local text file (`info.txt`)

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/Rexlep/Expense-Tracker.git
cd Expense-Tracker
```

### 2. Install dependencies

Make sure you have Python 3.10+ installed.

```bash
pip install customtkinter
```

### 3. Run the app

```bash
python main.py
```

---

## 📂 File Structure

```
Expense-Tracker/
├── main.py           # Main application code
├── info.txt          # File that stores all expenses
└── assets/
    └── screenshot.png (optional for GitHub preview)
```

---

## 🧠 How It Works

- Every time you add an expense, it’s saved as a new line in `info.txt` using this format:
  ```
  Title,$Amount,YYYY-MM-DD
  ```
- The app reads from this file at startup, displays the expenses, and calculates the total.
- Clicking the ❌ button next to each expense removes it both from the UI and the file.

---

## 📌 Example

> Adding this to `info.txt`:
```txt
Lunch,$12.00,2025-06-01
Coffee,$3.50,2025-06-01
Transport,$7.25,2025-06-02
```

> Displays:
```
Lunch - $12.00 - 2025-06-01
Coffee - $3.50 - 2025-06-01
Transport - $7.25 - 2025-06-02
```

> Total: `$22.75`

---

## 🌈 UI Preview

> A clean, dark-mode interface built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter).

![Screenshot 2025-06-04 124804](https://github.com/user-attachments/assets/c93d56f3-6fba-4f8e-9f98-27d11a9c0b45)

---

## 📃 License

MIT License © [Rexlep](https://github.com/Rexlep)

---

## 🙌 Contributing

Pull requests are welcome! Feel free to open issues for suggestions or bugs.
