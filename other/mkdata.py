import sqlite3

#INVENTORY
'''

db = sqlite3.connect("inventory")

c = db.cursor()

c.execute("CREATE TABLE inventory(Item TEXT, Quantity INTEGER, Price INTEGER)")
c.execute("INSERT INTO inventory VALUES('Horn', 50, 1000)")
c.execute("INSERT INTO inventory VALUES('Bubble', 100, 10)")
c.execute("INSERT INTO inventory VALUES('Rainbow', 150, 150)")

db.commit()
db.close()



#ORDERS

db = sqlite3.connect("orders")

c = db.cursor()

c.execute("CREATE TABLE orders(Date TEXT, Item1 TEXT, Q1 INTEGER, Item2 TEXT, Q2 INTEGER, Item3 TEXT, Q3 INTEGER, Total INTEGER, Done INTEGER)")
c.execute("INSERT INTO orders VALUES('10/01/17','Horn', 25, 'Bubble', 10, NULL, NULL, 2600, 1)")
c.execute("INSERT INTO orders VALUES('10/05/17','Bubble', 20, NULL, NULL, NULL, NULL, 200, 1)")
c.execute("INSERT INTO orders VALUES('10/10/17','Rainbow', 12, 'Horn', 5, 'Bubble', 2, 6820, 0)")

db.commit()
db.close()
'''

#EXPENSES
#UNICORNS
#STAFF


