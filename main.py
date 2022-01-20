import sqlite3

banco = sqlite3.connect('gamedata.db')
cursor = banco.cursor()

# cursor.execute("INSERT INTO games(BLUE_TEAM,RED_TEAM) VALUES (1,2)")
# banco.commit()
cursor.execute("SELECT teams.NAME FROM teams INNER JOIN games ON teams.ID_TEAM = games.BLUE_TEAM")
print(cursor.fetchall())
banco.close()


