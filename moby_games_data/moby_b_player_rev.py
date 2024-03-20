import json
import sqlite3

# Load JSON data
with open('moby_games_data/best_player_reviews', 'r') as json_file:
    reviews_data = json.load(json_file)

# Create SQLite connection
conn = sqlite3.connect('moby_best_player_reviews.db')
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
for review in reviews_data:
    # Insert into Games table
    cursor.execute('''INSERT INTO Games (id, title, release_date, moby_score, moby_url)
                      VALUES (?, ?, ?, ?, ?)''',
                   (review['id'], review['title'], review['release_date'], review['moby_score'], review['moby_url']))

    # Insert developers into Developers table
    for developer in review['developers']:
        cursor.execute('''INSERT OR IGNORE INTO Developers (name) VALUES (?)''', (developer,))

    # Insert genres into Genres table
    for genre in review['genres']:
        cursor.execute('''INSERT OR IGNORE INTO Genres (name) VALUES (?)''', (genre,))

    # Insert platforms into Platforms table
    for platform in review['platforms']:
        cursor.execute('''INSERT OR IGNORE INTO Platforms (name) VALUES (?)''', (platform,))

    # Insert publishers into Publishers table
    for publisher in review['publishers']:
        cursor.execute('''INSERT OR IGNORE INTO Publishers (name) VALUES (?)''', (publisher,))

# Commit changes and close connection
conn.commit()
conn.close()
