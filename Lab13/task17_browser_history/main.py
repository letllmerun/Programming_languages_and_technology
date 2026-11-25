import tkinter as tk
from tkinter import messagebox
from urllib.parse import urlparse

BG = "#101827"
PANEL = "#182438"
CARD = "#213149"
ACCENT = "#8B9CFF"
TEXT = "#F2F5FC"
MUTED = "#A7B3C8"
GREEN = "#57D6A0"


class BrowserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Orbit Browser")
        self.root.geometry("1080x720")
        self.root.configure(bg=BG)

        self.back_stack = []
        self.forward_stack = []
        self.current_url = ""
        self.visited = []

        self.build_ui()
        self.refresh()

    def build_ui(self):
        header = tk.Frame(self.root, bg=BG)
        header.pack(fill="x", padx=28, pady=22)

        tk.Label(
            header, text="orbit",
            bg=BG, fg=TEXT,
            font=("Segoe UI", 28, "bold")
        ).pack(side="left")

        tk.Label(
            header, text="  BROWSER HISTORY",
            bg=BG, fg=ACCENT,
            font=("Segoe UI", 10, "bold")
        ).pack(side="left", pady=15)

        browser = tk.Frame(self.root, bg=PANEL, padx=15, pady=15)
        browser.pack(fill="x", padx=28)

        navigation = tk.Frame(browser, bg=PANEL)
        navigation.pack(fill="x")

        self.back_button = self.button(
            navigation, "←", self.go_back, CARD
        )
        self.back_button.pack(side="left")

        self.forward_button = self.button(
            navigation, "→", self.go_forward, CARD
        )
        self.forward_button.pack(side="left", padx=7)

        self.url_entry = tk.Entry(
            navigation,
            bg="#0D1522",
            fg=TEXT,
            insertbackground=ACCENT,
            relief="flat",
            font=("Segoe UI", 12)
        )
        self.url_entry.pack(
            side="left", fill="x",
            expand=True, padx=12, ipady=10
        )

        self.url_entry.bind(
            "<Return>",
            lambda event: self.navigate()
        )

        self.button(
            navigation, "Go", self.navigate, GREEN
        ).pack(side="right")

        tk.Label(
            browser,
            text="Enter a website address and press Enter.",
            bg=PANEL, fg=MUTED,
            font=("Segoe UI", 9)
        ).pack(anchor="w", pady=10)

        body = tk.Frame(self.root, bg=BG)
        body.pack(fill="both", expand=True, padx=28, pady=15)

        page = tk.Frame(body, bg=PANEL, padx=22, pady=22)
        page.pack(side="left", fill="both", expand=True)

        tk.Label(
            page, text="CURRENT PAGE",
            bg=PANEL, fg=MUTED,
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w")

        self.page_title = tk.Label(
            page,
            text="Welcome to Orbit",
            bg=PANEL, fg=TEXT,
            font=("Segoe UI", 22, "bold")
        )
        self.page_title.pack(anchor="w", pady=25)

        self.page_url = tk.Label(
            page,
            text="Enter a URL to start browsing",
            bg=PANEL, fg=ACCENT,
            font=("Segoe UI", 12)
        )
        self.page_url.pack(anchor="w")

        tk.Frame(
            page, bg=CARD, height=2
        ).pack(fill="x", pady=25)

        self.description = tk.Label(
            page,
            text="Your current page will appear here.",
            bg=PANEL, fg=MUTED,
            font=("Segoe UI", 11),
            justify="left"
        )
        self.description.pack(anchor="w")

        sidebar = tk.Frame(body, bg=PANEL, width=260, padx=15, pady=15)
        sidebar.pack(side="right", fill="y", padx=(15, 0))
        sidebar.pack_propagate(False)

        tk.Label(
            sidebar,
            text="HISTORY STACKS",
            bg=PANEL, fg=MUTED,
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w")

        self.back_count = tk.Label(
            sidebar,
            text="BACK: 0",
            bg=PANEL, fg=ACCENT,
            font=("Segoe UI", 15, "bold")
        )
        self.back_count.pack(anchor="w", pady=12)

        self.forward_count = tk.Label(
            sidebar,
            text="FORWARD: 0",
            bg=PANEL, fg=GREEN,
            font=("Segoe UI", 15, "bold")
        )
        self.forward_count.pack(anchor="w")

        tk.Frame(
            sidebar, bg=CARD, height=2
        ).pack(fill="x", pady=20)

        tk.Label(
            sidebar,
            text="VISITED PAGES",
            bg=PANEL, fg=MUTED,
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w")

        self.history_list = tk.Listbox(
            sidebar,
            bg="#0D1522",
            fg=TEXT,
            selectbackground="#43527B",
            relief="flat",
            font=("Segoe UI", 9)
        )
        self.history_list.pack(fill="both", expand=True, pady=12)

        self.history_list.bind(
            "<Double-Button-1>",
            self.open_selected
        )

        footer = tk.Frame(
            self.root, bg="#0B1220", padx=28, pady=10
        )
        footer.pack(fill="x")

        self.status = tk.Label(
            footer, text="Ready",
            bg="#0B1220", fg=MUTED
        )
        self.status.pack(side="left")

        tk.Label(
            footer,
            text="Python | Two Stacks | LIFO",
            bg="#0B1220", fg=MUTED
        ).pack(side="right")

    def button(self, parent, text, command, color):
        return tk.Button(
            parent,
            text=text,
            command=command,
            bg=color,
            fg=TEXT,
            relief="flat",
            padx=15,
            pady=9,
            font=("Segoe UI", 10, "bold"),
            cursor="hand2"
        )

    def normalize_url(self, url):
        url = url.strip()

        if not url:
            return None

        if "://" not in url:
            url = "https://" + url

        parsed = urlparse(url)

        if not parsed.netloc or "." not in parsed.netloc:
            return None

        return url

    def navigate(self):
        new_url = self.normalize_url(
            self.url_entry.get()
        )

        if not new_url:
            messagebox.showwarning(
                "Invalid URL",
                "Enter a valid address, for example google.com"
            )
            return

        if new_url == self.current_url:
            return

        if self.current_url:
            self.back_stack.append(self.current_url)

        # A new navigation clears the forward stack.
        self.forward_stack.clear()

        self.current_url = new_url
        self.visited.append(new_url)

        self.refresh("Navigation completed")

    def go_back(self):
        if not self.back_stack:
            self.status.config(text="No previous page")
            return

        self.forward_stack.append(self.current_url)
        self.current_url = self.back_stack.pop()

        self.refresh("Moved backward")

    def go_forward(self):
        if not self.forward_stack:
            self.status.config(text="No next page")
            return

        self.back_stack.append(self.current_url)
        self.current_url = self.forward_stack.pop()

        self.refresh("Moved forward")

    def open_selected(self, event=None):
        selection = self.history_list.curselection()

        if not selection:
            return

        url = self.history_list.get(selection[0])
        self.url_entry.delete(0, "end")
        self.url_entry.insert(0, url)

        self.navigate()

    def refresh(self, message="Ready"):
        self.url_entry.delete(0, "end")
        self.url_entry.insert(0, self.current_url)

        self.back_count.config(
            text=f"BACK: {len(self.back_stack)}"
        )

        self.forward_count.config(
            text=f"FORWARD: {len(self.forward_stack)}"
        )

        self.back_button.config(
            state="normal" if self.back_stack else "disabled"
        )

        self.forward_button.config(
            state="normal" if self.forward_stack else "disabled"
        )

        if self.current_url:
            host = urlparse(self.current_url).netloc

            self.page_title.config(
                text=f"You opened: {host}"
            )

            self.page_url.config(
                text=self.current_url
            )

            self.description.config(
                text="This page is stored in your browser history.\n"
                     "Use Back and Forward to navigate between pages."
            )

        else:
            self.page_title.config(
                text="Welcome to Orbit"
            )

            self.page_url.config(
                text="Enter a URL to start browsing"
            )

        self.history_list.delete(0, "end")

        for url in reversed(self.visited):
            self.history_list.insert("end", url)

        self.status.config(text=message)


if __name__ == "__main__":
    root = tk.Tk()
    app = BrowserApp(root)
    root.mainloop()