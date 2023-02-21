import oracledb

# Set up the connection details for the first database
hostname1 = '<hostname>'
port1 = '<port>'
service_name1 = '<service_name>'
username1 = '<username>'
password1 = '<password>'
dsn1 = f"(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST={hostname1})(PORT={port1}))(CONNECT_DATA=(SERVICE_NAME={service_name1})))"

# Set up the connection details for the second database
hostname2 = '<hostname>'
port2 = '<port>'
service_name2 = '<service_name>'
username2 = '<username>'
password2 = '<password>'
dsn2 = f"(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST={hostname2})(PORT={port2}))(CONNECT_DATA=(SERVICE_NAME={service_name2})))"

# Establish the connection to the first database
connection1 = oracledb.connect(user=username1, password=password1, dsn=dsn1)

# Establish the connection to the second database
connection2 = oracledb.connect(user=username2, password=password2, dsn=dsn2)

# Define the table to compare
table = '<your_schema>.<your_table>'

# Get the data from the first table
cursor1 = connection1.cursor()
cursor1.execute(f'SELECT * FROM {table}')
data1 = cursor1.fetchall()

# Get the data from the second table
cursor2 = connection2.cursor()
cursor2.execute(f'SELECT * FROM {table}')
data2 = cursor2.fetchall()

# Compare the data in the two tables
for i in range(len(data1)):
    for j in range(len(data1[i])):
        if data1[i][j] != data2[i][j]:
            print(f"Row {i+1}, Column {j+1}: Database 1 value is {data1[i][j]}, Database 2 value is {data2[i][j]}")

# Close the cursors and the connections
cursor1.close()
cursor2.close()
connection1.close()
connection2.close()
