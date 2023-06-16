

def get_records_count(cursor):
	cursor.execute("select * from dept")
	return len(cursor.fetchall())
