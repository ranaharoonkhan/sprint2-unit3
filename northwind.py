import sqlite3
import pandas as pd
conn = sqlite3.connect('northwind_small.sqlite3')
cursor = conn.cursor()

# Part--2

query1 =f'''select ProductName, UnitPrice from ProductDetails_V order by UnitPrice DESC limit 10'''
query2 =f'''SELECT LastName , FirstName, HireDate - BirthDate as Avg_Age_At_Hiring from Employee'''

# Part--3

query3 =f'''SELECT ProductDetails_V.ProductName, ProductDetails_V.UnitPrice,Supplier.CompanyName from ProductDetails_V
            inner join Supplier on ProductDetails_V.SupplierId = Supplier.Id
            order by UnitPrice DESC limit 10'''

query4 =f'''select Category.CategoryName,count(distinct Product.ProductName) as No_Of_Product from Product
            join Category on Product.CategoryId = Category.Id
            group by CategoryId
            order by No_Of_Product DESC'''

Strech_query = '''select Employee.FirstName, Employee.LastName, EmployeeTerritory.EmployeeId,count(EmployeeTerritory.TerritoryId) as Max_Territory from EmployeeTerritory
                  join Employee on EmployeeTerritory.EmployeeId = Employee.Id
                  group by EmployeeId
                  order by Max_Territory  DESC'''



result1 = cursor.execute(query1).fetchall()
result2 = cursor.execute(query2).fetchall()
result3 = cursor.execute(query3).fetchall()
result4 = cursor.execute(query4).fetchall()
result_strech = cursor.execute(Strech_query).fetchall()

ans = pd.DataFrame(result1, columns =['Product Name', 'Unit Price'])
ans1 = pd.DataFrame(result2, columns =['Last Name','First Name','Age at Hiring'])
ans2 = pd.DataFrame(result3, columns =['Product Name', 'Unit Price','Supplier Name'])
ans3 = pd.DataFrame(result4, columns =['Category Name', 'No Of Products'])
ans4 = pd.DataFrame(result_strech, columns =['First Name','Last Name','Emp ID','No Of Territories'])

print(ans)
print(ans1)
print(ans2)
print(ans3)
print(ans4)

