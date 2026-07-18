import sqlite3

connection = sqlite3.connect("sqlite.db", check_same_thread=False)
cursor = connection.cursor()

cursor.execute('''
''')