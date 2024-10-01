import tkinter as tk
from tkinter import messagebox


class Account:
    total_accounts_created = 0

    def __init__(self):
        self.account_number = None
        self.customer_id = None
        self.minimum_balance = 1000
        self.available_balance = None
        self.account_type = None
        self.service_branch_ifsc = None
        self.customer_name = None
        self.branch = None
        Account.total_accounts_created += 1

    def set_details(self, acno, custid, bal, actype, ifsc, name, branchhh):
        self.account_number = acno
        self.customer_id = custid
        self.available_balance = bal
        self.account_type = actype
        self.service_branch_ifsc = ifsc
        self.customer_name = name
        self.branch = branchhh

    def get_details(self, account_no):
        if account_no == self.account_number:
            return (
                f"Customer ID: {self.customer_id}\n"
                f"Customer Name: {self.customer_name}\n"
                f"Account Type: {self.account_type}\n"
                f"IFSC Code: {self.service_branch_ifsc}\n"
                f"Minimum Balance: {self.minimum_balance}\n"
                f"Available Balance: {self.available_balance}\n"
                f"Branch name: {self.branch}"
            )
        else:
            return "NIL"

    def deposit(self, amount):
        self.available_balance += amount
        return f"Amount deposited. Available Balance: {self.available_balance}"

    def withdraw(self, amount):
        if self.available_balance - amount >= self.minimum_balance:
            self.available_balance -= amount
            return f"Amount Withdrawn. Available Balance: {self.available_balance}"
        else:
            return "Insufficient Balance Amount."

    @staticmethod
    def total_account():
        return Account.total_accounts_created


class BankingSystemApp:
    def __init__(self, root):
        self.accounts = []
        self.root = root
        self.root.title("Banking System")

        self.create_main_window()

    def create_main_window(self):
        # Create Account Button
        create_account_btn = tk.Button(self.root, text="Create Account", command=self.create_account_window)
        create_account_btn.grid(row=0, column=0, padx=10, pady=10)

        # Get Account Details Button
        details_btn = tk.Button(self.root, text="Get Account Details", command=self.get_details_window)
        details_btn.grid(row=0, column=1, padx=10, pady=10)

        # Deposit Button
        deposit_btn = tk.Button(self.root, text="Deposit", command=self.deposit_window)
        deposit_btn.grid(row=0, column=2, padx=10, pady=10)

        # Withdraw Button
        withdraw_btn = tk.Button(self.root, text="Withdraw", command=self.withdraw_window)
        withdraw_btn.grid(row=0, column=3, padx=10, pady=10)

        # Total Accounts Button
        total_accounts_btn = tk.Button(self.root, text="Total Accounts", command=self.total_accounts)
        total_accounts_btn.grid(row=0, column=4, padx=10, pady=10)

    def create_account_window(self):
        window = tk.Toplevel(self.root)
        window.title("Create Account")

        fields = ["Account Number", "Customer Name", "Customer ID", "Available Balance", "Account Type", "Branch", "IFSC Code"]
        entries = {}

        for i, field in enumerate(fields):
            label = tk.Label(window, text=field)
            label.grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(window)
            entry.grid(row=i, column=1, padx=10, pady=5)
            entries[field] = entry

        def create_account():
            try:
                acno = int(entries["Account Number"].get())
                name = entries["Customer Name"].get()
                custid = int(entries["Customer ID"].get())
                bal = float(entries["Available Balance"].get())
                actype = entries["Account Type"].get()
                branch = entries["Branch"].get()
                ifsc = entries["IFSC Code"].get()

                account = Account()
                account.set_details(acno, custid, bal, actype, ifsc, name, branch)
                self.accounts.append(account)

                messagebox.showinfo("Success", "Account Created Successfully")
                window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter correct values.")

        create_btn = tk.Button(window, text="Create Account", command=create_account)
        create_btn.grid(row=len(fields), columnspan=2, pady=10)

    def get_details_window(self):
        window = tk.Toplevel(self.root)
        window.title("Get Account Details")

        tk.Label(window, text="Enter Account Number:").grid(row=0, column=0, padx=10, pady=5)
        account_number_entry = tk.Entry(window)
        account_number_entry.grid(row=0, column=1, padx=10, pady=5)

        def get_details():
            try:
                acno = int(account_number_entry.get())
                for account in self.accounts:
                    details = account.get_details(acno)
                    if details != "NIL":
                        messagebox.showinfo("Account Details", details)
                        return
                messagebox.showerror("Error", "Account not found.")
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter a valid account number.")

        details_btn = tk.Button(window, text="Get Details", command=get_details)
        details_btn.grid(row=1, columnspan=2, pady=10)

    def deposit_window(self):
        window = tk.Toplevel(self.root)
        window.title("Deposit Money")

        tk.Label(window, text="Enter Account Number:").grid(row=0, column=0, padx=10, pady=5)
        account_number_entry = tk.Entry(window)
        account_number_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(window, text="Enter Amount to Deposit:").grid(row=1, column=0, padx=10, pady=5)
        amount_entry = tk.Entry(window)
        amount_entry.grid(row=1, column=1, padx=10, pady=5)

        def deposit():
            try:
                acno = int(account_number_entry.get())
                amount = float(amount_entry.get())
                for account in self.accounts:
                    if account.account_number == acno:
                        messagebox.showinfo("Deposit", account.deposit(amount))
                        return
                messagebox.showerror("Error", "Account not found.")
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter correct values.")

        deposit_btn = tk.Button(window, text="Deposit", command=deposit)
        deposit_btn.grid(row=2, columnspan=2, pady=10)

    def withdraw_window(self):
        window = tk.Toplevel(self.root)
        window.title("Withdraw Money")

        tk.Label(window, text="Enter Account Number:").grid(row=0, column=0, padx=10, pady=5)
        account_number_entry = tk.Entry(window)
        account_number_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(window, text="Enter Amount to Withdraw:").grid(row=1, column=0, padx=10, pady=5)
        amount_entry = tk.Entry(window)
        amount_entry.grid(row=1, column=1, padx=10, pady=5)

        def withdraw():
            try:
                acno = int(account_number_entry.get())
                amount = float(amount_entry.get())
                for account in self.accounts:
                    if account.account_number == acno:
                        messagebox.showinfo("Withdraw", account.withdraw(amount))
                        return
                messagebox.showerror("Error", "Account not found.")
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter correct values.")

        withdraw_btn = tk.Button(window, text="Withdraw", command=withdraw)
        withdraw_btn.grid(row=2, columnspan=2, pady=10)

    def total_accounts(self):
        messagebox.showinfo("Total Accounts", f"Total Accounts: {Account.total_account()}")


if __name__ == "__main__":
    root = tk.Tk()
    app = BankingSystemApp(root)
    root.mainloop()
