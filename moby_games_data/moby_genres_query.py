import json
import sqlite3

with open('moby_games_data/moby_g_genre_data.json', 'r') as json_file:
    games_data = json.load(json_file)

conn = sqlite3.connect('moby_g_genre.db')
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS Games (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    description TEXT,
                    moby_score DECIMAL(3, 1),
                    moby_url TEXT
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Genres (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    game_id INTEGER,
                    genre TEXT,
                    FOREIGN KEY (game_id) REFERENCES Games(id)
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Platforms (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    game_id INTEGER,
                    platform TEXT,
                    FOREIGN KEY (game_id) REFERENCES Games(id)
                )''')

# Insert data into tables
for game in games_data:
    #  Games table
    cursor.execute('''INSERT INTO Games (title, description, moby_score, moby_url)
                      VALUES (?, ?, ?, ?)''',
                   (game['Title'], game['Description'], game['Moby Score'], game['Moby URL']))
    game_id = cursor.lastrowid  # Get the ID of the last inserted row

    #  put  in Genres table
    for genre in game['Genres']:
        cursor.execute('''INSERT INTO Genres (game_id, genre) VALUES (?, ?)''', (game_id, genre))

    # put in platforms table
    for platform in game['Platforms']:
        cursor.execute('''INSERT INTO Platforms (game_id, platform) VALUES (?, ?)''', (game_id, platform))

conn.commit()
conn.close()
