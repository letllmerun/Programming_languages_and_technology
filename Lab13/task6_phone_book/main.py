import tkinter as tk
from tkinter import ttk, messagebox

# COLORS
BG = "#111827"
PANEL = "#1F2937"
ACCENT = "#8B5CF6"
TEXT = "#F9FAFB"
MUTED = "#9CA3AF"
GREEN = "#10B981"
RED = "#EF4444"

contacts = {}


# MAIN WINDOW
root = tk.Tk()
root.title("Phone Book | Task 1")
root.geometry("1000x850")
root.configure(bg=BG)
root.minsize(900, 750)


# HEADER
tk.Label(
    root,
    text="PHONE BOOK",
    font=("Segoe UI", 28, "bold"),
    bg=BG,
    fg=TEXT
).pack(pady=(30, 5))

tk.Label(
    root,
    text="CONTACT MANAGEMENT SYSTEM",
    font=("Segoe UI", 10),
    bg=BG,
    fg=MUTED
).pack(pady=(0, 25))


# INPUT PANEL
form = tk.Frame(root, bg=PANEL, padx=25, pady=20)
form.pack(fill="x", padx=40)

tk.Label(
    form,
    text="CONTACT NAME",
    bg=PANEL,
    fg=MUTED,
    font=("Segoe UI", 9, "bold")
).grid(row=0, column=0, sticky="w")

tk.Label(
    form,
    text="PHONE NUMBER",
    bg=PANEL,
    fg=MUTED,
    font=("Segoe UI", 9, "bold")
).grid(row=0, column=1, sticky="w", padx=15)

name_entry = tk.Entry(
    form,
    font=("Segoe UI", 12),
    bg="#374151",
    fg=TEXT,
    insertbackground=TEXT,
    relief="flat",
    width=25
)
name_entry.grid(row=1, column=0, ipady=10, pady=10)

number_entry = tk.Entry(
    form,
    font=("Segoe UI", 12),
    bg="#374151",
    fg=TEXT,
    insertbackground=TEXT,
    relief="flat",
    width=25
)
number_entry.grid(row=1, column=1, ipady=10, padx=15)


# CONTACT TABLE
table_frame = tk.Frame(root, bg=BG)
table_frame.pack(fill="both", expand=True, padx=40, pady=25)

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Treeview",
    background=PANEL,
    foreground=TEXT,
    fieldbackground=PANEL,
    rowheight=38,
    font=("Segoe UI", 11)
)

style.configure(
    "Treeview.Heading",
    background=ACCENT,
    foreground="white",
    font=("Segoe UI", 10, "bold")
)

style.map(
    "Treeview",
    background=[("selected", "#6D28D9")]
)

table = ttk.Treeview(
    table_frame,
    columns=("name", "number"),
    show="headings"
)

table.heading("name", text="CONTACT NAME")
table.heading("number", text="PHONE NUMBER")

table.column("name", width=300)
table.column("number", width=350)

table.pack(fill="both", expand=True)


# FUNCTIONS
def refresh_table():
    for item in table.get_children():
        table.delete(item)

    for name, number in contacts.items():
        table.insert("", "end", values=(name, number))


def select_contact(event):
    selected = table.selection()

    if selected:
        values = table.item(selected[0], "values")

        name_entry.delete(0, tk.END)
        name_entry.insert(0, values[0])

        number_entry.delete(0, tk.END)
        number_entry.insert(0, values[1])


table.bind("<<TreeviewSelect>>", select_contact)


def add_contact():
    name = name_entry.get().strip()
    number = number_entry.get().strip()

    if not name or not number:
        messagebox.showwarning(
            "Warning", "Fill in both fields!"
        )
        return

    if name in contacts:
        messagebox.showwarning(
            "Warning", "This contact already exists!"
        )
        return

    contacts[name] = number
    refresh_table()

    name_entry.delete(0, tk.END)
    number_entry.delete(0, tk.END)

    messagebox.showinfo(
        "Success", "Contact added successfully!"
    )


def search_contact():
    name = name_entry.get().strip()

    if name in contacts:
        number_entry.delete(0, tk.END)
        number_entry.insert(0, contacts[name])
        messagebox.showinfo(
            "Found", f"{name}: {contacts[name]}"
        )
    else:
        messagebox.showerror(
            "Not found", "Contact does not exist!"
        )


def edit_contact():
    name = name_entry.get().strip()
    number = number_entry.get().strip()

    if name not in contacts:
        messagebox.showerror(
            "Error", "Select an existing contact!"
        )
        return

    if not number:
        messagebox.showwarning(
            "Warning", "Enter a new phone number!"
        )
        return

    contacts[name] = number
    refresh_table()

    messagebox.showinfo(
        "Success", "Contact updated!"
    )


def delete_contact():
    name = name_entry.get().strip()

    if name not in contacts:
        messagebox.showerror(
            "Error", "Select a contact first!"
        )
        return

    del contacts[name]
    refresh_table()

    name_entry.delete(0, tk.END)
    number_entry.delete(0, tk.END)

    messagebox.showinfo(
        "Success", "Contact deleted!"
    )


# BUTTONS
buttons = tk.Frame(root, bg=BG)
buttons.pack(pady=(0, 25))


def create_button(title, command, color):
    tk.Button(
        buttons,
        text=title,
        command=command,
        bg=color,
        fg="white",
        activebackground=color,
        activeforeground="white",
        font=("Segoe UI", 10, "bold"),
        relief="flat",
        padx=20,
        pady=12,
        cursor="hand2"
    ).pack(side="left", padx=7)


create_button("+ ADD", add_contact, ACCENT)
create_button("SEARCH", search_contact, "#2563EB")
create_button("EDIT", edit_contact, GREEN)
create_button("DELETE", delete_contact, RED)


# FOOTER
tk.Label(
    root,
    text="LABORATORY WORK №13  |  PYTHON",
    bg=BG,
    fg=MUTED,
    font=("Segoe UI", 9)
).pack(pady=10)


root.mainloop()