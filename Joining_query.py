import sqlite3
import csv


conn = sqlite3.connect('gb_database.db')


conn.execute("ATTACH DATABASE 'igdb.db' AS ig")


query = """
WITH subquery AS (
  SELECT
    game_name,
    AVG(score) / 5 AS average_score,
    COUNT(*) AS gb_review_count 
  FROM
    user_reviews 
  GROUP BY
    game_name
)
SELECT
  sq.game_name,
  sq.average_score,
  sq.gb_review_count,
  ig.id,
  ig.name,
  ig.Genre1,
  ig.Genre2,
  ig.Genre3,
  ig.Genre4,
  ig.Genre5,
  ig.Involved_company1,
  ig.Involved_company2,
  ig.rating,
  ig.rating_count,
  ig.franchise_len,
  ig.first_release_date,
  ig.multiplayer  
FROM
  subquery sq
JOIN
  ig.IGDB_Games ig
ON
  sq.game_name = ig.name;

"""
cursor = conn.cursor()
cursor.execute(query)
rows = cursor.fetchall()
headers = [description[0] for description in cursor.description]


with open('output.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(headers)
    csv_writer.writerows(rows)


conn.close()
