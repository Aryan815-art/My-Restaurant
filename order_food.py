import tkinter as tk
from tkinter import messagebox

# -------- MENU DATA ----------
menu = {
    "Pizza": [
        ("Margherita", 299),
        ("Farmhouse", 399),
        ("Cheese Burst", 449)
    ],
    "Pasta": [
        ("White Sauce Pasta", 259),
        ("Red Sauce Pasta", 239),
        ("Cheese Pasta", 279)
    ]
}

cart = []
total = 0

# -------- FUNCTIONS ----------
def save_details():
    if name_entry.get() == "" or phone_entry.get() == "":
        messagebox.showerror("Error", "Name and Phone are required!")
        return

    messagebox.showinfo(
        "Details Saved",
        f"Welcome {name_entry.get()} 😊\nYou can now place your order."
    )

def add_item(category, index):
    global total
    item, price = menu[category][index]
    cart.append((item, price))
    total += price

    cart_list.insert(tk.END, f"{item} - ₹{price}")
    total_label.config(text=f"Total: ₹{total}")

def finish_order():
    if not cart:
        messagebox.showwarning("No Order", "You have not ordered anything!")
        return

    bill = "\n".join([f"{i+1}. {item} - ₹{price}" for i, (item, price) in enumerate(cart)])

    messagebox.showinfo(
        "Order Completed 🧾",
        f"Customer: {name_entry.get()}\n\n"
        f"Ordered Items:\n{bill}\n\n"
        f"Grand Total: ₹{total}\n\nThank you for ordering! 🍴"
    )

# -------- GUI ----------
root = tk.Tk()
root.title("Restaurant Ordering System")
root.geometry("600x600")

# -------- USER DETAILS ----------
tk.Label(root, text="Customer Details", font=("Arial", 14, "bold")).pack(pady=5)

frame_details = tk.Frame(root)
frame_details.pack()

tk.Label(frame_details, text="Name").grid(row=0, column=0)
name_entry = tk.Entry(frame_details)
name_entry.grid(row=0, column=1)

tk.Label(frame_details, text="Address").grid(row=1, column=0)
address_entry = tk.Entry(frame_details)
address_entry.grid(row=1, column=1)

tk.Label(frame_details, text="Email").grid(row=2, column=0)
email_entry = tk.Entry(frame_details)
email_entry.grid(row=2, column=1)

tk.Label(frame_details, text="Phone").grid(row=3, column=0)
phone_entry = tk.Entry(frame_details)
phone_entry.grid(row=3, column=1)

tk.Button(root, text="Save Details", command=save_details, bg="lightgreen").pack(pady=5)

# -------- MENU ----------
tk.Label(root, text="Menu", font=("Arial", 14, "bold")).pack(pady=5)

menu_frame = tk.Frame(root)
menu_frame.pack()

# Pizza
pizza_frame = tk.LabelFrame(menu_frame, text="Pizza")
pizza_frame.grid(row=0, column=0, padx=10)

for i, (item, price) in enumerate(menu["Pizza"]):
    tk.Button(
        pizza_frame,
        text=f"{item} ₹{price}",
        command=lambda i=i: add_item("Pizza", i)
    ).pack(fill="x")

# Pasta
pasta_frame = tk.LabelFrame(menu_frame, text="Pasta")
pasta_frame.grid(row=0, column=1, padx=10)

for i, (item, price) in enumerate(menu["Pasta"]):
    tk.Button(
        pasta_frame,
        text=f"{item} ₹{price}",
        command=lambda i=i: add_item("Pasta", i)
    ).pack(fill="x")

# -------- CART ----------
tk.Label(root, text="Your Cart", font=("Arial", 14, "bold")).pack(pady=5)

cart_list = tk.Listbox(root, width=50)
cart_list.pack()

total_label = tk.Label(root, text="Total: ₹0", font=("Arial", 12, "bold"))
total_label.pack(pady=5)

tk.Button(
    root,
    text="Finish Order",
    command=finish_order,
    bg="orange",
    font=("Arial", 12, "bold")
).pack(pady=10)

root.mainloop()
