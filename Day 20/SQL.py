# import mysql.connector

# # Connect to the MySQL Server
# mydb = mysql.connector.connect(
#   host="localhost",      
#   user="root",           
#   password="NEBcomputer137!!"  
# )

# # Create a cursor (the robot worker)
# cursor = mydb.cursor()

# # Let's ask MySQL to show us all existing databases
# cursor.execute("SHOW DATABASES")

# # Print them out so we can see it worked!
# print("Successfully connected! Here are your databases:")
# for db in cursor:
#   print(db)




import sqlite3

connection = sqlite3.connect('students.sqlite3')
terminal = connection.cursor()

# 1. FIX: Create the table if it doesn't exist yet!
terminal.execute('''
    CREATE TABLE IF NOT EXISTS students (
        name TEXT,
        address TEXT,
        collage TEXT,
        age INTEGER,
        gender TEXT,
        faculty TEXT,
        university TEXT
    )
''')

# 2. Insert Query
query = 'Insert into students (name, address, collage, age, gender, faculty, university) values ("John Doe", "123 Main St", "ABC University", 20, "Male", "XYZ University", "DEF University")'
terminal.execute(query)
connection.commit()

print("Data inserted successfully!") # Changed this so it's easier to read than the connection object

# 3. Select Query
query = 'SELECT * FROM students'
terminal.execute(query)   
results = terminal.fetchall()

# Print the final data
for row in results:
    print(row)



# Request Library if Legal
#Will scripe tommrow if legal, but I have to check the rules first. I don't want to get in trouble!
# Data Comes through an API, so we need to use the requests library to get it.
# database ma gayera database banaunu .