import cx_Oracle

# Set up the connection for the first database
dsn_tns1 = cx_Oracle.makedsn('hostname1', 'port1', service_name='service_name1')
conn1 = cx_Oracle.connect(user='username1', password='password1', dsn=dsn_tns1)

# Set up the connection for the second database
dsn_tns2 = cx_Oracle.makedsn('hostname2', 'port2', service_name='service_name2')
conn2 = cx_Oracle.connect(user='username2', password='password2', dsn=dsn_tns2)

# Define the name of the table to compare
table_name = 'table_name'

# Get the list of columns for the table from the first database
cursor1 = conn1.cursor()
cursor1.execute(f"SELECT column_name FROM all_tab_columns WHERE table_name='{table_name}'")
cols1 = [row[0] for row in cursor1.fetchall()]
cursor1.close()

# Get the list of columns for the table from the second database
cursor2 = conn2.cursor()
cursor2.execute(f"SELECT column_name FROM all_tab_columns WHERE table_name='{table_name}'")
cols2 = [row[0] for row in cursor2.fetchall()]
cursor2.close()

# Compare the two lists of columns
if cols1 != cols2:
    print("The tables have different columns:")
    print(f"Columns in {dsn_tns1}: {cols1}")
    print(f"Columns in {dsn_tns2}: {cols2}")
    conn1.close()
    conn2.close()
    exit()

# Get the data for the table from the first database
cursor1 = conn1.cursor()
cursor1.execute(f"SELECT * FROM {table_name}")
rows1 = cursor1.fetchall()
cursor1.close()

# Get the data for the table from the second database
cursor2 = conn2.cursor()
cursor2.execute(f"SELECT * FROM {table_name}")
rows2 = cursor2.fetchall()
cursor2.close()

# Compare the two sets of data
if len(rows1) != len(rows2):
    print("The tables have a different number of rows.")
    conn1.close()
    conn2.close()
    exit()

for row_num, (row1, row2) in enumerate(zip(rows1, rows2)):
    for col_num, (col_name, col1, col2) in enumerate(zip(cols1, row1, row2)):
        if col1 != col2:
            print(f"Data in row {row_num+1} and column {col_name} is different:")
            print(f"{dsn_tns1}: {col1}")
            print(f"{dsn_tns2}: {col2}")

# Close the database connections
conn1.close()
conn2.close()
