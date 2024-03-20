import json
import sqlite3

# Load JSON data
with open('moby_games_data/games_moby_data.json', 'r') as json_file:
    games_data = json.load(json_file)

# Create an SQLite connection
conn = sqlite3.connect('moby_all_games.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''CREATE TABLE IF NOT EXISTS Games (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    release_date DATE,
                    moby_score DECIMAL(5, 2),
                    moby_url TEXT
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Developers (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Genres (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Platforms (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Publishers (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                )''')

# Insert data into tables
for game in games_data:
    # Insert into Games table
    # Insert into Games table with INSERT OR REPLACE
    cursor.execute('''INSERT OR REPLACE INTO Games (id, title, release_date, moby_score, moby_url)
                    VALUES (?, ?, ?, ?, ?)''',
                (game['id'], game['title'], game['release_date'], game['moby_score'], game['moby_url']))


    # Insert developers into Developers table
    for developer in game['developers']:
        cursor.execute('''INSERT OR IGNORE INTO Developers (name) VALUES (?)''', (developer,))

    # Insert genres into Genres table
    for genre in game['genres']:
        cursor.execute('''INSERT OR IGNORE INTO Genres (name) VALUES (?)''', (genre,))

    # Insert platforms into Platforms table
    for platform in game['platforms']:
        cursor.execute('''INSERT OR IGNORE INTO Platforms (name) VALUES (?)''', (platform,))

    # Insert publishers into Publishers table
    for publisher in game['publishers']:
        cursor.execute('''INSERT OR IGNORE INTO Publishers (name) VALUES (?)''', (publisher,))

# Commit changes and close connection
conn.commit()
conn.close()
