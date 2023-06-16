import pandas as pd
import mysql.connector


# Import CSV
data = pd.read_csv (r'd://products.csv')   
df = pd.DataFrame(data)

# Connect to SQL Server
conn = mysql.connector.connect(
				 host = "localhost",
				 database = "accenture",
				 user = "root",
				 password = "root",
				 port = "3306"
		)
cursor = conn.cursor()


# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO products (product_id, product_name, price)
                VALUES (?,?,?)
                ''',
                row.product_id, 
                row.product_name,
                row.price
                )
conn.commit()
print("data written")