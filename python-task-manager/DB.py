import sqlite3
from tkinter import *
from tkinter import ttk

# Connect to the database or create one if it doesn't exist
conn = sqlite3.connect("records.db")
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS Records (
                    serial_number INTEGER PRIMARY KEY AUTOINCREMENT,
                    MTR INTEGER,
                    date TEXT,
                    ITEMS TEXT,
                    EQPT_SL_NO TEXT,
                    QTY TEXT,
                    UNIT TEXT,
                    COY TEXT,
                    CAT TEXT,
                    ORIGINATOR_REPORT TEXT,
                    TYPE_OF_REPAIR TEXT,
                    JC_NO TEXT,
                    DATE_OF_REPAIRED TEXT,
                    NAME_OF_TECH TEXT,
                    REMARKS TEXT)''')
conn.commit()

# Function to add a record
def add_record():
    cursor.execute("INSERT INTO Records (MTR, date, ITEMS, EQPT_SL_NO, QTY, UNIT, COY, CAT, ORIGINATOR_REPORT, TYPE_OF_REPAIR, JC_NO, DATE_OF_REPAIRED, NAME_OF_TECH, REMARKS) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                   (MTR.get(), date.get(), ITEMS.get(), EQPT_SL_NO.get(), QTY.get(), UNIT.get(), COY.get(), CAT.get(), ORIGINATOR_REPORT.get(), TYPE_OF_REPAIR.get(), JC_NO.get(), DATE_OF_REPAIRED.get(), NAME_OF_TECH.get(), REMARKS.get()))
    conn.commit()
    fetch_records()

    MTR.set("")
    date.set("")
    ITEMS.set("")
    EQPT_SL_NO.set("")
    QTY.set("")
    UNIT.set("")
    COY.set("")
    CAT.set("")
    ORIGINATOR_REPORT.set("")
    TYPE_OF_REPAIR.set("")
    JC_NO.set("")
    DATE_OF_REPAIRED.set("")
    NAME_OF_TECH.set("")
    REMARKS.set("")

# Function to fetch and display records
def fetch_records():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT * FROM Records")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", END, values=row)

# Function to search records by a specific column
def search_by_column():
    search_column = column_var.get()
    search_value = search_var.get()
    for row in tree.get_children():
        tree.delete(row)
    query = f"SELECT * FROM Records WHERE {search_column} LIKE ?"
    cursor.execute(query, (f"%{search_value}%",))
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", END, values=row)

# Function to delete a record
def delete_record():
    cursor.execute("DELETE FROM Records WHERE serial_number = ?", (serial_var.get(),))
    conn.commit()
    fetch_records()

# Function to refresh the records
def refresh_records():
    fetch_records()

# Initialize Tkinter root
tkwin = Tk()
tkwin.title("CRPF 4 Signal Data")
tkwin.geometry("1400x700")  # Adjusted window size

# Variables
serial_var = IntVar()
MTR = StringVar()
date = StringVar()
ITEMS = StringVar()
EQPT_SL_NO = StringVar()
QTY = StringVar()
UNIT = StringVar()
COY = StringVar()
CAT = StringVar()
ORIGINATOR_REPORT = StringVar()
TYPE_OF_REPAIR = StringVar()
JC_NO = StringVar()
DATE_OF_REPAIRED = StringVar()
NAME_OF_TECH = StringVar()
REMARKS = StringVar()
column_var = StringVar()
column_var.set("category")

# GUI Elements
Label(tkwin, text="MTR").grid(row=0, column=0, padx=10, pady=5)
Entry(tkwin, textvariable=MTR).grid(row=0, column=1, padx=10, pady=5)

Label(tkwin, text="DATE").grid(row=0, column=2, padx=10, pady=5)
Entry(tkwin, textvariable=date).grid(row=0, column=3, padx=10, pady=5)

Label(tkwin, text="ITEM").grid(row=0, column=4, padx=10, pady=5)
Entry(tkwin, textvariable=ITEMS).grid(row=0, column=5, padx=10, pady=5)

Label(tkwin, text="EQPT SL NO").grid(row=1, column=0, padx=10, pady=5)
Entry(tkwin, textvariable=EQPT_SL_NO).grid(row=1, column=1, padx=10, pady=5)

Label(tkwin, text="QTY").grid(row=1, column=2, padx=10, pady=5)
Entry(tkwin, textvariable=QTY).grid(row=1, column=3, padx=10, pady=5)

Label(tkwin, text="UNIT").grid(row=1, column=4, padx=10, pady=5)
Entry(tkwin, textvariable=UNIT).grid(row=1, column=5, padx=10, pady=5)

Label(tkwin, text="COY").grid(row=2, column=0, padx=10, pady=5)
Entry(tkwin, textvariable=COY).grid(row=2, column=1, padx=10, pady=5)

Label(tkwin, text="CAT").grid(row=2, column=2, padx=10, pady=5)
Entry(tkwin, textvariable=CAT).grid(row=2, column=3, padx=10, pady=5)

Label(tkwin, text="ORIGINATOR REPORT").grid(row=2, column=4, padx=10, pady=5)
Entry(tkwin, textvariable=ORIGINATOR_REPORT).grid(row=2, column=5, padx=10, pady=5)

Label(tkwin, text="TYPE OF REPAIR").grid(row=3, column=0, padx=10, pady=5)
Entry(tkwin, textvariable=TYPE_OF_REPAIR).grid(row=3, column=1, padx=10, pady=5)

Label(tkwin, text="J/C NO").grid(row=3, column=2, padx=10, pady=5)
Entry(tkwin, textvariable=JC_NO).grid(row=3, column=3, padx=10, pady=5)

Label(tkwin, text="DATE OF REPAIRED").grid(row=3, column=4, padx=10, pady=5)
Entry(tkwin, textvariable=DATE_OF_REPAIRED).grid(row=3, column=5, padx=10, pady=5)

Label(tkwin, text="NAME OF TECH").grid(row=4, column=0, padx=10, pady=5)
Entry(tkwin, textvariable=NAME_OF_TECH).grid(row=4, column=1, padx=10, pady=5)

Label(tkwin, text="REMARKS").grid(row=4, column=2, padx=10, pady=5)
Entry(tkwin, textvariable=REMARKS).grid(row=4, column=3, padx=10, pady=5)

Button(tkwin, text="Add Record", command=add_record).grid(row=5, column=1, pady=10)

# Search Section
Label(tkwin, text="Search Column").grid(row=6, column=0, padx=10, pady=5)
OptionMenu(tkwin, column_var, "serial_number", "MTR", "ITEMS", "EQPT_SL_NO", "COY", "CAT", "ORIGINATOR_REPORT").grid(row=6, column=1, padx=10, pady=5)

Label(tkwin, text="Search Value").grid(row=7, column=0, padx=10, pady=5)
search_var = StringVar()
Entry(tkwin, textvariable=search_var).grid(row=7, column=1, padx=10, pady=5)
Button(tkwin, text="Search", command=search_by_column).grid(row=8, column=1, pady=10)

# Treeview for displaying records with scrollbar
tree_frame = Frame(tkwin)
tree_frame.grid(row=9, column=0, columnspan=6, pady=20)

# Adding the Treeview widget with vertical and horizontal scrollbars
tree = ttk.Treeview(tree_frame, columns=("Serial", "MTR", "Date", "Item", "Eqpt SL No", "Qty", "Unit", "Coy", "Cat", "Originator Report", "Repair Type", "JC No", "Date of Repair", "Tech Name", "Remarks"), show="headings", height=20)

columns = ("Serial", "MTR", "Date", "Item", "Eqpt SL No", "Qty", "Unit", "Coy", "Cat", "Originator Report", "Repair Type", "JC No", "Date of Repair", "Tech Name", "Remarks")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=90, anchor="center")  # Adjusted the width to make sure columns are visible

# Adding scrollbars
vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
vsb.pack(side="right", fill="y")
tree.configure(yscrollcommand=vsb.set)

hsb = ttk.Scrollbar(tree_frame, orient="horizontal", command=tree.xview)
hsb.pack(side="bottom", fill="x")
tree.configure(xscrollcommand=hsb.set)

tree.pack()

Entry(tkwin, textvariable=serial_var).grid(row=7, column=3, padx=10, pady=5)
Button(tkwin, text="Delete Record", command=delete_record).grid(row=7, column=4, pady=10)
Button(tkwin, text="Refresh", command=refresh_records).grid(row=7, column=5, pady=10)

fetch_records()
tkwin.mainloop()

# Close database connection when done
conn.close()
