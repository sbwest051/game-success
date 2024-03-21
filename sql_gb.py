import sqlite3
import json


create_review_table = """
CREATE TABLE IF NOT EXISTS user_reviews (
    guid VARCHAR,
    game_name VARCHAR,
    score INTEGER,
    review_date DATETIME
);
"""

create_allgb_table = """
CREATE TABLE IF NOT EXISTS games (
    guid,
    name VARCHAR,
    description VARCHAR,
    number_of_user_reviews INTEGER,
    original_release_date DATE
);
"""


conn = sqlite3.connect('gb_database.db')


conn.execute(create_review_table)
conn.execute(create_allgb_table)


def insert_review_data(conn, val):
    guid = str(val['guid'])
    # print(guid)
    # game_id = val['game']['id'] if val.get('game') else None
    game_name = str(val['game']['name']) if val.get('game') else None
    # print(game_name)
    # reviewer = val['reviewer']
    score = int(val['score'])
    # print(score)
    review_date = val['date_added']

    # print(review_date)
    # review_title = val['deck']  
    # review_body = val['description']  
    
    insert_query = """
    INSERT INTO user_reviews (guid, game_name, score, review_date)
    VALUES (?, ?, ?, ?)
    """
    conn.execute(insert_query, (guid, game_name, score, review_date))

def insert_big_data(conn, val):
    guid = str(val['guid'])
    # print(guid)
    # game_id = val['game']['id'] if val.get('game') else None
    game_name = str(val['name']) #if val.get('game') else None
    description = str(val['deck'])
    original_release_date = val["original_release_date"] if val['original_release_date'] else ""
    number_of_user_reviews = int(val["number_of_user_reviews"])

    
    insert_query = """
    INSERT INTO games (guid, name, description, number_of_user_reviews, original_release_date)
    VALUES (?, ?, ?, ?, ?)
    """
    conn.execute(insert_query, (guid, game_name, description, number_of_user_reviews, original_release_date))

# UNCOMMENT WHEN CREATING DATABASE FOR REVIEWS
with open('gb_reviews_json.json', 'r') as file:
    reviews = json.load(file)
    for review in reviews:
        insert_review_data(conn, review)

with open('gb1_json.json', 'r') as file:
    values = json.load(file)
    for v in values:
        insert_big_data(conn, v)


conn.commit()
conn.close()
