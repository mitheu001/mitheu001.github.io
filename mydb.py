import mysql.connector
import passwords


hashed_password = passwords.hashed_password


# Connect to the MySQL database
mydb = mysql.connector.connect(
	host='localhost',
	user='joe',
	password='joe1234',
	database = 'passwords'
	)


mycursor = mydb.cursor()

# create table passwords
while True:
	# table_name = input("Enter the name of the table to check: ")
	table_name = "passwords"
	mycursor.execute(f"SHOW TABLES LIKE '{table_name}'")
	result = mycursor.fetchone()

	if result:
		print(f"Table '{table_name}' exists!")
		break 
	else:
		sql0 = "create table passwords (id int auto_increment, password varchar(255), primary key(id))"
		mycursor.execute(sql0)
		mydb.commit()

		print(f"Table created")


# # drop table
# sql = 'drop table passwords'
# mycursor.execute(sql)
# mydb.commit()

# insert the password into the MySQL database
sql1 = "insert into passwords (password) values (%s)"
val = (hashed_password,)
mycursor.execute(sql1, val)
mydb.commit()

print(mycursor.rowcount, "Password saved in database!")

# close connection
mydb.close()