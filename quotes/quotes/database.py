import sqlite3

conn = sqlite3.connect("quotes.db")
curr = conn.cursor()

# curr.execute("""create table quote_table( title text, author text)""")

curr.execute("""insert into quote_table values( "python is cool" , "praveen")""")
conn.commit()
conn.close()
