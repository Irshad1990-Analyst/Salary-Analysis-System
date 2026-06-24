import sqlite3

# 1. Database-kku connect panrom
conn = sqlite3.connect('my_shop.db')
cursor = conn.cursor()

# 2. Excel-la irundhu vandha 'Sales_Report' table-ai select panrom
cursor.execute("SELECT * FROM Sales_Report")

# 3. Ella data-vaiyum eduthu print panrom
data = cursor.fetchall()

# 4. Modhal 5 row-ai mattum print panni paarunga (nammala confuse aagama irukka)
for row in data[:5]:
    print(row)

conn.close()