import sqlite3

## Connect to sqlite
connection = sqlite3.connect("student.db")

## Creating a cursor to insert, update, retrieve table data
cursor=connection.cursor()

## Create the table
table_info = """
create table student(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);
"""

cursor.execute(table_info)

## Inserting records into table

cursor.execute('''insert into STUDENT values ('Manish', 'Data Science', 'A', 90)''')
cursor.execute('''insert into STUDENT values ('Amit', 'Junior MIS', 'C', 60)''')
cursor.execute('''insert into STUDENT values ('Dhiraj', 'MIS', 'B', 60)''')
cursor.execute('''insert into STUDENT values ('Sanjay', 'HR', 'B', 60)''')
cursor.execute('''insert into STUDENT values ('Rahul', 'Executive', 'B', 70)''')

## Display all the records
print("The inserted records are:")
data = cursor.execute('''select * from student''')

for row in data:
    print(row)


print(data)
## Close the connection
connection.commit()
connection.close()