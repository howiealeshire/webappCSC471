import psycopg2

def print_to_server():
	
		
		conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='shrimp'")
		cur = conn.cursor()
		my_look_up("departmentNum","Department",cur)

		
		my_delete("Department"," \"Department\".\"departmentNum\" ",cur)
		
		my_look_up("departmentNum","Department",cur)
		my_insert("Department","departmentNum",3,cur)
		my_look_up("departmentNum","Department",cur)
		
		my_update("Department","departmentNum",11,"departmentNum",3,cur)
		my_look_up("departmentNum","Department",cur)
		

		print("connected!")
	
	
		print("I am unable to connect to the database")
	

def my_look_up(field,table,cur):
	cur.execute(""" SELECT \"{}\" FROM \"{}\" """.format(field,table))
	print(cur.fetchall())
	

def my_delete(table,condition,cur):
	cur.execute(""" DELETE FROM \"{}\"  WHERE {} = '3' """.format(table,condition))
	
	

def my_insert(table,columns,fields,cur):
	cur.execute(""" INSERT INTO \"{}\" (\"{}\") VALUES (\'{}\') """.format(table,columns,fields))

	
	


def my_update(table,set_field,val_set_field,where_field,where_field_val,cur):	
		cur.execute(""" UPDATE \"{}\" SET \"{}\" = \'{}\' WHERE \"{}\" = \'{}\'		""".format(table,set_field,val_set_field,where_field,where_field_val))


	