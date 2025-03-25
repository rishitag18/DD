import sqlite3

# Connect to the database
conn = sqlite3.connect('signup.db')

# Create a cursor
c = conn.cursor()

# Retrieve all the data from the table
c.execute("SELECT * FROM info")

# Fetch all the data
data = c.fetchall()

# Loop through the data and print out each row
print("User\t\tEmail\t\tPassword\t\tMobile\t\tName")
for row in data:
    print(row[0],end="\t\t")
    print(row[1],end="\t\t")
    print(row[2],end="\t\t")
    print(row[3],end="\t\t")
    print(row[4],end="\n")

# Commit the changes
conn.commit()

# Close the connection
conn.close()