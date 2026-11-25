import tkinter as tk
from tkinter import ttk, messagebox

# Цветовая палитра
BG = "#111827"
PANEL = "#1F2937"
ACCENT = "#8B5CF6"
TEXT = "#F9FAFB"
SECONDARY = "#9CA3AF"
GREEN = "#10B981"
RED = "#EF4444"

contacts = {}


def phone_book():
    window = tk.Toplevel(root)
    window.title("Phone Book")
    window.geometry("850x750")
    window.configure(bg=BG)
    window.resizable(True, False)

    tk.Label(
        window,
        text="PHONE BOOK",
        font=("Segoe UI", 24, "bold"),
        bg=BG,
        fg=TEXT
    ).pack(pady=(25, 5))

    tk.Label(
        window,
        text="Manage your contacts in one place",
        font=("Segoe UI", 10),
        bg=BG,
        fg=SECONDARY
    ).pack(pady=(0, 20))

    form = tk.Frame(window, bg=PANEL, padx=20, pady=20)
    form.pack(fill="x", padx=35)

    tk.Label(
        form, text="CONTACT NAME",
        bg=PANEL, fg=SECONDARY,
        font=("Segoe UI", 9, "bold")
    ).grid(row=0, column=0, sticky="w")

    tk.Label(
        form, text="PHONE NUMBER",
        bg=PANEL, fg=SECONDARY,
        font=("Segoe UI", 9, "bold")
    ).grid(row=0, column=1, sticky="w", padx=10)

    name_entry = tk.Entry(
        form, font=("Segoe UI", 11),
        bg="#374151", fg=TEXT,
        insertbackground=TEXT, relief="flat",
        width=25
    )
    name_entry.grid(row=1, column=0, ipady=10, pady=8)

    number_entry = tk.Entry(
        form, font=("Segoe UI", 11),
        bg="#374151", fg=TEXT,
        insertbackground=TEXT, relief="flat",
        width=25
    )
    number_entry.grid(row=1, column=1, ipady=10, padx=10)

    table_frame = tk.Frame(window, bg=BG)
    table_frame.pack(fill="both", expand=True, padx=35, pady=20)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure(
        "Treeview",
        background=PANEL,
        foreground=TEXT,
        fieldbackground=PANEL,
        rowheight=35,
        font=("Segoe UI", 10)
    )
    style.configure(
        "Treeview.Heading",
        background=ACCENT,
        foreground="white",
        font=("Segoe UI", 10, "bold")
    )

    table = ttk.Treeview(
        table_frame,
        columns=("name", "number"),
        show="headings"
    )

    table.heading("name", text="CONTACT")
    table.heading("number", text="PHONE NUMBER")

    table.column("name", width=250)
    table.column("number", width=300)

    table.pack(fill="both", expand=True)

    def refresh():
        for item in table.get_children():
            table.delete(item)

        for name, number in contacts.items():
            table.insert("", "end", values=(name, number))

    def add_contact():
        name = name_entry.get().strip()
        number = number_entry.get().strip()

        if not name or not number:
            messagebox.showwarning(
                "Warning", "Enter name and phone number!"
            )
            return

        contacts[name] = number
        refresh()

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
        else:
            messagebox.showerror(
                "Not found", "Contact does not exist."
            )

    def edit_contact():
        name = name_entry.get().strip()
        number = number_entry.get().strip()

        if name not in contacts:
            messagebox.showerror(
                "Error", "Contact not found."
            )
            return

        if not number:
            messagebox.showwarning(
                "Warning", "Enter a new phone number."
            )
            return

        contacts[name] = number
        refresh()

        messagebox.showinfo(
            "Success", "Contact updated!"
        )

    def delete_contact():
        name = name_entry.get().strip()

        if name not in contacts:
            messagebox.showerror(
                "Error", "Contact not found."
            )
            return

        del contacts[name]
        refresh()

        messagebox.showinfo(
            "Success", "Contact deleted!"
        )

    buttons = tk.Frame(window, bg=BG)
    buttons.pack(pady=(0, 25))

    def create_button(text, command, color):
        tk.Button(
            buttons,
            text=text,
            command=command,
            bg=color,
            fg="white",
            activebackground=color,
            activeforeground="white",
            relief="flat",
            font=("Segoe UI", 10, "bold"),
            padx=18,
            pady=10,
            cursor="hand2"
        ).pack(side="left", padx=5)

    create_button("＋ Add", add_contact, ACCENT)
    create_button("⌕ Search", search_contact, "#2563EB")
    create_button("✎ Edit", edit_contact, GREEN)
    create_button("✕ Delete", delete_contact, RED)


# MAIN WINDOW
root = tk.Tk()
root.title("LAB 13 | Data Structures")
root.geometry("750x500")
root.configure(bg=BG)
root.resizable(False, False)

tk.Label(
    root,
    text="DATA STRUCTURES",
    font=("Segoe UI", 27, "bold"),
    bg=BG,
    fg=TEXT
).pack(pady=(55, 5))

tk.Label(
    root,
    text="Laboratory Work №13 • Python",
    font=("Segoe UI", 11),
    bg=BG,
    fg=SECONDARY
).pack(pady=(0, 35))

tk.Label(
    root,
    text="Choose a project to get started",
    font=("Segoe UI", 12),
    bg=BG,
    fg=TEXT
).pack(pady=10)

card = tk.Frame(root, bg=PANEL, padx=35, pady=25)
card.pack(padx=100, fill="x")

tk.Label(
    card,
    text="01  |  PHONE BOOK",
    font=("Segoe UI", 15, "bold"),
    bg=PANEL,
    fg=TEXT
).pack(pady=8)

tk.Label(
    card,
    text="Add, search, edit and delete contacts",
    font=("Segoe UI", 10),
    bg=PANEL,
    fg=SECONDARY
).pack(pady=5)

tk.Button(
    card,
    text="OPEN PROJECT  →",
    command=phone_book,
    bg=ACCENT,
    fg="white",
    font=("Segoe UI", 11, "bold"),
    relief="flat",
    cursor="hand2",
    padx=25,
    pady=12
).pack(pady=15)

tk.Label(
    root,
    text="PYTHON COLLECTIONS  •  2026",
    font=("Segoe UI", 9),
    bg=BG,
    fg=SECONDARY
).pack(side="bottom", pady=20)

root.mainloop()