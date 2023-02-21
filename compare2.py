import oracledb

# Set up the connections
dsn1 = oracledb.makedsn(host='<your_host_1>', port='<your_port_1>', service_name='<your_service_name_1>')
connection1 = oracledb.connect(user='<your_username_1>', password='<your_password_1>', dsn=dsn1)

dsn2 = oracledb.makedsn(host='<your_host_2>', port='<your_port_2>', service_name='<your_service_name_2>')
connection2 = oracledb.connect(user='<your_username_2>', password='<your_password_2>', dsn=dsn2)

# Define the tables to compare
table1 = 'schema1.table1'
table2 = 'schema2.table2'

# Get the data from the first table
cursor1 = connection1.cursor()
cursor1.execute(f'SELECT * FROM {table1}')
data1 = cursor1.fetchall()

# Get the data from the second table
cursor2 = connection2.cursor()
cursor2.execute(f'SELECT * FROM {table2}')
data2 = cursor2.fetchall()

# Compare the data from the two tables
if data1 == data2:
    print(f"The data in {table1} from database 1 and {table2} from database 2 is the same.")
else:
    print(f"The data in {table1} from database 1 and {table2} from database 2 is different.")

# Close the cursors and the connections
cursor1.close()
cursor2.close()
connection1.close()
connection2.close()
