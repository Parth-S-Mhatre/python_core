import tkinter as tk
from tkinter import messagebox

class RegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Form")

        # Create labels and entry widgets for Name, Age, and Address
        self.label_name = tk.Label(root, text="Name:")
        self.label_name.grid(row=0, column=0, padx=10, pady=10)

        self.entry_name = tk.Entry(root)
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)

        self.label_age = tk.Label(root, text="Age:")
        self.label_age.grid(row=1, column=0, padx=10, pady=10)

        self.entry_age = tk.Entry(root)
        self.entry_age.grid(row=1, column=1, padx=10, pady=10)

        self.label_address = tk.Label(root, text="Address:")
        self.label_address.grid(row=2, column=0, padx=10, pady=10)

        self.entry_address = tk.Entry(root)
        self.entry_address.grid(row=2, column=1, padx=10, pady=10)

        # Create a Submit button
        self.submit_button = tk.Button(root, text="Submit", command=self.submit)
        self.submit_button.grid(row=3, column=0, columnspan=2, pady=10)

    def submit(self):
        # Get values from the entry widgets
        name = self.entry_name.get()
        age = self.entry_age.get()
        address = self.entry_address.get()

        # Display the values in a message box
        messagebox.showinfo("Registration Details", f"Name: {name}\nAge: {age}\nAddress: {address}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationForm(root)
    root.mainloop()