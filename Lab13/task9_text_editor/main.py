import tkinter as tk
from tkinter import messagebox, filedialog
from pathlib import Path

BG = "#101827"
PANEL = "#182438"
CARD = "#213149"
ACCENT = "#8B9CFF"
TEXT = "#F2F5FC"
MUTED = "#A7B3C8"
GREEN = "#57D6A0"


class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TextFlow — Text Editor")
        self.root.geometry("1050x700")
        self.root.configure(bg=BG)

        self.undo_stack = []
        self.current_text = ""
        self.loading = False

        self.build_ui()

    def build_ui(self):
        header = tk.Frame(self.root, bg=BG)
        header.pack(fill="x", padx=28, pady=22)

        tk.Label(
            header, text="TextFlow",
            bg=BG, fg=TEXT,
            font=("Segoe UI", 26, "bold")
        ).pack(side="left")

        tk.Label(
            header, text="  / TEXT EDITOR",
            bg=BG, fg=ACCENT,
            font=("Segoe UI", 10, "bold")
        ).pack(side="left", pady=12)

        intro = tk.Frame(self.root, bg=PANEL, padx=18, pady=15)
        intro.pack(fill="x", padx=28)

        tk.Label(
            intro,
            text="Your workspace",
            bg=PANEL, fg=TEXT,
            font=("Segoe UI", 15, "bold")
        ).pack(anchor="w")

        tk.Label(
            intro,
            text="Write, edit and manage your text easily.",
            bg=PANEL, fg=MUTED
        ).pack(anchor="w")

        toolbar = tk.Frame(self.root, bg=BG)
        toolbar.pack(fill="x", padx=28, pady=15)

        self.button(toolbar, "↶ Undo", self.undo, ACCENT).pack(side="left")
        self.button(toolbar, "Clear", self.clear_text, CARD).pack(side="left", padx=8)
        self.button(toolbar, "Open file", self.open_file, CARD).pack(side="left")
        self.button(toolbar, "Save as", self.save_file, GREEN).pack(side="right")

        body = tk.Frame(self.root, bg=BG)
        body.pack(fill="both", expand=True, padx=28, pady=5)

        editor_frame = tk.Frame(body, bg=PANEL, padx=15, pady=15)
        editor_frame.pack(side="left", fill="both", expand=True)

        tk.Label(
            editor_frame,
            text="TEXT EDITOR",
            bg=PANEL, fg=MUTED,
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w")

        self.editor = tk.Text(
            editor_frame,
            bg="#0D1522",
            fg=TEXT,
            insertbackground=ACCENT,
            font=("Segoe UI", 12),
            wrap="word",
            relief="flat",
            padx=15,
            pady=15
        )
        self.editor.pack(fill="both", expand=True, pady=12)

        self.editor.bind("<KeyRelease>", self.on_change)
        self.editor.bind("<Control-z>", self.undo_shortcut)

        sidebar = tk.Frame(body, bg=PANEL, width=220, padx=15, pady=15)
        sidebar.pack(side="right", fill="y", padx=(15, 0))
        sidebar.pack_propagate(False)

        tk.Label(
            sidebar,
            text="EDIT HISTORY",
            bg=PANEL, fg=MUTED,
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w")

        self.stack_count = tk.Label(
            sidebar, text="0",
            bg=PANEL, fg=ACCENT,
            font=("Segoe UI", 32, "bold")
        )
        self.stack_count.pack(anchor="w", pady=10)

        tk.Label(
            sidebar,
            text="Saved states",
            bg=PANEL, fg=MUTED
        ).pack(anchor="w")

        tk.Frame(sidebar, bg=CARD, height=2).pack(fill="x", pady=20)

        tk.Label(
            sidebar,
            text="TEXT STATISTICS",
            bg=PANEL, fg=MUTED,
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w")

        self.words_label = tk.Label(
            sidebar, text="0 words",
            bg=PANEL, fg=TEXT,
            font=("Segoe UI", 15, "bold")
        )
        self.words_label.pack(anchor="w", pady=10)

        self.chars_label = tk.Label(
            sidebar, text="0 characters",
            bg=PANEL, fg=MUTED
        )
        self.chars_label.pack(anchor="w")

        footer = tk.Frame(self.root, bg="#0B1220", padx=28, pady=10)
        footer.pack(fill="x")

        tk.Label(
            footer,
            text="Python | Stack | LIFO",
            bg="#0B1220", fg=MUTED
        ).pack(side="right")

        self.status = tk.Label(
            footer, text="Ready",
            bg="#0B1220", fg=MUTED
        )
        self.status.pack(side="left")

    def button(self, parent, text, command, color):
        return tk.Button(
            parent,
            text=text,
            command=command,
            bg=color,
            fg="#101827" if color in [ACCENT, GREEN] else TEXT,
            relief="flat",
            padx=16,
            pady=9,
            cursor="hand2",
            font=("Segoe UI", 10, "bold")
        )

    def on_change(self, event=None):
        if self.loading:
            return

        new_text = self.editor.get("1.0", "end-1c")

        if new_text != self.current_text:
            self.undo_stack.append(self.current_text)
            self.current_text = new_text
            self.update_statistics()

    def undo(self):
        if not self.undo_stack:
            messagebox.showinfo(
                "Undo",
                "There are no changes to undo."
            )
            return

        previous = self.undo_stack.pop()

        self.loading = True
        self.editor.delete("1.0", "end")
        self.editor.insert("1.0", previous)
        self.loading = False

        self.current_text = previous
        self.update_statistics()

        self.status.config(text="Last change undone")

    def undo_shortcut(self, event):
        self.undo()
        return "break"

    def clear_text(self):
        if not self.current_text:
            return

        self.undo_stack.append(self.current_text)

        self.editor.delete("1.0", "end")
        self.current_text = ""

        self.update_statistics()
        self.status.config(text="Text cleared")

    def open_file(self):
        path = filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt")]
        )

        if not path:
            return

        try:
            content = Path(path).read_text(encoding="utf-8")

            if content != self.current_text:
                self.undo_stack.append(self.current_text)

            self.loading = True
            self.editor.delete("1.0", "end")
            self.editor.insert("1.0", content)
            self.loading = False

            self.current_text = content
            self.update_statistics()

            self.status.config(text="File opened")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def save_file(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")]
        )

        if not path:
            return

        try:
            content = self.editor.get("1.0", "end-1c")
            Path(path).write_text(content, encoding="utf-8")

            self.status.config(text="File saved successfully")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_statistics(self):
        text = self.editor.get("1.0", "end-1c")

        words = len(text.split())
        characters = len(text)

        self.stack_count.config(text=str(len(self.undo_stack)))
        self.words_label.config(text=f"{words} words")
        self.chars_label.config(text=f"{characters} characters")


if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()