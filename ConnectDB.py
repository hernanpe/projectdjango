import sqlite3
database = "database.db"
connection = sqlite3.connect(database)
cursor = connection.cursor()

try:
	cursor.execute("DROP TABLE table1")

except:
	print("table1 non trouvee")
cursor.execute("CREATE TABLE table1(titre TEXT,auteur TEXT,annee INTEGER)")
cursor.execute("INSERT INTO table1(titre,auteur,annee) VALUES('titre1','nom1',2018)")
cursor.execute("INSERT INTO table1(titre,auteur,annee) VALUES('titre2','nom2',2017)")
connection.commit()
cursor.close()
connection.close()
connection = sqlite3.connect(database)
cursor = connection.cursor()
cursor.execute("SELECT * FROM table1 WHERE annee=2017")
print(list(cursor))
cursor.close()
connection.close()

connection = sqlite3.connect(database)
cursor = connection.cursor()
cursor.execute("SELECT * FROM table1 WHERE annee=2017")
c = list(cursor)
print(list(cursor))
cursor.close()
connection.close()
