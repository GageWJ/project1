import tkinter as tk

class shoppingCart:
    def __init__(self):
        self.cookie_price = 1.50
        self.sandwich_price = 4.00
        self.water_price = 1.00
        self.cookie_count = 0
        self.sandwich_count = 0
        self.water_count = 0

        self.master = tk.Tk()
        self.master.title("Shop")
        self.master.geometry("400x400")

        self.frame = tk.Frame(self.master)
        self.frame.pack()
        self.label = tk.Label(self.frame, text="Enter amount for each item:")
        self.label.pack()
        self.cookie_label = tk.Label(self.frame, text="Cookie - $1.50")
        self.cookie_label.pack()
        self.cookie_entry = tk.Entry(self.frame, width=10)
        self.cookie_entry.pack()
        self.sandwich_label = tk.Label(self.frame, text="Sandwich - $4.00")
        self.sandwich_label.pack()
        self.sandwich_entry = tk.Entry(self.frame, width=10)
        self.sandwich_entry.pack()
        self.water_label = tk.Label(self.frame, text="Water - $1.00")
        self.water_label.pack()
        self.water_entry = tk.Entry(self.frame, width=10)
        self.water_entry.pack()
        self.finish_button = tk.Button(self.frame, text="Finish", command=self.show_total)
        self.finish_button.pack()
        self.exit_button = tk.Button(self.frame, text="Exit", command=self.master.destroy)
        self.exit_button.pack()

    def show_total(self):
        try:
            self.cookie_count = int(self.cookie_entry.get())
            self.sandwich_count = int(self.sandwich_entry.get())
            self.water_count = int(self.water_entry.get())
        except ValueError:
            self.error_label = tk.Label(self.frame, text="Please enter a valid number", fg="red")
            self.error_label.pack()
            return

        if self.cookie_count < 0 or self.sandwich_count < 0 or self.water_count < 0:
            self.error_label = tk.Label(self.frame, text="Please enter a positive number", fg="red")
            self.error_label.pack()
            return

        self.frame.destroy()
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.cookie_total = self.cookie_count * self.cookie_price
        self.sandwich_total = self.sandwich_count * self.sandwich_price
        self.water_total = self.water_count * self.water_price
        self.total = self.cookie_total + self.sandwich_total + self.water_total

        self.cookie_label = tk.Label(self.frame, text="({}) - Cookie = ${:.2f}".format(self.cookie_count, self.cookie_total))
        self.cookie_label.pack()
        self.sandwich_label = tk.Label(self.frame, text="({}) - Sandwich = ${:.2f}".format(self.sandwich_count, self.sandwich_total))
        self.sandwich_label.pack()
        self.water_label = tk.Label(self.frame, text="({}) - Water = ${:.2f}".format(self.water_count, self.water_total))
        self.water_label.pack()
        self.total_label = tk.Label(self.frame, text="TOTAL = ${:.2f}".format(self.total))
        self.total_label.pack()
        self.exit_button = tk.Button(self.frame, text="Exit", command=self.master.destroy)
        self.exit_button.pack()

if __name__ == "__main__":
    cart = shoppingCart()
    cart.master.mainloop()
