import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://www.mobygames.com/game/from:2000/until:2023/sort:critic_score/page:1/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the table containing the game information
table = soup.find("table", class_="table")

# Initialize lists to store data
games = []

# Loop through each row in the table
for row in table.find_all("tr"):
    # Initialize dictionary to store game details
    game_info = {}
    # Find all cells in the row
    cells = row.find_all("td")
    if len(cells) > 0:  # Ensure it's not a header row
        # Extract data and store it in the dictionary
        game_info["title"] = cells[0].a.text.strip()
        game_info["critic_score"] = cells[1].div.text.strip()
        game_info["year"] = cells[2].text.strip()
        game_info["developer"] = cells[3].text.strip()
        # Append the dictionary to the list of games
        games.append(game_info)

# Print the extracted data
for game in games:
    print(game)
