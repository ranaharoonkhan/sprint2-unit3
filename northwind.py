import sqlite3
conn = sqlite3.connect('northwind_samll.sqlite3')
cursor = conn.cursor()

query1 =f'''select ProductName, UnitPrice from ProductDetails_V order by UnitPrice DESC limit 10'''
query2 =f'''SELECT LastName , FirstName, HireDate - BirthDate as Avg_Age_At_Hiring from Employee'''

result1 = cursor.execute(query1).fetchall()
result2 = cursor.execute(query2).fetchall()

print(result1)
print(result2)