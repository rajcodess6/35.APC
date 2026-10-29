import csv
import os
import tkinter as tk
from tkinter import ttk

FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt")
FIELDS = ("Name", "Division", "Mobile", "Branch", "Email")

# New color theme
PRIMARY = "#0f766e"
PRIMARY_DARK = "#115e59"
BG = "#f0fdfa"
CARD = "#ffffff"
TEXT = "#134e4a"
MUTED = "#64748b"
ACCENT = "#ccfbf1"


def submit():
    values = [entries[f].get().strip() for f in FIELDS]

    if "" in values:
        result.config(text="⚠ Please fill in all fields", fg="#dc2626")
        return

    with open(FILE, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow(values)

    for entry in entries.values():
        entry.delete(0, tk.END)

    entries["Name"].focus()
    result.config(text="✓ Record saved successfully!", fg=PRIMARY)


def read():
    page = tk.Toplevel(root)
    page.title("Student Records")
    page.geometry("900x480")
    page.configure(bg=BG)

    header = tk.Frame(page, bg=PRIMARY)
    header.pack(fill="x")

    tk.Label(
        header, text="📋  Student Records",
        font=("Segoe UI", 20, "bold"),
        bg=PRIMARY, fg="white"
    ).pack(pady=18)

    frame = tk.Frame(page, bg=CARD)
    frame.pack(fill="both", expand=True, padx=22, pady=20)

    table = ttk.Treeview(frame, columns=FIELDS, show="headings")
    widths = {
        "Name": 160, "Division": 90, "Mobile": 140,
        "Branch": 140, "Email": 260
    }

    for col in FIELDS:
        table.heading(col, text=col)
        table.column(col, width=widths[col], anchor="center")

    table.tag_configure("odd", background="#ccfbf1")

    scroll = ttk.Scrollbar(
        frame, orient="vertical", command=table.yview
    )
    table.configure(yscrollcommand=scroll.set)

    table.pack(side="left", fill="both", expand=True)
    scroll.pack(side="right", fill="y")

    count = 0

    try:
        with open(FILE, newline="", encoding="utf-8") as f:
            for row in csv.reader(f):
                if len(row) == 5:
                    tag = ("odd",) if count % 2 else ()
                    table.insert("", "end", values=row, tags=tag)
                    count += 1
    except FileNotFoundError:
        pass

    tk.Label(
        page,
        text=f"Total records: {count}" if count else "No records found",
        font=("Segoe UI", 11, "bold"),
        bg=BG, fg=MUTED
    ).pack(pady=(0, 15))


# Main window
root = tk.Tk()
root.title("Student Application")
root.geometry("500x700")
root.configure(bg=BG)
root.resizable(False, False)

# Table styling
style = ttk.Style()
style.theme_use("clam")
style.configure(
    "Treeview", rowheight=32,
    font=("Segoe UI", 10),
    background="white", fieldbackground="white"
)
style.configure(
    "Treeview.Heading",
    font=("Segoe UI", 10, "bold"),
    background=PRIMARY, foreground="white"
)
style.map(
    "Treeview.Heading",
    background=[("active", PRIMARY_DARK)]
)

# Header
header = tk.Frame(root, bg=PRIMARY)
header.pack(fill="x")

tk.Label(
    header, text="STUDENT APPLICATION",
    font=("Segoe UI", 21, "bold"),
    bg=PRIMARY, fg="white"
).pack(pady=(24, 5))

tk.Label(
    header, text="Enter your details below",
    font=("Segoe UI", 11),
    bg=PRIMARY, fg="#ccfbf1"
).pack(pady=(0, 24))

# Form card
card = tk.Frame(
    root, bg=CARD,
    highlightbackground="#99f6e4",
    highlightthickness=1
)
card.pack(fill="x", padx=28, pady=25)

entries = {}

for field in FIELDS:
    tk.Label(
        card, text=field,
        font=("Segoe UI", 10, "bold"),
        bg=CARD, fg=TEXT, anchor="w"
    ).pack(fill="x", padx=22, pady=(12, 4))

    entry = tk.Entry(
        card, font=("Segoe UI", 11),
        relief="flat", bg="#f8fafc", fg=TEXT,
        insertbackground=PRIMARY,
        highlightthickness=1,
        highlightbackground="#cbd5e1",
        highlightcolor=PRIMARY
    )
    entry.pack(fill="x", padx=22, ipady=7)
    entries[field] = entry

tk.Frame(card, bg=CARD, height=18).pack()


def make_button(parent, text, command, primary=True):
    bg = PRIMARY if primary else "#d1fae5"
    hover = PRIMARY_DARK if primary else "#a7f3d0"
    fg = "white" if primary else TEXT

    button = tk.Button(
        parent, text=text, command=command,
        font=("Segoe UI", 11, "bold"),
        bg=bg, fg=fg,
        activebackground=hover,
        activeforeground=fg,
        relief="flat", width=13,
        pady=10, cursor="hand2", bd=0
    )

    button.bind("<Enter>", lambda e: button.config(bg=hover))
    button.bind("<Leave>", lambda e: button.config(bg=bg))
    return button


buttons = tk.Frame(root, bg=BG)
buttons.pack(pady=3)

make_button(buttons, "✓  Submit", submit).pack(side="left", padx=8)
make_button(buttons, "▤  Read Records", read, False).pack(side="left", padx=8)

result = tk.Label(
    root, text="",
    font=("Segoe UI", 10, "bold"),
    bg=BG
)
result.pack(pady=16)

tk.Label(
    root, text="STUDENT PORTAL  •  RECORD MANAGEMENT",
    font=("Segoe UI", 8),
    bg=BG, fg=MUTED
).pack(side="bottom", pady=12)

root.bind("<Return>", lambda event: submit())
entries["Name"].focus()

root.mainloop()